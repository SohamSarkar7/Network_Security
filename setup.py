

from setuptools import find_packages, setup

from typing import List

def get_requiremnts()-> List[str]:
    requirement_list : List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_list


setup(
    name= "Network_Security",
    version="0.0.1",
    author="Soham sarkar",
    packages=find_packages(),
    install_requires = get_requiremnts()
)