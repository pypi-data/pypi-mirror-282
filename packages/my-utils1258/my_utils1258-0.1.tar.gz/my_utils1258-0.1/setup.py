from setuptools import setup, find_packages

setup(
    name='my_utils1258',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        # e.g., 'numpy', 'requests',
    ],
    author='Shamim Khan',
    author_email='shamimkdev@gmail.com',
    description='This package provides methods to get the data in sql input formats',
    url='https://github.com/shamimkdev/my_utils1258',  # Project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
