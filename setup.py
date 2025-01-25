from setuptools import setup, find_packages

setup(
    name="endless_2020",
    version="0.1.0",
    description="Hindsight is 20/20",
    author="alexsmbaratti",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": [
            "freezegun==1.2.2",
        ],
    },
)
