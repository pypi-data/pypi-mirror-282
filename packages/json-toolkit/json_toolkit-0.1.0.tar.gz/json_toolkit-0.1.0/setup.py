from setuptools import setup, find_packages

setup(
    name='json_toolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    author='o_frun',
    description='A simple library for JSON manipulation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/S1lentAFK/json_toolkit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
