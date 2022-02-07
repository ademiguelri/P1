from opcua import Server
from random import randint
import datetime
import time
import config
import thermostat

server = Server()

server.set_endpoint(config.URL)

name = "OPCUA_SIMULATION_SERVER"
#addspace = server.register_namespace(name)
id = 'ns=2;s="V1"'

node =  server.get_objects_node()

Param = node.add_object(id, "Parameters")

Temp = Param.add_variable('ns=2;s="V1_Te"', "Temperature", 0)
Time = Param.add_variable('ns=2;s="V1_Ti"', "Time", 0)
State = Param.add_variable('ns=2;s="V1_St"', "State", 0)

Temp.set_writable()
Time.set_writable()
State.set_writable()

server.start()
print("Server started at {}".format(config.URL))

while True:
    Temperature = thermostat.thermostat.temp
    TIME = datetime.datetime.now()
    STATE = thermostat.thermostat.state

    print(Temperature, TIME)

    Temp.set_value(Temperature)
    Time.set_value(TIME)
    State.set_value(STATE)

    time.sleep(2)