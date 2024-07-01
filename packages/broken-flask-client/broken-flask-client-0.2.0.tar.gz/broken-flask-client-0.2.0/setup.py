"""Setup script"""
import setuptools
import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def get_version():
    init = open(os.path.join(HERE, "broken_flask_client", "version.py")).read()
    return VERSION_RE.search(init).group(1)


def get_description():
    return open(
        os.path.join(os.path.abspath(HERE), "broken_flask_client", "README.md"), encoding="utf-8"
    ).read()


setuptools.setup(
    name="broken-flask-client",
    include_package_data=True,
    version=get_version(),
    author="Kinnaird McQuade",
    author_email="kinnairdm@gmail.com",
    description="Client for the broken-flask app",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvsecurity/broken-flask",
    packages=setuptools.find_packages(exclude=["flask_app*"]),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=True,
    keywords="aws iam security",
    python_requires=">=3.7",
)