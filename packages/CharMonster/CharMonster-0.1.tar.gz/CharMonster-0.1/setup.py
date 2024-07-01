from setuptools import setup, find_packages

setup(
    name='CharMonster',
    version='0.1',
    author='James Evans',
    author_email='joesaysahoy@gmail.com',
    url='https://github.com/primal-coder/CharMonster',
    packages=find_packages(),
    install_requires=[
        'gridengine_framework',
        'dicepy',
        'pymunk',
        'entyty'
    ],
    license='MIT'    
)