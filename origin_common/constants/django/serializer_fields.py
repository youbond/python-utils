from rest_framework import serializers

from origin_common.constants.base import Constant, Constants


class ConstantChoiceMixin:
    """
    To be used with ChoiceField or MultipleChoiceField in serializers.
    Improves validation by returning a constant rather than builtin types like
    str or int.
    """

    def __init__(self, choices, filter_by=None, label_indexed=False, **kwargs):
        # ideally all this would have been done in `_set_choices` but since it
        # is protected, it can only be overridden in a child class and not a mixin.
        is_constants = isinstance(choices, Constants)
        if is_constants:
            if filter_by is None:
                filter_by = lambda x: True

            constant_choices = choices
            if label_indexed:
                # Tenors must be addressed not by value when the choice value is a
                # timedelta
                choices = [(c.label, c.label) for c in choices if filter_by(c)]
            else:
                # if not split, DRF duplicates the constant as both value and label
                choices = [(c.value, c.label) for c in choices if filter_by(c)]
        elif filter_by:
            raise TypeError("`filter_by` cannot be applied on non constant choices.")
        super().__init__(choices=choices, **kwargs)
        if is_constants:
            # remap so that it returns constants instead of the value
            if label_indexed:
                for key, value in self.choice_strings_to_values.items():
                    self.choice_strings_to_values[key] = constant_choices.get_by_label(
                        key
                    )
            else:
                for key, value in self.choice_strings_to_values.items():
                    self.choice_strings_to_values[key] = constant_choices[value]

    def to_internal_value(self, data):
        if isinstance(data, Constant):
            data = data.value
        if not isinstance(data, str) and hasattr(data, "__iter__"):
            data = [d.value if isinstance(d, Constant) else d for d in data]
        return super().to_internal_value(data)


class ChoiceField(ConstantChoiceMixin, serializers.ChoiceField):
    pass


class MultipleChoiceField(ConstantChoiceMixin, serializers.MultipleChoiceField):
    pass
