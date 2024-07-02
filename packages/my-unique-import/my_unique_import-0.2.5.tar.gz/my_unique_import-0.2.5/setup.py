from setuptools import setup, find_packages

setup(
    name="my_unique_import",
    version="0.2.5",
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
    entry_points={
        'console_scripts': [
            'qgit=my_import.quick_git:main',  # 格式：命令名=模块路径:函数名
        ],
    },
    python_requires='>=3.7',
)