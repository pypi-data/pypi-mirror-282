from setuptools import setup, find_packages

setup(
    name='prefixed_id_beanie',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beanie',
    ],
    author='Daniel Alvarado',
    author_email='danieldls.ucv@gmail.com',
    description='A utility library for prefixed IDs using Beanie',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DanielDls-exe/prefixed_id_beanie',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)