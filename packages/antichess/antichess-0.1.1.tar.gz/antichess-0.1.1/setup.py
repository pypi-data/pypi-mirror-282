from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent
long_description = (here / "README.txt").read_text()

setup(
    name='antichess',
    version='0.1.1',
    description='Package for simulating and playing antichess games.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Divit Rawal',
    author_email='divit.rawal+antichess@gmail.com',
    url='https://github.com/divitr/antichess',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    python_requires='>=3.6',
)

