run:
	flask --app server run --debug

shell:
	flask --app server shell

install:
	pip install -r requirements.txt

-include Makefile.local.mk
