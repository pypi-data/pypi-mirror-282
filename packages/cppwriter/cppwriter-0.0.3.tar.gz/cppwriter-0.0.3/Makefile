VENV_PATH = ./venv
VENV = . $(VENV_PATH)/bin/activate;
VERSION = 0.0.3

.PHONY: clean
clean:
	rm -rf ./*.egg-info
	rm -rf ./.pytest_cache
	rm -rf ./.ruff_cache
	rm -rf ./build
	rm -rf ./dist
	rm -f .version

.PHONY: test
test:
	$(VENV) pytest -vv tests/*.py

.PHONY: build
build:
	echo "$(VERSION)" > .version
	$(VENV) python -m build
	$(VENV) pip install .

.PHONY: lint
lint:
	$(VENV) pylint ./cppwriter
	$(VENV) ruff check ./cppwriter

.PHONY: publish
publish: build
	git add Makefile
	git commit -m "chore: release $(VERSION)"
	git tag -a $(VERSION) -m "release $(VERSION)"
	$(VENV) python -m twine upload --repository pypi dist/*

configure:
	rm -rf $(VENV_PATH)
	make $(VENV_PATH)

$(VENV_PATH):
	python3.11 -m venv $(VENV_PATH)
	$(VENV) pip install -r requirements.txt