from warnings import catch_warnings;
import psycopg2
import time
import Docker.config as config

CONNECTION = "postgres://"+config.username+":"+config.password+"@"+config.host+":"+config.port+"/"+config.dbName
query_create_table = "CREATE TABLE therm (datetime TIMESTAMP, temp FLOAT);"
query_create_hypertable = "SELECT create_hypertable('therm', 'datetime');"
drop_table = "DROP TABLE therm;"


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
        print("Sending to database: "+ str(config.TEMP))
        cursor.execute("INSERT INTO therm (datetime, temp) VALUES (current_timestamp,"+str(config.TEMP)+")")
        conn.commit()
        time.sleep(1)

    cursor.close()

