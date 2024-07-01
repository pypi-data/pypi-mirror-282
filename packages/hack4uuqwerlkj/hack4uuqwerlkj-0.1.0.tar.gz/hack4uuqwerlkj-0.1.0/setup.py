from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hack4uuqwerlkj",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="trovo",
    description="Una bibliotreca para consultar cursos de hack4u.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io",
)

