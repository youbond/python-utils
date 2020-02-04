# Origin Common Code
### [![pipeline status](https://git.originmarkets.com:48201/originmarkets/common/badges/master/pipeline.svg)](https://git.originmarkets.com:48201/originmarkets/common/commits/master) [![coverage report](https://git.originmarkets.com:48201/originmarkets/common/badges/master/coverage.svg)](https://git.originmarkets.com:48201/originmarkets/common/commits/master)

This module is a collection of util functions and mixins to make development of other projects easier.


### Installation
This module can be included in the requirements.txt file by adding
```text
git+ssh://git@git.originmarkets.com/originmarkets/origin-common.git#egg=origin_common
```
Alternatively you could just do
```shell script
pip install git+ssh://git@git.originmarkets.com/originmarkets/origin-common.git#egg=origin_common
```
In order to use the model fields, [Django][django] is needed.               
In order to use the serializer fields, [Django REST framework][drf] is needed.
Both are available as optional installations while installing this module.

```shell script
// installs Django
pip install "origin_common[django] @ git+ssh://git@git.originmarkets.com/originmarkets/origin-common.git"
// installs Django & rest framework
pip install "origin_common[djangorest] @ git+ssh://git@git.originmarkets.com/originmarkets/origin-common.git"
```


### Constants
Constants are immutable objects with value & label.          
Some constants might have other properties.                
For example: FundingBasis constants have some related PaymentFrequency, Currency & DayCount.
In order to use the constants just import them.
```python
from origin_common.constants import (
    ADJUSTMENTS,
    BUSINESS_DAY_CONVENTIONS,
    DAY_COUNTS,
    FUNDING_BASES,
    PAYMENT_FREQUENCIES,
    TENORS,
)

ADJUSTMENTS.ADJUSTED.value
FUNDING_BASES.EUR_3M.payment_frequency
```
Look into each type of constant to see what attributes are available on it.
In order to use it with django models you can import the model fields
```python
from django.db import models
from origin_common.constants.django import model_fields

class MyModel(models.Model):
    funding_basis = model_fields.FundingBasisField()
    payment_frequency = model_fields.PaymentFrequencyField()
```
In order to save something to db, you could provide the field with the appropriate 
constant instance or it's value.
For example for the above model you could do
```python
my_model = MyModel(funding_basis=FUNDING_BASES.EUR_3M, payment_frequency=3)
```
When you read from the db, the model instance will have the appropriate constant instance.
```python
isinstance(my_model.payment_frequency, PaymentFrequency)  # True
```

In order to be used with DRF the ChoiceField & MutlipleChoiceFields have been overridden.
```python
from rest_framework import serializers
from origin_common.constants.django import serializer_fields

class MySerializer(serializers.Serializer):
    basis = serializer_fields.ChoiceField(FUNDING_BASES, filter_by=lambda b: b.is_fixed_basis)
    currencies = serializer_fields.MultipleChoiceField(CURRENCIES)
```
Rather than passing in a subset of constant choices, pass in a function to filter the choices.
If non constant choices are provided, the field is behave like it normally does.

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


[django]: https://www.djangoproject.com/ "Django"
[drf]: https://www.django-rest-framework.org/ "Django REST framework"
