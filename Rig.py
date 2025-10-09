"""
File: Rig.py
Description: This is the rig class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset

class Rig:
  def __init__(self, name):
    self.name = name
    self.damage = 0
    self.broken = False
    self.upgrade_level = 0
    self.storage = [
      Asset("Data Spike", "Used to attack other rigs"),
      Asset("Data Spike", "Used to attack other rigs"),
      Asset("Removable Drive", "Used to extract unsecured assets")
    ]
