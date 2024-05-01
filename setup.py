from setuptools import setup, find_packages
from typing import List


# Declaring the variables for setup functions
PROJECT_NAME="Housing-Predictor"
VERSION="0.0.1"
AUTHOR="Sandeep"
DESCRIPTION="This is a Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENTS="requirements.txt"

def get_requirements_list()->List[str]:

    '''
    Description : This function is going to return the list of requirements
    mention in the requirements.txt file
    '''
    with open(REQUIREMENTS) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

