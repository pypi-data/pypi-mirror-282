from setuptools import setup, find_packages

setup(
    name="test_package_barraul",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'my_script=test_package_barraul.module:main',
        ],
    },
)