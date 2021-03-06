import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AliExpressAPI", # Replace with your own username
    version="1.0.0",
    author="mytja",
    description="Get AliExpress results in a very very detailed JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mytja/AliExpressAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        "beautifulsoup4"
    ],
    python_requires='>=3',
)