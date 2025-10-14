"""
File: Hacker.py
Description: This is the hacker class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset
from rig import Rig

class Hacker:
  def __init__(self. name):
    self.name = name
    self.inventory = [Asset("CryptoToken, "Used to buy or repair rigs")]
    self.rig = None
    self.trace_level = 0

  def acquire_rig(self):
    """Buy a rig using a CryptoToken"""
    for a in self.inventory:
        if a name == "CryptoToken":
            self.inventory.remove(a)
            self.rig = Rig(self.name)
            print(f"(self.name) has acquired a rig!")
            return
        print(f"(self.name) has no CryptoToken to buy a rig.")

  def attack(self, target):
    if self.rig is None:
        print(f"{self.name} has no rig to attack from!")
        return

    if self.trace_level > 5:
        print(f"{self.name} is too exposed to attack!")
        return

    spike = None
    for a in self.rig.inventory:
        if a.name == "Data Spike":
            spike = a
            break
        if spike is None:
            print(f"{self.name} has no Data Spikes")
            return

  def extract_assets(self, target):
    if self.trace > 5:
        print(f"{self.name} is too exposed to extract assets!")
        return

    if not target.rig.broken:
        print(f"{target.name}'s rig is not broken")
        return

  def encrypt_asset(self, asset_name):
      has_chip = any(a.name == "Security Chip" for a in self.inventory)
      if not has_chip:
          print(f"{self.name} has no Security Chip!")
          return

      for a in self.inventory:
          if a.name == asset_name:
              a.encrypted = True
              print(f"{self.name} encrypted {asset_name}.")
              return

  def decrypt_asset(self, asset_name):
      has_chip = any(a.name == "Security Chip" for a in self.inventory)
      if not has_chip:
          print(f"{self.name} has no Security Chip!")
          return

      for a in self.inventory:
          if a.name == asset_name and a.encrypted:
              a.encrypted = False
              print(f"{self.name} decrypted {asset_name}.")
              return

      print(f"{asset_name} not found or not encrypted.")

  def upgrade_rig(self):
      if self.rig is None:
          print(f"{self.name} has no rig to upgrade!")
          return

      for a in self.inventory:
          if a.name == "Hardware Patch":
              self.inventory.remove(a)
              self.rig.upgrade()
              return

      print(f"{self.name} has no Hardware Patch!")

  def __str__(self):
    inv = -----
    rig_name = self.rig.name if self.rig else "None"
    return f"Hacker: {self.name}, Rig: {rig_name}, Trace Level: {self.trace_level}, Inventory: {inv}"
