virtualenv
~~~~~~~~~~

Virtualenv is a script written by Ian Bicking that allows 
development of python libraries without polluting the
system path.

**Quick Start** ::

    #Create your project
    $ virtualenv projectdir

    #cd into the project
    $ cd projectdir

    #activate the new environment
    $ . ./bin/activate

Afer creating the environment, the user just needs to run the *activate*
script in the projects bin directory.

Once in the new environment, python *setup.py* and *pip*
will install everything into *projectdir* as if it were
root.  This removes the need for root access and allows
the end user to get his packages from **PyPI** through
*pip* instead of a distribution's set of packages (which
could be out of date.)

**virtualenv** changes the path, the python path and the
prompt to notify the user is in a different environment.

The prompt change will look something like this::

    (projectdir)user@computer:~/projects/projectdir$  


**Useful Options**::

    -p or --python:      Sets the python interpreter explicitly
    --relocatable:       Make the environment movable
    --no-site-packages:  No access to system-wide site-packages
    --setuptools:        Use setuptools instead of distribute
    --clear:             Clear the environment before creation
    --prompt:            Change the prompt
    

    



