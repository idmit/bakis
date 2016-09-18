from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_ = f.read()

setup(
    name='bakis',
    version='0.1.0',
    description='Predict seizures in long-term human intracranial EEG recordings',
    long_description=readme,
    author='Ivan Dmitrievsky',
    author_email='ivan.dmitrievsky@gmail.com',
    url='https://github.com/idmit/bakis',
    install_requires=[
        'altair',
        'attrs',
        'click',
        'keras',
    ],
    license=license_,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bakis=bakis.cli:root'
        ]
    },
)
