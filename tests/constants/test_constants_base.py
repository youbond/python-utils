import json
import operator
from unittest import TestCase

from origin_common.constants.base import Constant, Constants, perform_on_constant


class TestConstant(TestCase):
    def test_str(self):
        const = Constant(value=123, label="Foo")
        expected_possibilities = {
            # python 3.5 doesn't maintain the order
            "value=123, label=Foo",
            "label=Foo, value=123",
        }
        assert str(const) in expected_possibilities

    def test_representation(self):
        const = Constant(value=123, label="Foo")
        assert repr(const) == f"<Constant: {const} at {hex(id(const))}>"

    def test_equality(self):
        const = Constant(value=123, label="Foo")
        assert const == const
        assert const == 123

    def test_can_be_made_immutable(self):
        const = Constant(value=123, label="Foo")
        const.make_immutable()
        with self.assertRaises(AttributeError):
            const.value = 321
        with self.assertRaises(AttributeError):
            const.label = "Bar"
        with self.assertRaises(AttributeError):
            const.new_attribute = "Baz"
        const.make_mutable()
        try:
            const.value = 321
            const.label = "Bar"
            const.new_attribute = "Baz"
        except AttributeError:
            self.fail("AttributeError raised while mutable.")

    def test_json_dumps(self):
        const = Constant(value=123, label="Foo")
        assert json.dumps(const) == json.dumps(const.value)


class TestConstants(TestCase):
    def test_is_singleton(self):
        class Dummy1(Constants):
            pass

        class Dummy2(Constants):
            pass

        constants1 = Dummy1()
        constants2 = Dummy1()
        assert constants1 is constants2
        constants3 = Dummy2()
        assert constants1 is not constants3

    def test_can_iterate_over_constants(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")
            c2 = Constant(2, "two")
            c3 = Constant(2, "two")
            c4 = Constant(2, "two")

        assert list(Dummy()) == [Dummy.c1, Dummy.c2, Dummy.c3, Dummy.c4]

    def test_can_check_if_value_is_in_constants(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        dummy = Dummy()
        assert 1 in dummy
        assert 2 not in dummy

    def test_can_check_if_constant_is_in_constants(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        c2 = Constant("other", "Other")
        dummy = Dummy()
        assert Dummy.c1 in dummy
        assert c2 not in dummy

    def test_can_get_constant_by_value(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")
            c2 = Constant("foo", "Foo bar")

        dummy = Dummy()
        assert dummy[1] is Dummy.c1
        assert dummy["foo"] is Dummy.c2
        with self.assertRaises(KeyError):
            assert dummy[2]

    def test_getting_constant_using_constant(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        c2 = Constant("foo", "Foo bar")

        dummy = Dummy()
        assert dummy[dummy.c1] is Dummy.c1
        with self.assertRaises(KeyError):
            assert dummy[c2]

    def test_get_label_from_value(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        dummy = Dummy()
        assert dummy.get_label(1) == "one"

    def test_get_value_from_label(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        dummy = Dummy()
        assert dummy.get_value("one") == 1

    def test_get_constant_from_label(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        dummy = Dummy()
        assert dummy.get_by_label("one") is dummy.c1

    def test_length(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")

        class Dummy2(Constants):
            c1 = Constant(1, "one")
            c2 = Constant(2, "two")
            c3 = Constant(3, "three")

        dummy1 = Dummy()
        dummy2 = Dummy2()
        assert len(dummy1) == 1
        assert len(dummy2) == 3

    def test_can_be_made_immutable(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")
            c2 = Constant(2, "two")
            c3 = Constant(3, "three")

        dummy = Dummy()
        dummy.make_immutable()
        with self.assertRaises(AttributeError):
            dummy.c1.value = 321
        with self.assertRaises(AttributeError):
            dummy.new_attribute = Constant(4, "four")
        dummy.make_mutable()
        try:
            dummy.c1.value = 321
            dummy.new_attribute = Constant(4, "four")
        except AttributeError:
            self.fail("AttributeError raised while mutable.")

    def test_json_dumps(self):
        class Dummy(Constants):
            c1 = Constant(1, "one")
            c2 = Constant(2, "two")
            c3 = Constant(3, "three")

        dummy = Dummy()
        assert json.dumps(dummy) == json.dumps([c.value for c in dummy])


class TestPerformOnConstant(TestCase):
    def test_if_both_operands_are_constants_it_uses_value_of_both(self):
        c1 = Constant(1, "one")
        c2 = Constant(2, "two")
        operation = perform_on_constant(operator.add)
        assert operation(c1, c2) == 3

    def test_if_right_operand_is_not_a_constant_it_uses_it_directly(self):
        c1 = Constant(1, "one")
        operation = perform_on_constant(operator.add)
        assert operation(c1, 2) == 3

    def test_if_left_operand_is_not_a_constant_it_uses_it_directly(self):
        c1 = Constant(1, "one")
        operation = perform_on_constant(operator.add)
        assert operation(2, c1) == 3

    def test_if_right_operand_is_a_different_type_of_constant_it_uses_it_directly(self):
        class T1(Constant):
            pass

        class T2(Constant):
            pass

        c1 = T1(1, "one")
        c2 = T2(2, "Two")
        # even though values are of the same type, since they are different constants
        # they cannot be compared.
        operation = perform_on_constant(operator.add)
        with self.assertRaises(TypeError):
            assert operation(c1, c2)

    def test_optional_arguments_can_be_provided(self):
        c1 = Constant(3, "foo")
        operation = perform_on_constant(pow)
        assert operation(c1, 3, 4) == 3
