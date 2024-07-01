from setuptools import setup, find_packages

setup(
    name="examplenewproject",
    version="0.3",  # Sürüm numarasını artırın
    packages=find_packages(),
    description="A Python wrapper for a C++ project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vasfi Tataroglu",
    author_email="testestteestetestes2009@gmail.com",
    url="https://github.com/brainvs/examplenewproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={
        'examplenewproject': ['examplenewproject.cpython-311-darwin.so'],
    },
    include_package_data=True,
    zip_safe=False,
)
