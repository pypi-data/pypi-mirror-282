from setuptools import setup, find_packages

setup(
    name='gitvoyager',
    version='2.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'voyager=voyager.main:main',
            'vgr=voyager.main:main',
        ],
    },
    install_requires=[
        'requests',
    ],
)
