PROJECT_NAME = lost_ark_phishing

MAIN_SCRIPT = main.py

PYINSTALLER_OPTS = --onefile --noconsole --name $(PROJECT_NAME)

ASSESTS_DIR = assets
ASSETS_OPTS = --add-data "$(ASSESTS_DIR);$(ASSESTS_DIR)"

build:
	@echo "Creating executable with PyInstaller..."
	pyinstaller $(PYINSTALLER_OPTS) $(ASSETS_OPTS) $(MAIN_SCRIPT)

clean:
	@echo "Cleaning up..."
	rm -rf build dist __pycache__ $(PROJECT_NAME).spec

all: clean build
