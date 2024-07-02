from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='tsassure_feature',
    version='0.7',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl',
        # Add any additional dependencies here
    ],
    entry_points={
        'console_scripts': [
            'tsassure=tsassure_feature.main:main',
        ],
    },
    keywords='feature time-series feature_extraction',

    long_description=description,
    long_description_content_type="text/markdown",
)