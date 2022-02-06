#RPi Pinouts

#I2C Pins 
#GPIO2 -> SDA
#GPIO3 -> SCL

#Import the Library Requreid 
import smbus
import time
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the adress we setup in the Arduino Program
#Slave Address 1
address = 0x04

#Slave Address 2
address_2 = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte(address_2, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    # number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number
  
def send_mouvement_value(unused_addr, *args):
    data = "X {} {} Y {} {} Z {} {} ".format(*args)
    data_list = list(data)
    for i in data_list:
    	#Sends to the Slaves 
        writeNumber(int(ord(i)))
        #print(i)
        time.sleep(.001)

    writeNumber(int(0x0A))
    print("X {} {} Y {} {} Z {} {} ".format(*args))

def send_vitesse_value(unused_addr, *args):
    data = "V {}".format(args[0])
    data_list = list(data)
    for i in data_list:
    	#Sends to the Slaves 
        writeNumber(int(ord(i)))
        time.sleep(.001)

    writeNumber(int(0x0A))
    print("vitesse = {}".format(args[0]))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/mouvement", send_mouvement_value)
  dispatcher.map("/vitesse", send_vitesse_value)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()


