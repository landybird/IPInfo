# encoding : utf-8
# __author__ = 'jm'

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ip_info_all",  #
    version="0.0.5",
    author="landybird",
    author_email="1442172978@qq.com",
    description="get IPV4 or IPV6 info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/landybird/IPInfo",
    install_requires=[
        "netifaces",],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)