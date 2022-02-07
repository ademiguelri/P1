from opcua import Client
import time
import config
import thermostat

client = Client(config.URL1)

client.connect()
print("Client connected")

while True:
    Temp = client.get_node('ns=2;s="V1_Te"')
    print(Temp.get_value())

    Time = client.get_node('ns=2;s="V1_Ti"')
    print(Time.get_value())

    State = client.get_node('ns=2;s="V1_St"')
    print(State.get_value())

    if Temp > 23 and State == 'warming':
        thermostat.thermostat.temp_max()
    elif Temp < 16 and State == 'cooling':
        thermostat.thermostat.temp_min()
    time.sleep(2)