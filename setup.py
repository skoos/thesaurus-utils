from setuptools import setup, find_packages

with open('requirements.txt', 'r') as reqfile:
    setup(
        name='thesaurusutils',
        version='0.1',
        description='Python Wrapper for Thesaurus API',
        url='http://github.com/skoos/thesaurus-utils',
        package_dir={'':'src'},
        packages=find_packages('src'),
        install_requires=reqfile.readlines()
    )
