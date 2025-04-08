.PHONY: build clean run

build:
	pyinstaller --onefile src/main.py --name weapon-tracker --add-data "src/config/weapons_config.json:config"

clean:
	rm -rf build dist __pycache__ *.spec

run:
	./dist/weapon-tracker
