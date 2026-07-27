from setuptools import find_packages,setup
from typing import List
HYPN_DOT_E='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path, 'r') as f:
        requirements=f.readlines()
    # Remove newline characters from each requirement
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPN_DOT_E in requirements:
            requirements.remove(HYPN_DOT_E)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    packages=find_packages(),
    author='Yogesh Kumawat',
    author_email='yogesh.kumawat.civ23@itbhu.ac.in',
    install_requires=get_requirements('requirements.txt')
)