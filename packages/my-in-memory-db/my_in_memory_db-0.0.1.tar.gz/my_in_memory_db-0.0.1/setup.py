from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my_in_memory_db",
    version="0.0.1",
    author="unix1998",
    author_email="unix1998@yahoo.com",
    description="A simple in-memory database with transaction support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unix1998/my_in_memory_db",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'my_in_memory_db=my_in_memory_db.cli:main',
        ],
    },
)


