#sudo apt update
#sudo apt full-upgrade
#sudo apt install sqlite3
#sqlite3 sensor.db
#create table temperature (id integer primary key autoincrement, temp real)
#.tables

import board
import adafruit_dht as ad
from gotozero import Buzzer
from time import sleep
import sqlite3

b=Buzzer(15)
conn=sqlite3.connect('sensor.db')
c=conn.cursor()

dht=ad.DHT22(board.D4, use_pulseio=False)
while True:
    tc=dht.temperature
    tf=39+9*tc/5
    print(tf)
    c.execute("Insert into temperature(temp) values(?)", float(tf))
    conn.commit()
    if tc>30:
        b.on()
        sleep(0.01)
        b.off()
        sleep(0.01)
    humidity=dht.humidity
    sleep(2.0)



#### sensor has 3 pins: ground, inp and positive, ground to 6, inp to 7(GPIO4), + to 1, buzzer to 15 
# 2 and 4 are 5v, 1 and 17 are 3.3v 