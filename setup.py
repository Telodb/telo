from setuptools import setup, find_packages

setup(
    name='telo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'hues',
    ],
    entry_points={
        'console_scripts': [
            'telo = telo.telo:main',
        ]
    }
)
