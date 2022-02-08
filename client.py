from opcua import Client
import time
import Control.config as config
import thermostat
import Docker.config as configDocker

def start_client():
    client = Client(config.URL1)
    client.connect()
    print("Client connected")

    while True:

        Temp = client.get_node('ns=2;s="V1_Te"')
        configDocker.TEMP = Temp.get_value()
        #print(Temp.get_value())
        Time = client.get_node('ns=2;s="V1_Ti"')
        #print(Time.get_value())
        State = client.get_node('ns=2;s="V1_St"')
        #print(State.get_value())
        print("Client: "+ str(Temp.get_value()), str(Time.get_value()), str(State.get_value()))

        if Temp.get_value() > 23.0 and State.get_value() == 'warming':
            #thermostat.thermostat.temp_max()
            config.local_temp_max = 1
            config.local_temp_min = 0
        elif Temp.get_value() < 16 and State.get_value() == 'cooling':
            #thermostat.thermostat.temp_min()
            config.local_temp_max = 0
            config.local_temp_min = 1
            
        time.sleep(2)