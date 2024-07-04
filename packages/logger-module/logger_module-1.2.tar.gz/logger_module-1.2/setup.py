from setuptools import setup
from logger_module import __version__

setup(
    name='logger_module',
    version=__version__,
    description='A module for logging status messages',
    url='https://github.com/Byron0x7D2/logger-module',
    author='Byron Anemogiannis',
    author_email='bgane@di.uoa.gr',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    py_modules=['logger_module'],
)
