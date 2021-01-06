import threading
import tools


import controllers.motor_controller as motor_controller
import controllers.temp_controller as temp_controller


def check_temps():
    thermostat_status = tools.get_config('thermostat_status')
    goal_temp = tools.get_config('goal_temp')
    actual_temp = temp_controller.get_temp_float()

    print(f'goal_temp: {goal_temp}')
    print(f'actual_temp: {actual_temp}')

    if actual_temp >= goal_temp:
        if thermostat_status == 'open':
            print('closing')
            motor_controller.turn(-1, 0.35, 1)
            tools.write_config('thermostat_status', 'closed')
    else:
        if thermostat_status == 'closed':
            print('opening')
            motor_controller.turn(1, 0.35, 1)
            tools.write_config('thermostat_status', 'open')


def start_timer():
    threading.Timer(60, start_timer).start()
    check_temps()
