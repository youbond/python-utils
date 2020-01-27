from unittest import TestCase

from rest_framework import serializers

from origin_common.constants.base import Constant, Constants
from origin_common.constants.django.serializer_fields import (
    ChoiceField,
    MultipleChoiceField,
)


class DummyChoices(Constants):
    c1 = Constant(1, "foo")
    c2 = Constant(2, "bar")
    c3 = Constant(3, "baz")


class TestChoiceField(TestCase):
    def test_returns_constant_during_validation(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = ChoiceField(choices=dummy_choices)

        serializer = Serializer(data={"foo": 1})
        assert serializer.is_valid()
        assert serializer.validated_data["foo"] is dummy_choices.c1

    def test_returns_constant_in_representation(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = ChoiceField(choices=dummy_choices)

        serializer = Serializer(instance={"foo": 1})
        assert serializer.data["foo"] is dummy_choices.c1

    def test_validation_still_works_normally_for_non_constant_choices(self):
        class Serializer(serializers.Serializer):
            foo = ChoiceField(choices={1: "One"})

        serializer = Serializer(data={"foo": 1})
        assert serializer.is_valid()
        assert serializer.validated_data["foo"] == 1

    def test_text_input_also_works_for_validation(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = ChoiceField(choices=dummy_choices)

        serializer = Serializer(data={"foo": "1"})
        assert serializer.is_valid()
        assert serializer.validated_data["foo"] is dummy_choices.c1

    def test_instance_can_be_an_actual_constant(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = ChoiceField(choices=dummy_choices)

        serializer = Serializer(instance={"foo": dummy_choices.c1})
        assert serializer.data["foo"] is dummy_choices.c1


class TestMultipleChoiceField(TestCase):
    def test_returns_constant_during_validation(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = MultipleChoiceField(choices=dummy_choices)

        serializer = Serializer(data={"foo": [1, 2]})
        assert serializer.is_valid()
        assert serializer.validated_data["foo"] == {dummy_choices.c1, dummy_choices.c2}

    def test_returns_constant_in_representation(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = MultipleChoiceField(choices=dummy_choices)

        serializer = Serializer(instance={"foo": [1]})
        assert serializer.data["foo"] == {dummy_choices.c1}

    def test_validation_still_works_normally_for_non_constant_choices(self):
        class Serializer(serializers.Serializer):
            foo = MultipleChoiceField(choices={1: "One"})

        serializer = Serializer(data={"foo": [1]})
        assert serializer.is_valid()
        assert serializer.validated_data["foo"] == {1}

    def test_text_input_also_works_for_validation(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = MultipleChoiceField(choices=dummy_choices)

        serializer = Serializer(data={"foo": ["1"]})
        assert serializer.is_valid()
        assert serializer.validated_data["foo"] == {dummy_choices.c1}

    def test_instance_can_be_an_actual_constant(self):
        dummy_choices = DummyChoices()

        class Serializer(serializers.Serializer):
            foo = MultipleChoiceField(choices=dummy_choices)

        serializer = Serializer(instance={"foo": [dummy_choices.c1]})
        assert serializer.data["foo"] == {dummy_choices.c1}
