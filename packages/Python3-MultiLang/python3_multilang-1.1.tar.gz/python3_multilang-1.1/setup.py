from setuptools import setup, find_packages

setup(
    name='Python3-MultiLang',
    version='1.1',
    packages=find_packages(),

    author='DDavid701',
    author_email='ddavid701@gmail.com',
    description='ML is a Library for Multi Language support in Python.',
    url='https://github.com/DDavid701/python_multilang',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
)