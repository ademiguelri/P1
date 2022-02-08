from opcua import Client
import time
import Control.config as config
import thermostat
import Docker.config as configDocker
from warnings import catch_warnings;
import psycopg2

CONNECTION = "postgres://"+configDocker.username+":"+configDocker.password+"@"+configDocker.host+":"+configDocker.port+"/"+configDocker.dbName
query_create_table = "CREATE TABLE therm (datetime TIMESTAMP, temp FLOAT);"
query_create_hypertable = "SELECT create_hypertable('therm', 'datetime');"
drop_table = "DROP TABLE therm;"

def start_client():
    client = Client(config.URL1)
    client.connect()
    print("Client connected")

    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

    cursor = conn.cursor()
    try:
        cursor.execute(query_create_table)
        conn.commit()
        cursor.execute(query_create_hypertable)
        conn.commit()
    except:
        cursor.execute(drop_table)
    finally:
        conn.commit()

        while True:

            Temp = client.get_node('ns=2;s="V1_Te"')
            #print(Temp.get_value())
            Time = client.get_node('ns=2;s="V1_Ti"')
            #print(Time.get_value())
            State = client.get_node('ns=2;s="V1_St"')
            #print(State.get_value())
            print("Client: "+ str(Temp.get_value()), str(Time.get_value()), str(State.get_value()))

            cursor.execute("INSERT INTO therm (datetime, temp) VALUES (current_timestamp,"+str(Temp.get_value())+")")
            conn.commit()


            if Temp.get_value() > 23.0 and State.get_value() == 'warming':
                #thermostat.thermostat.temp_max()
                config.local_temp_max = 1
                config.local_temp_min = 0
            elif Temp.get_value() < 16 and State.get_value() == 'cooling':
                #thermostat.thermostat.temp_min()
                config.local_temp_max = 0
                config.local_temp_min = 1
                
            time.sleep(2)
            
        cursor.close()