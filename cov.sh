#!/usr/bin/env bash

export WOLFIT_SETTINGS=$(pwd)/test.settings
export FLASK_ENV=test
export FLASK_DEBUG=0
coverage run --source "app/" --omit "app/commands.py" -m pytest
coverage html
wslview htmlcov/index.html