from setuptools import find_packages,setup

from typing import List

def get_reqiurements()->List[str]:
    """
    this fucntion will return list of requirmements
    """
    requirements_list:List[str] = []
    
    return requirements_list
setup(
    name="sensor",
    version="0.0.1",
    author="rizwan",
    author_email="rizwanzhad@gmail.com",
    packages = find_packages(),
    install_requires=get_reqiurements().#["pymongo==4.2.0"]
)
