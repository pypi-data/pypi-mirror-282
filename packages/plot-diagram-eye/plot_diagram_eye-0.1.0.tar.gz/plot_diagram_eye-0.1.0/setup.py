from setuptools import setup, find_packages

setup(
    name="plot_diagram_eye",
    version="0.1.0",
    description="A library designed to generate and visualize eye diagrams for digital communication signals. ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="K ABHISHEK MENON",
    author_email="kabhishekmenon@gmail.com",
    url="https://github.com/yourusername/eye_diagram",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.0",
        "matplotlib>=3.1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires='>=3.6',
)
