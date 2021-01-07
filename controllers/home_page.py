import tools
from flask import render_template
import controllers.temp_controller as temp_controller


def show():
    template_data = {
        'content': tools.render_page('home',
                                     {'actual_temp': temp_controller.get_temp_string(),
                                      'thermostat_status': tools.get_config('thermostat_status'),
                                      'goal_temp': tools.get_config('goal_temp'),
                                      })
    }
    return render_template('main.html', **template_data)
