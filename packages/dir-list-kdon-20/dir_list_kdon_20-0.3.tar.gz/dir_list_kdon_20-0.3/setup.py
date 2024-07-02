from setuptools import setup, find_packages

setup(
    name="dir_list_kdon_20",
    version="0.3",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dir-list-kdon-20 = dir_list.main:main'
        ]
    },
)
