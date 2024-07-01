# setup.py

from setuptools import setup, find_packages

setup(
    name='sine_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    extras_require={
        'dev': [
            'matplotlib',
            'unittest',
        ],
    },
    author='K ABHISHEK MENON',
    author_email='kabhishekmenon@gmail.com',
    description='A library to generate sinusoidal waveforms with a DC offset.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    #url='https://github.com/yourusername/sine_generator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
