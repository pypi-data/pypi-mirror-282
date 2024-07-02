from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description1 = fh.read()

setup(
    name="GDI_effects",
    version="0.1",
    author="coder",
    author_email="memecoder17@gmail.com",
    description="Một mô tả ngắn về package của bạn",
    long_description=long_description1,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)