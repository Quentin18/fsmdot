"""
* Install with pip (recommended):
    pip3 install .
* Install with setuptools:
    python3 setup.py install
"""
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fsmdot',
    version='0.0.1',
    description="""
    Implementation of finite-state machines and exportation to dot format""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quentin Deschamps',
    author_email='quentindeschamps18@gmail.com',
    url='https://github.com/Quentin18/fsmdot',
    packages=['fsmdot'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Education',
        'Topic :: Scientific/Engineering'
    ],
    license='MIT',
    keywords='fsm automata dfa nfa',
    project_urls={
        'Travis':
        'https://travis-ci.org/github/Quentin18/fsmdot/',
        'Source Code': 'https://github.com/Quentin18/fsmdot/',
    },
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['pygraphviz', 'tabulate'],
    python_requires='>=3.6',
)
