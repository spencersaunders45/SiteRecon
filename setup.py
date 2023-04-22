from setuptools import setup, find_packages

setup(
    name='siterecon',
    version='0.1.0',
    description='A tool for website reconnaissance',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'rich'
    ]
)