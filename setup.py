from setuptools import find_packages,setup
from typing import List

trigger = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements =[]

    with open (file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if trigger in requirements:
            requirements.remove(trigger)
    
    return requirements



setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Bhasvati',
    author_email= 'bhasvati2106@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)