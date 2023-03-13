from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qrbsgen',
    packages=['qrbsgen'],  # this must be the same as the name above
    version='0.0.1',
    description='A simple Python library for encoding Quantum Rule Based Systems',
    author='Kate Marshall',
    author_email='kate.marshall@ibm.com',
    # use the URL to the github repo
    url='https://github.com/kvcmarshall/qrbsgen',
    keywords=['quantum computing', 'quantum rule based systems', 'rule based systems',
              'expert systems', 'qiskit', 'python'],  # arbitrary keywords
    license='LICENSE.txt',
    install_requires=[
        "qiskit >= 0.36.0",
    ],
    classifiers=['Programming Language :: Python :: 3.7'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
