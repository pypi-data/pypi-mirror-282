from setuptools import setup, find_packages

setup(
    name='oracle-n',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'transformers',
        'datasets',
    ],
    description='A model for sentiment analysis',
    author='Hilal Agil',
    author_email='hilal@tenzro.com',
    url='https://github.com/hilarl/oracle-n',
)
