init:
	pip install -r requirements.txt

install:
	pip install .

check:
	cd tests && python -m unittest discover -s . -p *.py -v
