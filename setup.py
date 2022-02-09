from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
        name='LaTeXDatax',
        version='1.3',
        author='David Gustavsson',
        author_email='david.e.gustavsson@gmail.com',
        description='Export individual data from a Python script to a LaTeX document',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/Datax-package/LaTeXDatax.py',
        packages=find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            ],
        python_requires='>=3.6',
        )


