import threading
import tools
import datetime
import box

import controllers.motor_controller as motor_controller
import controllers.temp_controller as temp_controller



def check_temps():
    if temp_controller.get_temp_float() >= tools.get_config('goal_temp'):
        if tools.get_config('thermostat_status') == 'open':
            motor_controller.turn(-1, 0.25, 1)
            tools.write_config('thermostat_status','closed')
    else:
        if tools.get_config('thermostat_status') == 'closed':
            motor_controller.turn(1, 0.25, 1)
            tools.write_config('thermostat_status','open')



def start_timer():
    threading.Timer(60, start_timer).start()
    check_temps()
