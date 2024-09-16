from setuptools import setup

setup(
    name="aa598",
    version="0.0.1",
    description="virtual environment for aa598 homework",
    author="Karen Leung",
    author_email="kymleung@uw.edu",
    packages=["aa598"],
    install_requires=[
        "jax",
        "matplotlib",
        "numpy",
        "torch",
        "ipywidgets",
        "ipykernel"
    ],
)