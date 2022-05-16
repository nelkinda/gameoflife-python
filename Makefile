## Game of Life in Pythonn
##

export PATH:=./venv/bin/:$(PATH)

.PHONY: all
## all: Verifies the Game of Life program.
all: verify

.PHONY: verify
## verify: Performs all verification (lint and test).
verify: lint test

.PHONY: pipeline
## pipeline: Whatever the CI/CD Pipeline is supposed to run.
pipeline: pip-install verify

.PHONY: setup-venv
## setup-venv: Setup a virtual environment.
setup-venv:
	python3 -m venv venv

.PHONY: pip-install
## pip-install: Install requirements.
pip-install: .pip-install-timestamp
.pip-install-timestamp: requirements.txt
	pip install -r requirements.txt
	touch $@

.PHONY: pip-freeze
## pip-freeze: Update requirements.txt.
pip-freeze:
	pip freeze >requirements.txt

.PHONY: test
## test: Run tests (including coverage).
test: .coverage

.PHONY: lint
## lint: Run static code analyzers (mypy and prospector).
lint: pip-install
	mypy *.py
	prospector *.py

coverage-reports/unit-test.coverage: pip-install
	COVERAGE_FILE=$@ coverage run --omit "venv/*" -m unittest discover

coverage-reports/acceptance-test.coverage: pip-install
	COVERAGE_FILE=$@ coverage run --omit "venv/*" -m behave

.coverage: coverage-reports/acceptance-test.coverage coverage-reports/unit-test.coverage
	coverage combine coverage-reports/*.coverage
	coverage report --fail-under 100.0

coverage-reports/coverage-.xml: .coverage
	coverage xml -o coverage-reports/coverage-.xml

.PHONY: sonarqube
sonarqube: coverage-reports/coverage-.xml
	docker run --network host --rm -v "$$(pwd):/usr/src" sonarsource/sonar-scanner-cli -Dsonar.projectKey=gameoflife-python

.PHONY: sonard
## Runs a Sonar server locally.
sonard:
	docker start sonarqube || docker run -d --name sonarqube sonarqube

.PHONY: checkUpdates
checkUpdates:
	pip list --outdated

.PHONY: clean
## clean: Removes generated files (in this case, coverage reports).
clean::
	coverage erase
clean::
	$(RM) -r coverage-reports

.PHONY: help
## help: Prints this help text.
help:
	@sed -n 's/^## \?//p' $(MAKEFILE_LIST)
