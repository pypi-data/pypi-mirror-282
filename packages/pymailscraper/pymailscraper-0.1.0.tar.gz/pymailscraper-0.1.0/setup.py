from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pymailscraper",
    version="0.1.0",  # Update this as you release new versions
    author="Md Mazedul Islam Khan",
    author_email="mazedulislamkhan@gmail.com",
    description="A Python tool for scraping email addresses from websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmikhan/pymailscraper",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "tqdm",
    ],
    entry_points={
        'console_scripts': [
            'pymailscraper=pymailscraper.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
