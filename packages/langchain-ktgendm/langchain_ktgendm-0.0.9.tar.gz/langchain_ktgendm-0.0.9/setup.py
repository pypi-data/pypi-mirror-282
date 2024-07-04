# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("./langchain_ktgendm/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='langchain_ktgendm',
    version='0.0.9',
    description='langchain_ktgendm',
    author='langchain_ktgendm',
    author_email='',
    long_description=long_description,
    python_requires='>=3.8',
    long_description_content_type="text/markdown",
    packages= find_packages(exclude = ['docs', 'tests*','__pycache__/', 'excluded_files','dist']),
    package_data={
        'langchain_ktgendm': ['*.py','LICENSE','README.md'],  # include all Python files in langchain_ktgendm package
    },
)