from setuptools import setup, find_packages

setup(
    name="toolsworks",
    version="0.1.0",
    description="A simple Python package for demonstration purposes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/toolsworks",
    author="Dong H. Ahn",
    author_email="donga@nvidia.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "toolsworks=toolsworks.cli:main",
        ],
    },
)

