from setuptools import setup, find_packages

setup(
    name="avcontext",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    description="Interactive script for converting letters to various cases and transformations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Avinion",
    author_email="shizofrin@gmail.com",
    url="https://x.com/Lanaev0li",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'avcontext=avcontext.avcontext:main',
        ],
    },
)
