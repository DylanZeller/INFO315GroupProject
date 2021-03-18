from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'SQLite Database Wrapper'
LONG_DESCRIPTION = 'SQLite Database Wrapper for Info 315'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="db_wrapper", 
        version=VERSION,
        author="INFO315Group",
        author_email="",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'wrapper'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)