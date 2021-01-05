import threading
import tools
import datetime
import box

import controllers.motor_controller as motor_controller
import controllers.temp_controller as temp_controller


def check_temps():
    thermostat_status = tools.get_config('thermostat_status')
    goal_temp = tools.get_config('goal_temp')
    actual_temp = temp_controller.get_temp_float()
    if actual_temp <= goal_temp:
        offset_goal_temp = goal_temp - 0.8
    if actual_temp >= goal_temp:
        offset_goal_temp = goal_temp + 0.8

    print(f'goal_temp: {goal_temp}')
    print(f'offset_goal_temp: {offset_goal_temp}')
    print(f'actual_temp: {actual_temp}')

    if actual_temp >= offset_goal_temp:
        if thermostat_status == 'open':
            print('closing')
            motor_controller.turn(-1, 0.25, 1)
            tools.write_config('thermostat_status', 'closed')
    else:
        if thermostat_status == 'closed':
            print('opening')
            motor_controller.turn(1, 0.25, 1)
            tools.write_config('thermostat_status', 'open')


def start_timer():
    threading.Timer(60, start_timer).start()
    check_temps()
