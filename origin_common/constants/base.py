from collections import OrderedDict
from functools import lru_cache
from json import JSONEncoder
from typing import Any, Callable, Dict, Generator, Generic, Tuple, TypeVar, Union

T = TypeVar("T")

OPERATOR_METHODS = {
    # only left & right binary operations can be supported by passing through
    # to the value. In place operations don't make sense on constants.
    "__add__",
    "__sub__",
    "__mul__",
    "__matmul__",
    "__truediv__",
    "__floordiv__",
    "__mod__",
    "__divmod__",
    "__pow__",
    "__lshift__",
    "__rshift__",
    "__and__",
    "__xor__",
    "__or__",
    "__radd__",
    "__rsub__",
    "__rmul__",
    "__rmatmul__",
    "__rtruediv__",
    "__rfloordiv__",
    "__rmod__",
    "__rdivmod__",
    "__rpow__",
    "__rlshift__",
    "__rrshift__",
    "__rand__",
    "__rxor__",
    "__ror__",
    "__le__",
    "__lt__",
    "__ge__",
    "__gt__",
}


def perform_on_constant(operation: Callable) -> Callable:
    """
    Modifies the given operation so that it can work with Constant values.
    If both operands to the operation are Constant the operation is performed
    only if they are of the same type. If either is a Constant, it's value is
    used instead.
    Example:
    The following would work:
        Tenor + timedelta
        Tenor + Tenor
    But not operations like
        Tenor + PaymentFrequency
    """

    def operate(self, other, *optional):
        if isinstance(self, Constant):
            if isinstance(other, Constant):
                if type(self) == type(other):
                    return operation(self.value, other.value, *optional)
            else:
                return operation(self.value, other, *optional)
        if isinstance(other, Constant):
            other = other.value
        return operation(self, other, *optional)

    return operate


class DuplicateConstantError(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.message = f"Multiple constants have the same value '{value}'"


class ImmutableMixin:
    _mutable = True

    def make_immutable(self):
        self._mutable = False

    def make_mutable(self):
        self._mutable = True

    def __setattr__(self, key: any, value: any) -> None:
        # allow changing private & protected variables as they are set from within
        if not (self._mutable or key.startswith("_")):
            raise AttributeError("Cannot change constant values.")
        super().__setattr__(key, value)


class Constant(Generic[T], ImmutableMixin):
    creation_counter = 0

    def __init__(self, value: T, label: str):
        super().__init__()
        self._creation_counter = Constant.creation_counter
        Constant.creation_counter += 1
        self.value = value
        self.label = label

    def __str__(self) -> str:
        return ", ".join(
            f"{key}={value}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )

    def __format__(self, format_spec):
        return f"{self.value:{format_spec}}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self} at {hex(id(self))}>"

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

    def __hash__(self) -> int:
        return hash(self.value)

    def to_json(self):
        return self.value


C = TypeVar("C", bound=Constant)


class Constants(Generic[C], ImmutableMixin):
    __instance = None

    def __init__(self):
        super().__init__()
        self.__value_to_object_mapping = None
        self.__label_to_object_mapping = None
        self.__object_set = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            fields = [
                getattr(cls, attr_name)
                for attr_name in dir(cls)
                if not attr_name.startswith("_")
                and isinstance(getattr(cls, attr_name), Constant)
            ]
            seen = set()
            for constant in fields:
                if constant in seen:
                    raise DuplicateConstantError(constant)
                seen.add(constant)

            cls._ordered_fields = OrderedDict(
                sorted(((f._creation_counter, f) for f in fields), key=lambda i: i[0])
            )
        return cls.__instance

    def __iter__(self) -> Generator[C, None, None]:
        for field in self._ordered_fields.values():
            yield field

    def __getitem__(self, item: Union[C, T]) -> C:
        return self._value_to_object_mapping[item]

    def __contains__(self, item: Union[C, T]) -> bool:
        return item in self._value_to_object_mapping

    def __len__(self) -> int:
        return len(self._value_to_object_mapping)

    def __setattr__(self, key: str, value: Any) -> None:
        if not key.startswith("_") and isinstance(value, Constant):
            counter = value._creation_counter
            if hasattr(self, key):
                counter = getattr(self, key)._creation_counter
            elif value in self:
                raise DuplicateConstantError(value)
            self._ordered_fields[counter] = value
        super().__setattr__(key, value)

    @lru_cache()
    def to_django_choices(self) -> Tuple[Tuple[T, str]]:
        return tuple((attr.value, attr.label) for attr in self)

    def get_value(self, label: str) -> T:
        return self.get_by_label(label).value

    def get_label(self, value: T) -> str:
        return self._value_to_object_mapping[value].label

    def get_by_label(self, label: str) -> C:
        return self._label_to_object_mapping[label]

    @property
    def _value_to_object_mapping(self) -> Dict[T, C]:
        if self.__value_to_object_mapping is None:
            self.__value_to_object_mapping = {attr.value: attr for attr in self}
        return self.__value_to_object_mapping

    @property
    def _label_to_object_mapping(self) -> Dict[str, C]:
        if self.__label_to_object_mapping is None:
            self.__label_to_object_mapping = {attr.label: attr for attr in self}
        return self.__label_to_object_mapping

    def make_mutable(self):
        super().make_mutable()
        for constant in self:
            constant.make_mutable()

    def make_immutable(self):
        super().make_immutable()
        for constant in self:
            constant.make_immutable()

    @lru_cache()
    def to_json(self):
        """
        Called when you do `json.dumps` with constants. The return value is
        cached as constants are immutable.

        If the constant is modified make sure to clear the lru cache.
        """
        return [o.to_json() for o in self]


def add_sorting_functions(
    constant_cls: type(Constant), constants_iterable: Constants
) -> None:
    def get_compare_value(other) -> Constant:
        try:
            return constants_iterable[other]
        except KeyError:
            raise TypeError(
                f"Cannot compare instances of '{constant_cls.__name__}' and '{type(other).__name__}'"
            )

    def __lt__(self, other):
        return self._creation_counter < get_compare_value(other)._creation_counter

    def __le__(self, other):
        return self._creation_counter <= get_compare_value(other)._creation_counter

    def __gt__(self, other):
        return self._creation_counter > get_compare_value(other)._creation_counter

    def __ge__(self, other):
        return self._creation_counter >= get_compare_value(other)._creation_counter

    constant_cls.__lt__ = __lt__
    constant_cls.__le__ = __le__
    constant_cls.__gt__ = __gt__
    constant_cls.__ge__ = __ge__


def encode_default(self, obj):
    if isinstance(obj, (Constant, Constants)):
        return obj.to_json()
    return encode_default.default(self, obj)


encode_default.default = JSONEncoder.default
JSONEncoder.default = encode_default
