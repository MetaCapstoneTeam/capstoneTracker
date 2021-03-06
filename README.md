## Prerequisites
#### OSX/Linux
* Python 3.4
* Pip (should be installed with python 3.4 installation)
* Virtualenv (pip3 install virtualenv)
* Virtualenvwrapper (pip3 install virtualenvwrapper)
* MySQL

#### Windows
##### Be sure to add python34 and python34/Scripts to you PATH
* Python 3.4
* Pip ( should be installed with the python3.4 installation)
* Virtualenv (pip3 install virtualenv)
* Virtualenvwrapper (pip3 install virtualenvwrapper-win)
* MySQL

## Localhost Setup
1. Clone the repository:
   <p>`$ git clone https://github.com/MetaCapstoneTeam/capstoneTracker.git capstone`

2. Navigate into capstone repo:
   <p>`$ cd capstone`

3. Create Virtual Environment Wrapper using Python 3.4:
   <p>`$ mkvirtualenv -p python3.4 capstone-project`

4. Go into you're local environment if not already there:
  	<p>`$ workon capstone-project`
    <p>(capstone-project) should appear at the start of your command prompt

5. Install all the requirements:
	<p>`$ cd c1_capstonetracker`
	<p>`$ pip3 install -r requirements.txt`

6. Create local database
    <p>`$ mysql -u root`
    <p>`$ create database capitalonecapstone;`
    <p>`$ quit`

7. Set up the database: (for windows do not include ./)
    <p>`$ ./manage.py syncdb`
	  <p>`$ ./manage.py shell < projectTracker/create_groups.py`
	  <p>`$ ./manage.py makemigrations`
	  <p>`$ ./manage.py migrate`

## MySQL Notes
* When creating the root account if asked to create a root password, you must
 remove the root password in order to run the syncdb and migrations call.
  <p>`$ mysql -u root -p`
  <p>enter your password
  <p>`SET PASSWORD FOR root@localhost=PASSWORD('');`

* In order to use the mysql -u root, be sure to start your mysql server first. To start or stop the server use these commands
  <p>`$ mysql.server start`
  <p>`$ mysql.server stop`

##Virtual Env Notes
* If you are having issues running the mkvirtualenv or workon commands, make sure you have your vitrual env python and variable are set correctly. Adding these three lines to your .bash_profile should do the trick:
<p> `export WORKON_HOME=$HOME/.virtualenvs`  (This should be set to where ever your .virtualenvs directory is)
<p> `export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3` (This should be set to where ever your Python3 is located)
<p> `source /usr/local/bin/virtualenvwrapper.sh` (This should be where ever your virtualenvwrapper.sh can be found)
* In order to stop working within your virtualenv just type deactivate in your command prompt

## Adding code
Once you have completed your additions to files run the make file to check if your
code can be committed. Your code will be checked against the pep8 standards and
a code coverage check will be run. You want to conform to all standards and
have 100% code coverage.

For non linux running the make file will be almost impossible to run, you will be able to commit but it is easiest to keep code consistant with these standards in place.
