from setuptools import setup, find_packages

setup(
    name='ngon-commis',
    package_name='commis',
    version='0.1.2',
    author='Silver',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "dataclasses",
        "numpy",
        "python-opencv",
        "pytest",
        "setuptools~=69.5.1",
    ],
)