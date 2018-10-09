#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from mattermost_marmiton.app import app
from mattermost_marmiton.settings import MARMITON_API_KEY, MATTERMOST_MARMITON_TOKEN


if __name__ == "__main__":
    if not MARMITON_API_KEY:
        print("MARMITON_API_KEY must be configured. Please see README.md for instructions")
        sys.exit()

    if not MATTERMOST_MARMITON_TOKEN:
        print("MATTERMOST_MARMITON_TOKEN must be configured. Please see README.md for instructions")
        sys.exit()

    port = os.environ.get('MATTERMOST_MARMITON_PORT', None) or os.environ.get('PORT', 5000)
    host = os.environ.get('MATTERMOST_MARMITON_HOST', None) or os.environ.get('HOST', '0.0.0.0')
    app.run(host=str(host), port=int(port))
