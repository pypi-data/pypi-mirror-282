import setuptools

# Package metadata
NAME = "AuthoRex"
VERSION = "1.0.1"
DESCRIPTION = "A package for generating and authenticating OTPs using MongoDB."
URL = "https://github.com/TraxDinosaur/AuthoRex"
AUTHOR = "TraxDinosaur"
AUTHOR_CONTACT = "https://traxdinosaur.github.io"
LICENSE = "CC-BY-SA 4.0"
KEYWORDS = ["OTP", "authentication", "MongoDB", "OTP generator", "OTP authenticator"]

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Packages required by the project
REQUIRED_PACKAGES = [
    "pymongo"
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_contact=AUTHOR_CONTACT,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    keywords=KEYWORDS,
    install_requires=REQUIRED_PACKAGES,
    python_requires=">=3.6",
)