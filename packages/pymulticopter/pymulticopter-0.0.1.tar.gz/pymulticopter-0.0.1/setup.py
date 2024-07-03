import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymulticopter",
    version="0.0.1",
    author="Sangmin Lee",
    author_email="everlastingminii@gmail.com",
    description="A framework for performing numerical simulation of multicopter system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minii93/pysimenv-multicopter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pysimenv',
        'numpy',
        'scipy',
        'matplotlib',
        'h5py',
        'pytictoc',
        'pyquaternion'
    ]
)
