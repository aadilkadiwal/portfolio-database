.PHONY: run deps migrate sh db

# target: Run a dev server on local host
run:
	manage runserver

#target: To install all dependencies
deps:
	pip install -r requirements.txt

#target: To run migrations
migrate:
	manage makemigrations
	manage migrate

#target: To open extension shell
sh: 
	manage shell_plus

#target: To open database shell
db:
	manage dbshell

