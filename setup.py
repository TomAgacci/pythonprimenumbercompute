from setuptools import setup, find_packages

setup(
    name="tama-prime",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sympy",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "tama-prime = tama_prime.cli:main",
        ]
    },
    author="Maximillian",
    description="Tama Prime System: analytic + discrete prime modeling engine",
    license="MIT",
)
