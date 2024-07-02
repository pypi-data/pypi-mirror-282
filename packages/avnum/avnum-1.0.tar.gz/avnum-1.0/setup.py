from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="avnum",
    version="1.0",
    author="Andrei Motin",
    author_email="motinandrei@icloud.com",
    description="A simple module to calculate the average of numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreimotin/avnum",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)