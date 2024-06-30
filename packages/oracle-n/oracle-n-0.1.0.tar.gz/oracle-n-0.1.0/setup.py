from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='oracle-n',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'transformers',
        'datasets',
        'apache-beam',
        'pandas',
        'scikit-learn',
    ],
    description='A custom model for sentiment analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hilal Agil',
    author_email='hilal@tenzro.com',
    url='https://github.com/hilarl/oracle-n',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
