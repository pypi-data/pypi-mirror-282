# setup.py
from setuptools import setup, find_packages

setup(
    name="dir_list_kdon_20",
    version="0.2",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dir_list = dir_list.main:main'
        ]
    },
)
