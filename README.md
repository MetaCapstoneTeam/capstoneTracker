## Prerequisites
#### OSX/Linux
* Python 3.4
* Pip
* Virtualenv (pip install virtualenv)
* Virtualenvwrapper (pip install virtualenvwrapper)
* MySQL

#### Windows
##### Be sure to add python34 and python34/Scripts to you PATH
* Python 3.4
* Pip
* Virtualenv (pip install virtualenv)
* VIrtualenvwrapper (pip install virtualenvwrapper-win)
* MySQL

## Localhost Setup
1. Clone the repository:
   `$ git clone https://github.com/MetaCapstoneTeam/capstoneTracker.git capstone`

2. Navigate into capstone repo:
   `$ cd capstone`

3. Create Virtual Environment Wrapper using Python 3.x:
   `$ mkvirtualenv -p python3.4 capstone-project`

4. Go into you're local environment if not already there:
  	`$ workon capstone-project`
    <p>(capstone-project) should appear at the start of your command prompt

5. Install all the requirements:
	`$ cd c1_capstonetracker`
	`$ pip3 install -r requirements.txt`

6. Create local database
    `$ mysql -u root`
    `$ create database capitalonecapstone;`
    `$ quit`

7. Set up the database: (for windows do not include ./)
    `$ ./manage.py syncdb`
	   `$ ./manage.py shell < create_groups.py`
	    `$ ./manage.py makemigrations`
	     `$ ./manage.py migrate`

## MySQL Notes
* When creating the root account if asked to create a root password, you must
 remove the root password in order to run the syncdb and migrations call.
  `$ mysql -u root -p`
  enter your password
  `SET PASSWORD FOR root@localhost=PASSWORD('');`

## Adding code
Once you have completed your additions to files run the make file to check if your
code can be committed. Your code will be checked against the pep8 standards and
a code coverage check will be run. You want to conform to all standards and
have 100% code coverage.
