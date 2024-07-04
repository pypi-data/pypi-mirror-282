from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ID3classifier",
    version="0.1.0",
    description="A simple ID3 decision tree implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dingwalnitin/id3",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
    ],
)