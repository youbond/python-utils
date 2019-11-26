import collections
from typing import Dict, Generator, Set, Any, Tuple, Union


class Constant:
    def __init__(self, value: Any, label: str):
        super().__init__()
        self.value = value
        self.label = label

    def __str__(self) -> str:
        return "value={}, label={}".format(self.value, self.label)

    def __repr__(self):
        return "<{}: {} at {}>".format(
            self.__class__.__name__, str(self), hex(id(self))
        )


class OrderedClassMembers(type):
    @classmethod
    def __prepare__(self, name, bases):
        return collections.OrderedDict()

    def __new__(mcs, name, bases, classdict):
        classdict["__ordered__"] = [
            key for key in classdict.keys() if key not in ("__module__", "__qualname__")
        ]
        return type.__new__(mcs, name, bases, classdict)


class Constants(metaclass=OrderedClassMembers):
    __instance = None

    def __init__(self):
        super().__init__()
        self.__value_to_object_mapping = None
        self.__label_to_object_mapping = None
        self.__object_set = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __iter__(self) -> Generator[Constant, None, None]:
        for attr_name in self.__ordered__:
            yield getattr(self, attr_name)
        # for attr_name in dir(self):
        #     if attr_name.startswith("_"):
        #         continue
        #     if isinstance(getattr(self, attr_name), Constant):
        #         yield getattr(self, attr_name)

    def __getitem__(self, item: Union[Constant, Any]) -> Constant:
        if isinstance(item, Constant):
            if item in self:
                return item
            raise KeyError(item)
        return self._value_to_object_mapping[item]

    def __contains__(self, item: Union[Constant, Any]) -> bool:
        if isinstance(item, Constant):
            return item in self._values
        return item in self._value_to_object_mapping

    def to_django_choices(self) -> Tuple[Tuple[Any, str]]:
        return tuple((attr.value, attr.label) for attr in self)

    def get_value(self, label: str) -> Any:
        return self._label_to_object_mapping[label].value

    def get_label(self, value: Any) -> str:
        return self._value_to_object_mapping[value].label

    @property
    def _values(self) -> Set[Constant]:
        if self.__object_set is None:
            self.__object_set = {
                attr
                for attr_name, attr in vars(self.__class__).items()
                if isinstance(attr, Constant)
            }
        return self.__object_set

    @property
    def _value_to_object_mapping(self) -> Dict[Any, Constant]:
        if self.__value_to_object_mapping is None:
            self.__value_to_object_mapping = {attr.value: attr for attr in self}
        return self.__value_to_object_mapping

    @property
    def _label_to_object_mapping(self) -> Dict[str, Constant]:
        if self.__label_to_object_mapping is None:
            self.__label_to_object_mapping = {attr.label: attr for attr in self}
        return self.__label_to_object_mapping
