.PHONY: all
all: test

.PHONY: test
test: coverage-reports/unit-test.coverage coverage-reports/acceptance-test.coverage

coverage-reports/unit-test.coverage:
	COVERAGE_FILE=$@ coverage run -m unittest discover

coverage-reports/acceptance-test.coverage:
	COVERAGE_FILE=$@ coverage run -m behave

.coverage: coverage-reports/acceptance-test.coverage coverage-reports/unit-test.coverage
	coverage combine coverage-reports/*.coverage

coverage-reports/coverage-.xml: .coverage
	coverage xml -o coverage-reports/coverage-.xml

.PHONY: sonarqube
sonarqube: coverage-reports/coverage-.xml
	docker run --network host --rm -v "$$(pwd):/usr/src" sonarsource/sonar-scanner-cli -Dsonar.projectKey=gameoflife-python

.PHONY: sonard
## Runs a Sonar server locally.
sonard:
	docker start sonarqube || docker run -d --name sonarqube sonarqube

.PHONY: clean
clean::
	coverage erase
clean::
	$(RM) -r coverage-reports
