from setuptools import setup, find_packages

setup(
    name='gitvoyager',
    version='2.2.0',  # Update the version number
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'voyager=gitvoyager.main:main',
            'vgr=gitvoyager.main:main',
        ],
    },
    install_requires=[
        'requests',
    ],
)
