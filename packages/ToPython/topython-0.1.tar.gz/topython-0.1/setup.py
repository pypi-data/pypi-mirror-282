from setuptools import setup, find_packages

setup(
    name='ToPython', 
    version='0.1',  # الإصدار الأول
    packages=find_packages(),
    install_requires=[
        'requests',
        'uuid',
        'secrets',
        'json', 
        'time',
        'urllib'
    ],
    author='L7N Iraqi',
    author_email='l7npypi@gmail.com',
    description='Best library To Checker Applications',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://t.me/ToPython',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)