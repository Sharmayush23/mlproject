from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str) -> List[str]:
    with open("requirements.txt") as f:
        return f.read().splitlines()



setup(
    name='mlproject',
    version='0.1',
    author='Ayush',
    author_email="sharmayush70@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)