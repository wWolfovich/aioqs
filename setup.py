
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aioqs-wWolf",
    version="0.5",
    author="Oleg Marin",
    author_email="wWolfovich@gmail.com",
    description="Async queue and scheduler with limit for number of simultaneous coroutines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wWolfovich/aioqs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE v.3",
        "Operating System :: OS Independent",
    ],
)