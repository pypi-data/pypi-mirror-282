from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ngon-commis',
    package_name='commis',
    version='0.1',
    author='Silver',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=required,
)