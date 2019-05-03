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
        assertion_message = "'{serializer}' does not have any fields to test.".format(serializer=self.serializer)
        assert hasattr(self.serializer, "fields") and hasattr(self.serializer.fields, "items"), assertion_message
        missing_tests = []
        for field_name in self.serializer.fields.keys():
            if not hasattr(self, "test_{}_field".format(field_name)):
                missing_tests.append(field_name)
        assert not missing_tests, "Tests are missing for the following fields: {}.".format(", ".join(missing_tests))
