from collections import OrderedDict
from json import JSONEncoder
from typing import Any, Dict, Generator, Generic, Set, Tuple, TypeVar, Union

T = TypeVar("T")


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

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self} at {hex(id(self))}>"

    def __eq__(self, other):
        if type(self) == type(other):
            return hash(self) == hash(other)
        return self.value == other

    def __hash__(self) -> int:
        return hash(
            tuple(
                value for key, value in self.__dict__.items() if not key.startswith("_")
            )
        )

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

            cls._ordered_fields = OrderedDict(
                sorted(((f._creation_counter, f) for f in fields), key=lambda i: i[0])
            )
        return cls.__instance

    def __iter__(self) -> Generator[C, None, None]:
        for field in self._ordered_fields.values():
            yield field

    def __getitem__(self, item: Union[C, T]) -> C:
        if isinstance(item, Constant):
            if item in self:
                return item
            raise KeyError(item)
        return self._value_to_object_mapping[item]

    def __contains__(self, item: Union[C, T]) -> bool:
        if isinstance(item, Constant):
            return item in self._values
        return item in self._value_to_object_mapping

    def __len__(self) -> int:
        return len(self._values)

    def __setattr__(self, key: str, value: Any) -> None:
        # this will be replaced after init to prevent changing the constants
        if not key.startswith("_") and hasattr(value, "_creation_counter"):
            counter = value._creation_counter
            if hasattr(self, key):
                counter = getattr(self, key)._creation_counter
            self._ordered_fields[counter] = value
        super().__setattr__(key, value)

    def to_django_choices(self) -> Tuple[Tuple[T, str]]:
        return tuple((attr.value, attr.label) for attr in self)

    def get_value(self, label: str) -> T:
        return self.get_by_label(label).value

    def get_label(self, value: T) -> str:
        return self._value_to_object_mapping[value].label

    def get_by_label(self, label: str) -> C:
        return self._label_to_object_mapping[label]

    @property
    def _values(self) -> Set[C]:
        if self.__object_set is None:
            # quicker for lookups
            self.__object_set = set(self)
        return self.__object_set

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

    def to_json(self):
        return [o.to_json() for o in self]


def encode_default(self, obj):
    if isinstance(obj, (Constant, Constants)):
        return obj.to_json()
    return encode_default.default(self, obj)


encode_default.default = JSONEncoder.default
JSONEncoder.default = encode_default
