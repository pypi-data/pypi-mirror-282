
#  pip install setuptools
from setuptools import setup, find_packages

setup(
    name= 'SubhashTech-STT',
    version='0.1',
    author='Subhash Chandra',
    author_email='solisubhash1415@gmail.com',
    description='This is Speech to text package created by Subhash Chandra'
)
packages= find_packages(),
install_requirements= [
    'selenium',
    'webdriver_manager'
]

