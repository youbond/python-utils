from setuptools import setup, find_packages

setup(
    name="origin_common",
    version="0.0.3",
    description="Common util functions and mixins to make development "
    "of other projects easier.",
    url="https://git.originmarkets.com/originmarkets/origin-common",
    # packages=find_packages(exclude=["*.tests*"]),
    packages=["origin_common", "origin_common.constants"],
    zip_safe=True,
    tests_require=["tox"],
    python_requires=">=3.5",
)
