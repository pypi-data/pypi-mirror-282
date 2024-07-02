# setup.py
from setuptools import setup, find_packages

setup(
    name='examplemul',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[],  # List your dependencies here
    author='Nandhini',
    author_email='nandhini67288@gmail.com',
    description='A simple example library to perform multiplication',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nandhinikesavan20/hello_world',  # Update with your URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
