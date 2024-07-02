# setup.py

from setuptools import setup, find_packages

setup(
    name='desmy-python',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    include_package_data=True,
    license='MIT',
    description='A Django manager for create, update, delete, and read operations with pagination, search, and sorting.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Desmy Dev',
    author_email='desmydev@gmail.com',
    url='https://github.com/yourusername/desmy-python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
    ],
)
