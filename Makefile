.PHONY: install-dev build clean

install-dev:
	poetry install

build:
	poetry run pyinstaller --onefile src/main.py --name weapon-tracker

clean:
	rm -rf dist build *.spec __pycache__
