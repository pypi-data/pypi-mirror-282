from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

description = """
PyDocMark is a Python documentation generator that:

- Automatically creates Markdown documentation from Python source code
- Analyzes the Abstract Syntax Tree (AST) to extract docstrings, function signatures, and class structures
- Generates comprehensive, well-formatted documentation for modules, classes, and functions
- Supports optional inclusion of source code in the documentation
- Utilizes parallel processing for efficient handling of large projects
- Provides flexible logging options and colored console output for better user experience
"""


setup(
    name="mdpydoc",
    version="0.2.1",
    # author="Your Name",
    author_email="package@dynovant.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/dynovant/mdpydoc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "mdpydoc=mdpydoc.cli:main",
        ],
    },
)