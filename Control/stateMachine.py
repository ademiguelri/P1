import random
from transitions import Machine

class thermostat(object):

    STATESLIST = ['start', 'warming', 'cooling', 'off']
    DEFAULT_START_TEMPERATURE = 20
    DEFAULT_TARGET_TEMPERATURE = 25

    def __init__(self, start_temperature = DEFAULT_START_TEMPERATURE, target_temperature = DEFAULT_TARGET_TEMPERATURE):
        self.machine = Machine(model=self, states=thermostat.STATESLIST, initial ='start')
        self.temp = thermostat.DEFAULT_START_TEMPERATURE
        self.target = thermostat.DEFAULT_TARGET_TEMPERATURE

        self.machine.add_transition(trigger='initialize', source='start', dest='warming')
        self.machine.add_transition(trigger='temp_max', source='warming', dest='cooling')
        self.machine.add_transition(trigger='temp_min', source='cooling', dest='warming')
        self.machine.add_transition(trigger='power_off', source='*', dest='off')


