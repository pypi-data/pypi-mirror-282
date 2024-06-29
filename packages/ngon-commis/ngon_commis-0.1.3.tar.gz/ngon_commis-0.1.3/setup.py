from setuptools import setup, find_packages

setup(
    name='ngon-commis',
    package_name='commis',
    version='0.1.3',
    author='Silver',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "dataclasses",
        "numpy",
        "opencv-python",
        "pytest",
        "setuptools~=69.5.1",
    ],
)