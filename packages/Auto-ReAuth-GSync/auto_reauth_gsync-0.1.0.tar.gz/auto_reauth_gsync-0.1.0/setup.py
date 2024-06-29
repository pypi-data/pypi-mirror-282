from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="Auto-ReAuth-GSync",
    version="0.1.0",
    install_requires=requirements,
    description="Google Drive syncing script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="hengtseChou",
    author_email="hankthedev@gmail.com",
    url="https://github.com/hengtseChou/Auto_ReAuth-GSync",
    license="MIT",
    keywords="sync",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    entry_points={
        "console_scripts": [
            "argsync = src.main:cli",
        ],
    },
)