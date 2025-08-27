from setuptools import setup, find_packages

setup(
    name="mytool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",  # depende de tu parser
    ],
    entry_points={
        "console_scripts": [
            "mytool=mytool.main:main",
        ],
    },
    author="Charles J. Rodriguez Marin",
    description="Herramienta para parsear archivos JSON y YAML",
    python_requires=">=3.7",
)
