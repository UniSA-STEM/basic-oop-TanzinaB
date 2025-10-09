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
    pass

  def attack(self, target):
    pass

  def extract_assets(self, target):
    pass

  def encrypt_asset(self, asset_name):
    pass

  def decrypt_asset(self, asset_name):
    pass

  def upgrade_rig(self):
    pass

  def __str__(self):
    inv = -----
    rig_name = self.rig.name if self.rig else "None"
    return f"Hacker: {self.name}, Rig: {rig_name}, Trace Level: {self.trace_level}, Inventory: {inv}"
