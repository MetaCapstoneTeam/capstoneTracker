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
   <p>`$ git clone https://github.com/MetaCapstoneTeam/capstoneTracker.git capstone`

2. Navigate into capstone repo:
   <p>`$ cd capstone`

3. Create Virtual Environment Wrapper using Python 3.x:
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
	  <p>`$ ./manage.py shell < create_groups.py`
	  <p>`$ ./manage.py makemigrations`
	  <p>`$ ./manage.py migrate`

## MySQL Notes
* When creating the root account if asked to create a root password, you must
 remove the root password in order to run the syncdb and migrations call.
  <p>`$ mysql -u root -p`
  <p>enter your password
  <p>`SET PASSWORD FOR root@localhost=PASSWORD('');`

## Adding code
Once you have completed your additions to files run the make file to check if your
code can be committed. Your code will be checked against the pep8 standards and
a code coverage check will be run. You want to conform to all standards and
have 100% code coverage.
