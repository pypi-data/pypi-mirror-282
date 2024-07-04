from setuptools import setup, find_packages

setup(
    name='modelslab',
    version='0.2',
    description='A package for interacting with the ModelsLab API',
    author='Adhik Joshi',
    author_email='support@modelslab.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)