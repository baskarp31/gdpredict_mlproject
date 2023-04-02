from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n"," ") for req in requirements]
        


setup(
name='gdpredict',
version='0.0.1',
author='Baskar',
author_email='baskarp31@gmail.com',
packages=find_packages(),
install_reuires=get_requirements('requirements.txt')

)