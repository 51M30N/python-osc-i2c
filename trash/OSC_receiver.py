"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_vitesse_value(unused_addr, args):
    print("{}".format(args))
  
def print_mouvement_value(unused_addr, args1, args2, args3, args4, args5, args6):
  print("X {} {} Y {} {} Z {} {} ".format(args1, args2, args3, args4, args5, args6))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/mouvement", print_mouvement_value)
  dispatcher.map("/vitesse", print_vitesse_value)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()