install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_fast_api.py

format:
	black *.py


lint:
	pylint --disable=R,C nfl.py

all: install lint test
