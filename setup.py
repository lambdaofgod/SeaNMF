from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='seanmf',
    version='0.1',
    description='',
    url='https://github.com/lambdaofgod/SeaNMF',
    packages=find_packages(),
    install_requires=requirements
)
