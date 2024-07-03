from setuptools import setup, find_packages

setup(
    name="facilities",
    version="0.1.2",
    author="RS",
    author_email="",
    description="Package for facilities scrape",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Vitek233/FACILITIES",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)