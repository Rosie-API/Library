from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rosieapi',
    version='2.0.0',
    author='Rosie-API',
    author_email='contact@error44.tech',
    license='MIT',
    description='The Rosie API from Error44 as python package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "aiohttp >= 3.6"
    ],
    url='https://github.com/Rosie-API/Library',
    py_modules=['rosieapi'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
