from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="blurplefier-standalone",
    version="0.0.6",
    description="A standalone version of the blurplefier that the Blurplefier bot has.",
    license="MIT",
    long_description=long_description,
    author="Project Blurple, Sonic49",
    url="https://github.com/Sonic4999/blurplefier-standalone",
    packages=["blurplefier"],
    install_requires=["pillow"],
    python_requires=">=3.8.0",
)
