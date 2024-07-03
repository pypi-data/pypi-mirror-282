# setup.py
from setuptools import setup, find_packages

setup(
    name='meta-pkg',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'meta-pkg-cli = meta_pkg.metadata:main',
        ],
    },
    test_suite='tests',
    python_requires='>=3.6',
    author='Benjamin Mark',
    description='A Python package for metadata operations.',
    url='https://github.com/bzm10/meta-pkg',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
