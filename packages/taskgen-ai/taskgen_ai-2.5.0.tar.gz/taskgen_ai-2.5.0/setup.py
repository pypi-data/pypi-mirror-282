from setuptools import setup, find_packages

setup(
    name="taskgen",
    version="2.5.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.3.6",
        "dill>=0.3.7",
        "termcolor>=2.3.0"
    ],
)
