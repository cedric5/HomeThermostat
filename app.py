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
import controllers.temp_controller as temp_controller

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
    direction = int(request.args.get('direction'))
    turns = float(request.args.get('turns'))
    speed = int(request.args.get('speed'))
    motor_controller.turn(direction, turns, speed)
    return f'Rotating motor: {direction} - {turns} - {speed}'

@app.route("/open")
def open():
    if tools.get_config('thermostat_status') == 'closed':
        motor_controller.turn(1, 0.5, 1)
        tools.write_config('thermostat_status', 'open')
        return 'Opend thermostat'
    else:
        return 'thermostat already open'

@app.route("/close")
def close():
    if tools.get_config('thermostat_status') == 'open':
        motor_controller.turn(-1, 0.5, 1)
        tools.write_config('thermostat_status', 'closed')
        return 'closed thermostat'
    else:
        return 'thermostat already closed'

@app.route("/temp")
def get_temp():
    return temp_controller.get_temp_string()

timer.start_timer()
