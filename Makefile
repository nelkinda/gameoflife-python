.PHONY: all
all: test

.PHONY: test
test: unit-test acceptance-test

.PHONY: unit-test
unit-test:
	python -m unittest discover

.PHONY: acceptance-test
acceptance-test:
	behave
