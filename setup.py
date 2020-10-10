import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="txtimg",
    version="0.0.8",
    author="Yoong Kang Lim",
    author_email="yoongkang.lim@gmail.com",
    description="A library to easily create text-based images (e.g. images that primarily contain text).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoongkang/txtimg",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["Pillow>=7.2,<7.3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
