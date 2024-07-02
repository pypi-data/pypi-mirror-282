"""
**Short description of this Python module**

Longer description of this module.

"""

__author__ = "Maxim Ustin"
__authors__ = ["Maxim Ustin"]
__contact__ = "mxustin@gmail.com"
__copyright__ = "Copyright © 2024, Maxim Ustin"
__credits__ = ["Maxim Ustin"]
__date__ = "2024"
__deprecated__ = False
__email__ =  "mxustin@gmail.com"
__license__ = "MIT License"
__maintainer__ = "Maxim Ustin"
__status__ = "Beta"
__version__ = "0.0.1"


from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='aval',
    version='0.0b1',
    author='Maxim Ustin',
    author_email='mxustin@gmail.com',
    description='AVal is a class capable of applying a list of validation '
                'strategies and an exception handler to an object to be '
                'validated. It can be used by calling the validation method '
                'as well as a decorator',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/hmxustin/aval',
    download_url='https://github.com/hmxustin/aval/archive/refs/heads/main.zip',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13"
    ],
    keywords='validator, validation, data validation, abstract validator, '
             'validation strategy, validation method, validation decorator',
    project_urls={
        'GitHub': 'https://github.com/hmxustin/aval',
        'ZIP': 'https://github.com/hmxustin/aval/archive/refs/heads/main.zip',
        'Manual (RU)': 'https://docs.mxustin.ru/micro/validator/manual/intro'
    },
    python_requires='>=3.6'
)
