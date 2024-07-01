from setuptools import setup, find_packages
import io

try:
    with io.open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except UnicodeDecodeError:
    with io.open('README.md', encoding='latin-1') as f:
        long_description = f.read()

setup(
    name="Prasar",
    version="1.0.0",
    author="Abhishek Mishra",
    author_email="mishraabhishek.2899@gmail.com",
    description="A robust event handling framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mishrababhishek/prasar",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'colorama',
    ],
)