from setuptools import setup, find_packages

setup(
    name="my_unique_import",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    description="A custom importer package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="http://example.com",
    author="Jingyuan Chen",
    author_email="jchensteve@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)