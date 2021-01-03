import threading
import tools
import datetime
import box

import controllers.motor_controller as motor_controller
import controllers.temp_controller as temp_controller



def check_temps():
    if temp_controller.get_temp_float() >= 22:
        motor_controller.turn(-1, 0.5, 1)
    else:
        motor_controller.turn(1, 0.5, 1)


def start_timer():
    threading.Timer(600, start_timer).start()
    check_temps()
