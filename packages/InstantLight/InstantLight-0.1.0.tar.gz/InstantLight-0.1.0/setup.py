from setuptools import setup, find_packages

setup(
    name="InstantLight",
    version="0.1.0",
    description="A Python SDK for your API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Saliou Kane",
    author_email="saliou@fotographer.ai",
    url="https://github.com/FotographerAI/InstantLight-sdk/",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
