from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    requirments = []
    with open('requirments.txt') as f:
        requirments = f.readlines()
        requirments = [req.replace("\n","") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)
            
    return requirments

setup(
    name='mlproject',
    author='MD.Saad',
    author_email='saadbagwan07041@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')

)