from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='paraormal_stories_scrapper',
    version='0.1',
    description='Story Scraper',
    author='Andrija Jovanovic',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements
)
