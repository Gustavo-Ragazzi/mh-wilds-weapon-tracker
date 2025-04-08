.PHONY: install-dev code-check build clean run

install-dev:
	poetry install --no-root

code-check:
	poetry run pre-commit run --all-files

build:
	poetry run pyinstaller --onefile src/main.py --name weapon-tracker.exe
	cp config/default.json dist/weapons_config.json
	@echo "Build completed: dist/weapon-tracker.exe + weapons_config.json"

run:
	./dist/weapon-tracker

clean:
	rm -rf dist build *.spec __pycache__ .pytest_cache .mypy_cache .coverage
