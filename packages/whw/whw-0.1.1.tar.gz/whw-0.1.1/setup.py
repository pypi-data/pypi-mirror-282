from setuptools import setup, find_packages

setup(
    name="whw",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "web3",
        "cryptography",
        "requests"
    ],
    author="paquitoKikakop",
    author_email="paquitokikakop@gmail.com",
    description="Module gestion wallet basé sur la blockchain Ethereum",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://gitlab.com/paquito3/whw-wallet-web3-module.git",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
