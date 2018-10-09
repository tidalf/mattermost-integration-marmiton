# -*- coding: utf-8 -*-
import json
import logging
import random
import re
from jinja2 import Template
import codecs

try:
    from urllib.parse import urlsplit
    from urllib.parse import urlunsplit
except ImportError:
    from urlparse import urlsplit
    from urlparse import urlunsplit

import requests
from flask import Flask
from flask import Response
from flask import request, render_template

from mattermost_marmiton.settings import USERNAME, ICON_URL, RATING, SCHEME, \
    MARMITON_API_KEY, MATTERMOST_MARMITON_TOKEN

from mattermost_marmiton.marmiton import Marmiton

logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
app = Flask(__name__)


@app.route('/')
def root():
    """
    Home handler
    """

    return "OK"


@app.route('/new_post', methods=['POST'])
def new_post():
    """
    Mattermost new post event handler
    """
    try:
        # NOTE: common stuff
        slash_command = False
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        data = request.form

        if 'token' not in data:
            raise Exception('Missing necessary token in the post data')
        # disable token handling
        # !!
        #if data['token'] not in MATTERMOST_MARMITON_TOKEN:
        #    raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        # NOTE: support the slash command
        if 'command' in data:
            slash_command = True
            resp_data['response_type'] = 'in_channel'

        tpl_string = ''
        with codecs.open('recipe.tpl', encoding='utf8') as fh:
            tpl_string = fh.read()
        tpl = Template(tpl_string)
        out = tpl.render(Marmiton.get(Marmiton.search({'aqt': data['text']})[0]['url']))
        logging.log('{}'.format(out))
        resp_data['text'] = 'pffff {}'.format(out)
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp

