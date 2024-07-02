from setuptools import setup, find_packages

setup(
    name='calculator_sdk',
    version='0.1.3',
    description='A simple calculator SDK',
    packages=find_packages(),
    install_requires=[
        'py4j',
    ],
)