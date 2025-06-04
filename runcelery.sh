#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings

celery -A app.celery_worker worker --loglevel=info