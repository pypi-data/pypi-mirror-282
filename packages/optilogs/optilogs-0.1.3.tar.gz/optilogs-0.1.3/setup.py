from setuptools import setup, find_packages

setup(
    name="optilogs",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Allan PEREZ GONZALEZ",
    author_email="aperezgo74@gmail.com",
    description="A simple logging library to send logs to a server",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
