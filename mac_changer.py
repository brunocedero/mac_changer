#!/usr/bin/env python

import subprocess


interface = input("interface >")
new_mac = input("nuevo MAC >")

print("Cambiando la direccion MAC para" + interface + " a " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
