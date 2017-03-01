import serial
import threading

def save_raw_data():
    while 1:
        line = gps.readline()
        print line
        f = open('raw_data', 'a')
        f.write(line)
        f.close()

gps = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
save_raw_data()
gps.close()
