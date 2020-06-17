########################################################################################

# Sometimes we have to use someone else’s code(Module) in our program 
# because it saves our lot of time and off-course it is legal and free.

#### Modules ####

# Module – Module or library is the file which contain definitions of several functions,
# classes, variables, etc. which are written by someone else for free use.

#### Pip ####

# Pip – Pip is a package manager in python
# i.e. pip command is used to download any external module in python. 
# It is something like which helps us to get something from somewhere 
# and automatically save packages at suitable location for futher use.

### We can install any module in our system by pip command :

# Simply open cmd or Powershell in your system.
# And then type pip install module_name and press enter.

### Example : 
# >pip install numpy

# After that the module will start downloading 
# and will install automatically in your computer.

# After installing any module in python 
# you can import it in your program or in your project of Python.

### Example :
## In file xyz.py write: ## 
import numpy


########## There are 2 types of modules in Python :

# Built-in Modules -
# Built-in modules are those modules which are pre-installed in python 
# i.e. there is no need to download them before using. 
# These modules come with python interpreter itself.

# Example – random module, winreg, etc.

# To get complete list of built-in modules of python - 
link = "https://docs.python.org/3/py-modindex.html"

# External Modules –
# These are those modules which are not pre-installed in python 
# i.e. we need to download them before using in our program.

# Example – Flask, Pandas, etc.

##################### That's all about modules in Python. #########################


################################ Extra Content  ###################################

## The following command will install the latest version of a module 
#  and its dependencies from the Python Packaging Index:

#=>$ pip install SomePackage

## It’s also possible to specify an exact or minimum version directly on the command line.
#  When using comparator operators such as >, < or some other special character which get 
# interpreted by shell, the package name and the version should be enclosed within double quotes:

#=>$ pip install SomePackage==1.0.4    # specific version
#=>$ pip install "SomePackage>=1.0.4"  # minimum version

## Normally, if a suitable module is already installed, 
# attempting to install it again will have no effect. 
# Upgrading existing modules must be requested explicitly:

#=>$ pip install --upgrade SomePackage