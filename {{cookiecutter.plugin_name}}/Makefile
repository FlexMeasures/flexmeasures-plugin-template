# Note: use tabs
# actions which are virtual, i.e. not a script
.PHONY: install install-for-dev test 


# ---- Development ---

test:
	make install-for-dev
	pytest


# ---- Installation ---

install:
	pip install -e .

install-for-dev:
	pip install -r requirements.txt
	make install
	pre-commit install

