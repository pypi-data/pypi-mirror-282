from setuptools import setup, find_packages

setup(
    name="ip_restriction",
    version="1.0.0",
    author="Bothraj P",
    author_email="bothrajvasu@gmail.com",
    description="A middleware for IP-based access restriction in Django",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bothrajvasu/IP-Restriction-Middleware",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
