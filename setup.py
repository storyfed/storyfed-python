from setuptools import setup, find_packages

setup(
    name="storyfed",
    version="1.0.1",
    description="The official Python SDK for the Storyfed Video Generation API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Storyfed",
    url="https://github.com/YOUR_GITHUB_USERNAME/storyfed-python",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)
