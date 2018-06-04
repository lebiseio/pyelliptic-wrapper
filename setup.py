import os

from setuptools import setup, find_packages

__VERSION__ = '0.0.1'

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'pyelliptic',
    'pytest',
]

setup(
    name='pyelliptic-wrapper',
    version=__VERSION__,
    description='Python Elliptic Cryptography Wrapper for OpenSSL',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: Cryptography",
    ],
    author='lebiseio',
    author_email='lebiseio@gmail.com',
    url='https://github.com/lebiseio/pyelliptic-wrapper.git',
    keywords='cryptography elliptic',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='pyelliptic-wrapper',
    install_requires=requires,
)
