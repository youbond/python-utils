from rest_framework import serializers

from origin_common.constants.base import Constants


class ConstantChoiceMixin:
    """
    To be used with ChoiceField or MultipleChoiceField in serializers.
    Improves validation by returning a constant rather than builtin types like
    str or int.
    """

    def __init__(self, choices, filter_by=None, **kwargs):
        # ideally all this would have been done in `_set_choices` but since it
        # is protected, it can only be overridden in a child class and not a mixin.
        is_constants = isinstance(choices, Constants)
        if is_constants:
            if filter_by is None:
                filter_by = lambda x: True
            # if not split, DRF duplicates the constant as both value and label
            constant_choices = choices
            choices = [(c.value, c.label) for c in choices if filter_by(c)]
        elif filter_by:
            raise TypeError("`filter_by` cannot be applied on non constant choices.")
        super().__init__(choices=choices, **kwargs)
        if is_constants:
            # remap so that it returns constants instead of the value
            for key, value in self.choice_strings_to_values.items():
                self.choice_strings_to_values[key] = constant_choices[value]


class ChoiceField(ConstantChoiceMixin, serializers.ChoiceField):
    pass


class MultipleChoiceField(ConstantChoiceMixin, serializers.MultipleChoiceField):
    pass
