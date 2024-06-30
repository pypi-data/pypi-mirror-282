from setuptools import setup, find_packages

setup(
    name="tim_odoo",
    version="0.2.0",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bùi Đức Tuấn",
    author_email="buiductuan12081995@gmail.com",
    url="https://github.com/OrcCyber/tim.git",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
