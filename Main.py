"""
File: main.py
Description: This is the main code file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from hacker import Hacker
from asset import Asset

h1 = Hacker("NeonRaven")
h2 = Hacker("CyberWolf")

h1.acquire_rig()
h2.acquire_rig()

print(h1)
print(h2)

h1.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt"))
h1.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs"))