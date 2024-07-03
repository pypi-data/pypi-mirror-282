from setuptools import setup, find_packages

setup(
    name='hash_code_separator',
    version='0.5',
    packages=find_packages(),
    install_requires=[
        'halo',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'hash = code_separator.cli:main',
            # Define other CLI commands here if needed
        ],
    },
    author='Bryan Antoine',
    author_email='b.antoine.se@gmail.com',
    description='Python package for inserting hash separators between functions and classes.',
    long_description='Python package for inserting hash separators between functions and classes in Python files.',
    url='https://github.com/bantoinese83/Code_separator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
