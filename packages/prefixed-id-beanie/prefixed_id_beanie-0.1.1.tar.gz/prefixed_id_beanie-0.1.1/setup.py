from setuptools import setup, find_packages

setup(
    name="prefixed_id_beanie",
    version="0.1.1",
    description="A utility library for prefixed IDs using Beanie",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="http://yourwebsite.com",
    packages=find_packages(include=['types', 'types.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
