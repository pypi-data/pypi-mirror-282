# setup.py

from setuptools import setup, find_packages

setup(
    name="delta_logger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic",
    ],
    author="Yu-Cheng Huang",
    author_email="ychuang2@bu.edu",
    description="A Python library for logging messages to JSON files with rotation and validation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YCHuang2112sub/dict_delta_logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
