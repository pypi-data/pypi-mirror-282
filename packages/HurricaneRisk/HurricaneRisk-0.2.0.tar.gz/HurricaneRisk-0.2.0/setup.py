# setup.py

from setuptools import setup, find_packages

setup(
    name="HurricaneRisk",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "geopandas",
        "shapely",
        "requests",
        "pandas",
        "openpyxl"
    ],
    author="Scott",
    #author_email="your.email@example.com",
    description="A library to analyze and visualize hurricane risk",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/yourusername/my_hurricane_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
