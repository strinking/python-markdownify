#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(filepath):
    with open(filepath) as f:
        return f.read()


setup(
    name='markdownify',
    description='Convert HTML to markdown.',
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.rst')),
    version="0.4.0",
    author="Matthew Tretter",
    author_email='m@tthewwithanm.com',
    url='http://github.com/matthewwithanm/python-markdownify',
    download_url='http://github.com/matthewwithanm/python-markdownify/tarball/master',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    setup_requires=[
        'flake8',
    ],
    tests_require=[
        'pytest',
    ],
    install_requires=[
        'beautifulsoup4',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
