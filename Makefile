PYTHON ?= python

export PYTHONPATH = $(shell echo "$$PYTHONPATH"):./jukebox

.PHONY: all check clean clean-pyc clean-patchfiles pylint reindent test

all: clean-pyc check test

check:
	@$(PYTHON) utils/check_sources.py -i jukebox/manage.py -i jukebox/registration -i jukebox/music/templatetags/seconds_to_duration.py -i jukebox/utils/templatetags/digg_templatetag.py -i lib -i debian -i build -i tests/coverage.py .

clean: clean-pyc clean-patchfiles

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-patchfiles:
	find . -name '*.orig' -exec rm -f {} +
	find . -name '*.rej' -exec rm -f {} +

pylint:
	@pylint --rcfile utils/pylintrc jukebox

reindent:
	@$(PYTHON) utils/reindent.py -r -B .

test:
	@cd tests; $(PYTHON) run.py -d -m '^[tT]est' $(TEST)

covertest:
	@cd tests; $(PYTHON) run.py -d -m '^[tT]est' --with-coverage --cover-package=cups_fab $(TEST)
