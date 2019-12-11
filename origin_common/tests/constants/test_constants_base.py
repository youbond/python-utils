from unittest import TestCase

from origin_common.constants.base import Constant, Constants


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
        assert repr(const) == "<Constant: {} at {}>".format(const, hex(id(const)))

    def test_equality(self):
        const = Constant(value=123, label="Foo")
        assert const == const
        assert const == 123


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
