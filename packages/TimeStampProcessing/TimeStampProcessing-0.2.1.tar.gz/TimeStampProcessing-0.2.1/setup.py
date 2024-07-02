from setuptools import setup, find_packages

setup(
    name="TimeStampProcessing",
    version="0.2.1",
    author="Wei Wang",
    author_email="wwang487@wisc.edu",
    description="A package for timestamp-related data processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/yourusername/TimeStampProcessing",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=open("requirements.txt").read().splitlines(),
)
