# lambdata13, my own OOP python package which can be reused in the future.
### create their own Python package and install dependencies in a dedicated environment
#### code that should live on and be reused in a variety of circumstances. Enter modules, packages, and environments.
- pipenv as a Python packaging tool giving reproducible builds.
- write code based on shared principles of design and style,e.g PEP8. 
- To learn the basic principles of object-oriented programming(OOP), to design and building of large codebases.To create a basic Python class, with a constructor, methods, and fields.
- comparing pipenv, we will use containers(e.g. Docker) with a greater reproducibility (and deployability),are the tool of choice. A container is a minimal virtual operating system, complete with all the software needed to run the desired application
- test and document, a core part of software engineering, and code that lacks these properties is essentially impossible to maintain or build on in the long term.
-  choose an appropriate licenses of your dependencies and the ecosystem in general. You don’t need a law degree, but there are big differences between licenses you should understand, even ones that all count as “open source.”


## my_lambdata

Package for unit3-week1

Using the package from PIPY instructions:




## Installation

cd path/to/lambdata

Install package dependencies:

pipenv 



pipenv install  pytest-i https://test.pypi.org/simple/ my_lambdata

## Usage
Use an if __name__ == '__main__': guard to only execute code when a file is invoked as a script and not just imported.
An example script, a collection of classes that may be built upon

python my_lambdata/my_script.py