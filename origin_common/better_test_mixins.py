class SerializerTestMixin:
    """
    Use this to test serializer. All it does is assert each field has
    a test for it.
    Each field test should have the name `test_<field_name>_test`.
    """

    serializer = None

    def setUp(self):
        # initialize serializer here
        pass

    def test_all_fields_are_tested(self):
        assertion_message = f"'{self.serializer}' does not have any fields to test."
        assert hasattr(self.serializer, "fields") and hasattr(
            self.serializer.fields, "items"
        ), assertion_message
        missing_tests = []
        for field_name in self.serializer.fields.keys():
            if not hasattr(self, f"test_{field_name}_field"):
                missing_tests.append(field_name)
        assert (
            not missing_tests
        ), f"Tests are missing for the following fields: {', '.join(missing_tests)}."
