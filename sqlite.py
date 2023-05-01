#sudo apt update
#sudo apt full-upgrade
#sudo apt install sqlite3
#sqlite3 sensor.db
#create table distance (id integer primary key autoincrement, dist real)
#.tables

import RPi.GPIO as g
from time import sleep, time
import sqlite3
g.setwarnings(False)
g.setmode(g.BOARD)
conn=sqlite3.connect('sensor.db')
c=conn.cursor()
trig=5
echo=12
g.setup(trig,g.OUT,initial=g.LOW) #trig generates waveform that gets reflected and analysed by echo
g.setup(echo,g.IN)
while True:
    g.output(trig, g.HIGH) #generate waveform
    time.sleep(0.01)
    g.output(trig, g.LOW) #stop
    while g.input(echo)==0: #while echo is analysing input
        start_time=time()
    while g.input(echo)==1:
        end_time=time()
    pulse=end_time-start_time
    dist=round(pulse*17150,2)
    print(dist)
    c.execute("Insert into distance(dist) values(?)", float(dist))
    conn.commit()
    sleep(5)
