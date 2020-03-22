#!/usr/bin/env python

import serial
import time
import os
from datetime import datetime

serial_port = '/dev/ttyACM0'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)

while True:
   now = datetime.now()
   cur_path = os.getcwd() + "/log/" + now.strftime("%Y_%m_%d") + "/"
   print(cur_path)
   if not os.path.exists(cur_path):
      os.makedirs(cur_path)
   file = cur_path + "LOG_" + now.strftime("%Y_%m_%d-%I%P") + ".txt"
   print(file)
   with open(file, 'a') as f:
      line = ser.readline()
      f.writelines(str(line.decode("utf-8").rstrip("\n\r")) + "\t" + now.strftime("%Y_%m_%d-%I_%M_%S") + "\n")
   f.close()
   time.sleep(1)
