from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='zomato_delivery_time_prediction',
    version='0.0.1',
    author='kmsumanth',
    author_email='kmsumanth08@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')

)