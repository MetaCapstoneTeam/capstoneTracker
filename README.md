## Prerequisites
#### OSX/Linux
* Python 3.4
* Pip
* Virtualenv (pip install virtualenv)
* Virtualenvwrapper (pip install virtualenvwrapper)

## Localhost Setup
1. Clone the repository:
   `$ git clone https://github.com/MetaCapstoneTeam/capstoneTracker.git capstone`

2. Navigate into capstone repo:
   `$ cd capstone`

3. Create Virtual Environment Wrapper using Python 3.x:
   `$ mkvirtualenv -p python3.4 capstone-project`

4. Go into youre local environment:
	`$ workon capstone-project

5. Install all the requirements:
	`$ cd c1_capstonetracker
	`$ pip3 install -r requirements.txt

6. Set up the database
	`$ ./manage.py shell < create_groups.py
	`$ ./manage.py makemigrations
	`$ ./manage.py migrate


#### MySQL Database
  1. Create a local capitalonecapstone database 
  	'$ mysql -u root'
  	'$ create database capitalonecapstone'


