from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="Hemanth",
    author_email="hemanthvhs@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-google-genai','langchain ','langchain-astradb','datasets','pypdf','python-dotenv','flask']
)