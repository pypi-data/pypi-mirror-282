import setuptools
import a3rt_talkpy

__name__ = "a3rt_talkpy"
__author__ = "NattyanTV"
__description__ = "A3RT Talk API wrapper for Python"
__url__ = "https://github.com/nattyan-tv/a3rt-talkpy"
__classifiers__ = [
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: MIT License"
]
__install_requires__ = [
    "requests",
    "asyncio",
    "aiohttp"
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=a3rt_talkpy.__name__,
    version=a3rt_talkpy.__version__,
    install_requires=__install_requires__,
    author=__author__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=setuptools.find_packages(),
    classifiers=__classifiers__,
)
