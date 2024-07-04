from setuptools import setup,find_packages

setup(
    name='MasterPB-STT',
    version='0.1',
    author='MasterPB',
    author_email='example@gmail.com',
    description='this is speech to text real time package crated by MasterPB best STT'
)
packages = find_packages(),
install_requirement = [
    'selenium',
    'webdriver_manager'
]



