from setuptools import setup

setup(
    name='includexls',
    version='0.0.1',
    author='Nico Hoffmann',
    author_email='n-includexls@maxdoom.com',
    packages=['includexls',],
    url='https://github.com/maxdoom-com/includexls/',
    license='LICENSE.md',
    description='A markdown extension to include xls files from markdown files (pagewise).',
    long_description=open('README.md').read(),
    install_requires=[
        'markdown',
        'xlrd',
    ],
)
