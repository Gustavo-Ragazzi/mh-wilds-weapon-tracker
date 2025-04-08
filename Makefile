.PHONY: build clean run

build:
	pyinstaller --onefile src/main.py --name weapon-tracker
	cp config/default.json dist/weapons_config.json

clean:
	rm -rf build dist __pycache__ *.spec

run:
	./dist/weapon-tracker
