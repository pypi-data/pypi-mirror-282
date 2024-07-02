
from setuptools import setup, find_packages

setup(
    name="performaddition",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    author="Nandhini",
    author_email="nandhini67288@gmail.com",
    description="A short description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/nandhinikesavan20/hello_world",  # Your package's GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.10',
)
