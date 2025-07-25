"""
Setup script for my-github-class package.
"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-github-class",
    version="0.1.0",
    author="GitHub Actions Tutorial",
    author_email="tutorial@example.com",
    description="A tutorial project demonstrating GitHub Actions with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-github-class",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Add your runtime dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
            "bandit>=1.7.0",
            "safety>=2.0.0",
            "pylint>=2.15.0",
            "radon>=5.0.0",
            "xenon>=0.9.0",
        ],
    },
)