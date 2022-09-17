install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_project1.py

format:
	black *.py


lint:
	pylint --disable=R,C project1.py

all: install lint test