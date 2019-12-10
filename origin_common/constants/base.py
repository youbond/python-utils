from collections import OrderedDict
from typing import Dict, Generator, Generic, Set, Tuple, TypeVar, Union

T = TypeVar("T")


class Constant(Generic[T]):
    creation_counter = 0

    def __init__(self, value: T, label: str):
        super().__init__()
        self._creation_counter = Constant.creation_counter
        Constant.creation_counter += 1
        self.value = value
        self.label = label

    def __str__(self) -> str:
        return ", ".join(
            "{}={}".format(key, value)
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )

    def __repr__(self):
        return "<{}: {} at {}>".format(
            self.__class__.__name__, str(self), hex(id(self))
        )

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


C = TypeVar("C", bound=Constant)


class Constants(Generic[C]):
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

    def __len__(self):
        return len(self._values)

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
