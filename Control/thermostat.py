import stateMachine
import random
import time

def main():
    thermostat = stateMachine.thermostat()
    temp = 20
    print("---Thermostat created---")
    print("Startig state: "+ thermostat.machine.get_state(thermostat.state).name)
    while True:
            
        if thermostat.state == 'start':
            thermostat.initialize()
        elif thermostat.state == 'warming':
            thermostat.temp += random.random()
        elif thermostat.state == 'cooling':
            thermostat.temp -= random.random()
        print("Buelta")
        time.sleep(3)

if __name__ == "__main__":
   main()