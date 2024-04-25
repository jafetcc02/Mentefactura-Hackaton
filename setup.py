import setuptools

setuptools.setup(
    name="Mentefactura-Hackaton",
    version="0.0.1",
    author="J. Castañeda Cerdan",
    author_email="jafetcc17@gmail.com",
    maintainer="Dan H. Muñiz",
    maintainer_email="",
    description="A package containing deep learning methods .",
    url="https://github.com/jafetcc02/Mentefactura-Hackaton",
    project_urls={"Bug Tracker": "https://github.com/jafetcc02/Mentefactura-Hackaton/issues"},
    license="BSD 3-Clause",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[ 
        "pandas==1.2.4",
        "transformers==4.40.1",
        "torch==2.2.1",
        "os",
        "time", 
        "googletrans==4.0.0rc1",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.10",
)