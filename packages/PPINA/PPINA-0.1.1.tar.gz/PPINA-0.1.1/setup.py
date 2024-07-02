from setuptools import setup,find_packages

setup(
    name='PPINA',
    version='0.1.1',
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires = [
        "biopython>=1.81",
        "colorama>=0.4",
        "matplotlib>=3.8",
        "networkx>=3.3",
        "numpy>=1.24",
    ],
    python_requires=">=3.10",
    url='https://github.com/Bassam-Elhamsa/PPINA',
    license='MIT License',
    author='Bassam Elhamsa, Mahmoud Nashaat, Ebtehal Mahmoud, Mai Mohamed',
    author_email='bassamelhamsa@gmail.com',
    description='PPINA is a python package to analyze Protein Protein Interaction Networks'
)
