.DEFAULT_GOAL := or

coverage:
	coverage run --source=. --omit=c1_capstonetracker/*,**/migrations/* manage.py test
	coverage report

test:
	python manage.py test

clean:
	find . -name '*.pyc' -delete
	coverage erase
	rm -r **/__pycache__

validate:
	flake8 . --ignore D100,F403 --exclude=**/migrations/*,uploads/*

check:
	python manage.py check

runserver:
	python manage.py runserver

success:
	@tput setaf 2
	@echo "All systems are go. You may now commit to master"
	@tput sgr0

fail:
	@tput setaf 1
	@echo "An error has occured. Please fix it and try again"
	@tput sgr0	

all: validate check coverage success

or:
	@${MAKE} all || ${MAKE} fail