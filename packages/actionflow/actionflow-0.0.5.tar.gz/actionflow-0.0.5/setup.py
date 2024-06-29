# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages

# Avoids IDE errors, but actual version is read from version.py
__version__ = ""
exec(open('actionflow/version.py').read())

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='actionflow',
    version=__version__,
    description='LLM agent workflows',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/actionflow',
    license="Apache License 2.0",
    zip_safe=False,
    python_requires=">=3.8.0",
    entry_points={"console_scripts": ["actionflow = actionflow.cli:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords='actionflow,Agent Tool,action,agent',
    install_requires=[
        "loguru",
        "beautifulsoup4",
        "fire",
        "openai",
        "python-dotenv",
        "sqlalchemy",
        "pydantic",
    ],
    packages=find_packages(),
)
