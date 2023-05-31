from setuptools import find_packages,setup

from typing import List

def get_requirements() ->List[str]:
    package_list=[]
    with open('requirements.txt','r') as f:
        for line in f:
            # Remove any leading/trailing whitespace
            line=line.strip()

            if not line or line.startswith('#'):
                continue
            package_name=line.split('==',1)[0]
            package_list.append(package_name)
    return package_list

setup(
    name="finance_complaint",
    version="0.0.1",
    author="riad",
    author_email="rrriaduddin@gmail.com",
    packages=find_packages(),
    install_requires=[],
)