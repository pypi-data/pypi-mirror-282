from setuptools import setup, find_packages
import io

try:
    with open('readme.md', 'r', encoding='utf-8') as file:
        long_description = file.read()
except UnicodeDecodeError:
    import chardet
    
    with open('readme.md', 'rb') as file:
        raw_data = file.read()
        detected = chardet.detect(raw_data)
        encoding = detected['encoding']
    
    # Try to open the file again with the detected encoding
    with open('readme.md', 'r', encoding=encoding) as file:
        long_description = file.read()


setup(
    name="Prasar",
    version="1.2.1",
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