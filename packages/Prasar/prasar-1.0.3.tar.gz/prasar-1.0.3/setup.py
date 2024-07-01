from setuptools import setup, find_packages
import io

with io.open('readme.md', "r") as f:
    long_description = f.read()


setup(
    name="Prasar",
    version="1.0.3",
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