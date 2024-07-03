from setuptools import setup, find_packages
from os import path
working_directory= path.abspath(path.dirname(__file__))

with open(path.join(working_directory,'README.md'),encoding='utf-8') as f :
    long_description= f.read()
setup(
    name='authentication_microservices_webelight',
    version='0.0.1',
    author='Keyur Parmar',
    author_email='keyurp@webelight.co.in',
    description='Authentication Microservices',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
)