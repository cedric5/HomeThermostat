import datetime
import json
import os
import box
import tools as tools
import timer as timer
from flask import Flask
from flask import request
import wifi_client


import controllers.home_page as home_page_controller
import controllers.motor_controller as motor_controller

import controllers.wifi_page as wifi_page_controller
import controllers.open_close_page as open_close_page_controller
import controllers.reboot_page as reboot_page_controller
import controllers.status_page as status_page_controller

app = Flask(__name__)


def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered


@app.route("/")
def show_main_page():
    return home_page_controller.show()

@app.route("/turn")
def turn_motor():
    direction = request.args.get('direction')
    turns = request.args.get('turns')
    speed = request.args.get('speed')
    motor_controller.turn()
    return 'Rotating motor'

