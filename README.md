# Origin Common Code
### [![pipeline status](https://git.originmarkets.com:48201/originmarkets/common/badges/master/pipeline.svg)](https://git.originmarkets.com:48201/originmarkets/common/commits/master) [![coverage report](https://git.originmarkets.com:48201/originmarkets/common/badges/master/coverage.svg)](https://git.originmarkets.com:48201/originmarkets/common/commits/master)

This module is a collection of util functions and mixins to make development of other projects easier.


### Installation
This module can be included in the requirements.txt file by adding
```text
-e https://git.originmarkets.com:48201/originmarkets/common.git#egg=origin_common
```
Alternatively you could just do
```
pip install https://git.originmarkets.com:48201/originmarkets/common.git
```


### Util functions
##### join_list
`from origin_common.utils import join_list`                 
Takes a list `["a", "b", "c"]` and returns a string `"a, b & c"`.
##### string_to_timedelta
`from origin_common.utils import string_to_timedelta`                 
Takes a string `"1Y"` and returns a `timedelta(days=365.25)`.
##### timedelta_to_string
`from origin_common.utils import timedelta_to_string`                 
Inverse of `string_to_timedelta`. Takes a timedelta and returns a string.






### Mixins
##### SerializerTestMixin
`from origin_common.better_test_mixins import SerializerTestMixin`       
A very useful mixing to use as a base for all your serializers tests. 
It will ensure that all the fields of your serializer are tested.
Example:
```python
class FooSerializer(serializers.Serialzer):
    class Meta:
        model = Foo
        fields = ("foo", "bar", "baz")
        

class TestFooSerializer(SerializerTestMixin, TestCase):
    def setUp(self):
        self.serializer = FooSerializer()
        
    def test_bar(self):
        assert True
```
```
test
E       AssertionError: Tests are missing for the following fields: foo, baz
```
