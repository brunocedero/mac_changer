#!/usr/bin/env python

import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface", dest="interface", help="Interface para cambiar direccion MAC")
parser.parse_args("-m", "--mac", dest="new_mac", help="Nueva Direccion MAC")
args = parser.parse_args()

interface = args.interface
new_mac = args.new_mac

print("[+] Cambiando la direccion MAC para" + interface + " a " + new_mac)



subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

