import pathlib

with open(
    str(pathlib.Path(__file__).parent.absolute()) + "/fib_py/version.py", "r"
) as fh:
    version = fh.read().split("=")[1].strip().replace("'", "")

with open("README.md", "r") as fh:
    long_description = fh.read()

from setuptools import find_packages, setup

setup(
    name="nbg_fib_py",
    version=version,
    author="nebelgrau77",
    author_email="nebelgrau77@gmail.com",
    description="Calculates a Fibonacci number",
    # long_description="A basic library to calculate Fibonacci numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nebelgrau77/fib-py.git",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">3",
    tests_require=["pytest"],
    entry_points={"console_scripts": ["fib-number = fib_py.cmd.fib_numb:fib_numb"]},
)
