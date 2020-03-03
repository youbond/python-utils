from functools import lru_cache
from unittest import TestCase

from origin_common.better_test_mixins import LruCacheTestMixin, SerializerTestMixin


class Field:
    pass


class TestSerializerTestMixin(TestCase):
    class Serializer:
        fields = {"field": Field()}

    class OtherObject:
        field = Field()

    class NoFieldObject:
        pass

    def test_serializer_is_initialized_correctly(self):
        class DummyTestCase1(SerializerTestMixin, TestCase):
            pass

        class DummyTestCase2(SerializerTestMixin, TestCase):
            def setUp(inner_self):
                inner_self.serializer = self.OtherObject()

        class DummyTestCase3(SerializerTestMixin, TestCase):
            def setUp(inner_self):
                inner_self.serializer = self.NoFieldObject()

        dummy_test_case1 = DummyTestCase1()
        dummy_test_case1.setUp()
        msg = f"'{None}' does not have any fields to test."
        with self.assertRaises(AssertionError, msg=msg):
            dummy_test_case1.test_all_fields_are_tested()

        dummy_test_case2 = DummyTestCase2()
        dummy_test_case2.setUp()
        msg = f"'{dummy_test_case2.serializer}' does not have any fields to test."
        with self.assertRaises(AssertionError, msg=msg):
            dummy_test_case2.test_all_fields_are_tested()

        dummy_test_case3 = DummyTestCase3()
        dummy_test_case3.setUp()
        msg = f"'{dummy_test_case3.serializer}' does not have any fields to test."
        with self.assertRaises(AssertionError, msg=msg):
            dummy_test_case3.test_all_fields_are_tested()

    def test_throws_error_if_any_field_is_not_tested(self):
        class Dummy(SerializerTestMixin, TestCase):
            def setUp(inner_self):
                inner_self.serializer = self.Serializer()

        dummy = Dummy()
        dummy.setUp()
        with self.assertRaises(
            AssertionError, msg="Tests are missing for the following fields: field."
        ):
            dummy.test_all_fields_are_tested()

    def test_no_errors_if_all_fields_are_tested(self):
        class Dummy(SerializerTestMixin, TestCase):
            def setUp(inner_self):
                inner_self.serializer = self.Serializer()

            def test_field_field(self):
                assert True

        dummy = Dummy()
        dummy.setUp()
        dummy.test_all_fields_are_tested()
        # see ma... no errors
        dummy.test_field_field()


class TestLruCacheTestMixin(LruCacheTestMixin, TestCase):
    def test_no_error_if_decorated(self):
        @lru_cache()
        def func():
            pass

        self.assert_has_lru_cache(func)

    def test_throws_error_if_not_decorated(self):
        def func():
            pass

        with self.assertRaises(AssertionError):
            self.assert_has_lru_cache(func)
