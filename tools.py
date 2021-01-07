import json
from flask import render_template


def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered


def get_config(key):
    with open('settings.json') as json_data_file:
        settings = json.load(json_data_file)
    return settings[key]


def write_config(key, value):
    with open('settings.json') as json_data_file:
        settings = json.load(json_data_file)
    settings[key] = value
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile)
    return


def config_is_set(key):
    if not get_config(key):
        return False
    else:
        return True
