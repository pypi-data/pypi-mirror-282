from setuptools import setup, find_packages

setup(
    name="LangChainUtility",
    version="0.0.1",
    description="LangChain Utility Library",
    author="Lee Wan",
    author_email="snoopy_kr@yahoo.com",
    url="https://github.com/snoopykr/LangChainUtility",
    install_requires=["langchain"],
    packages=find_packages(exclude=[]),
    keywords=[
        "langchain",
        "snoopy_kr",
    ],
    python_requires=">=3.0",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
