# python setup.py install
from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='sahil gupta',
    author_email='vg7649004@gmail.com',
    packages=find_packages(),  # Corrected to find_packages() and added the comma
    install_requires=[
        "groq",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2"
    ], 
)
