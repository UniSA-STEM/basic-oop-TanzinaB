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
def take_hit(self):
    self.damage += 1
    print(f"{self.name} took a hit! Damage = {self.damage}")

    if self.damage >= 2 + self.upgrade_level:
        self.broken = True
        print(f"{self.name} is broken!")

def repair(self):
    if self.broken:
        self.broken = False
        self.damage = 0
        print(f"{self.name} has been repaired!")
    else:
        print(f"{self.name} does not need repair.")

def upgrade(self):
    self.upgrade_level += 1
    print(f"{self.name} upgraded to Level {self.upgrade_level}!")

def condition(self):
    if self.broken:
        return f"Broken (Level {self.upgrade_level})"
    elif self.damage == 0:
        return f"Pristine (Level {self.upgrade_level})"
    else:
        return f"Damaged ({self.damage}) (Level {self.upgrade_level})"

def __str__(self):
  stored = -----
  return f"Rig: {self.name}, Condition: {self.condition())}. Storage: {stored}"
