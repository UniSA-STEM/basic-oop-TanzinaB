"""
File: Hacker.py
Description: This is the hacker class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Hacker.py
# The Hacker class represents a person who can buy rigs, attack others and use assets.

from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):

        #Hacker's name
        self.name = name

        #The hacker starts with one CryptoToken(used to buy rigs)
        self.inventory = [Asset("CryptoToken", "Used to buy or repair rigs")]

        #No rig at the beginning. A rig must be bought
        self.rig = None

        #Trace level measures how "exposed" the hacker is (too high = can't act)
        self.trace_level = 0

    def acquire_rig(self):
        """Buy a rig using a CryptoToken"""

        #Look for a CryptoToken in the inventory
        for a in self.inventory:
            if a.name == "CryptoToken":
                #Remove the CryptoToken from the inventory and create a rig
                self.inventory.remove(a)
                self.rig = Rig(self.name + "'s Rig")
                print(f"(self.name) has acquired a new rig!")
                return
        #If no CryptoToken is found
        print(f"(self.name) has no CryptoToken to buy a rig.")

    def attack(self, target):
        """Use a Data Spike to damage another hacker's rig."""
        if self.rig is None:
            print(f"{self.name} has no rig to attack from!")
            return

        if self.trace_level > 5:
            print(f"{self.name} is too exposed to attack!")
            return

        #Find a Data Spike(remove in storage
        spike = None
        for a in self.rig.storage:
            if a.name == "Data Spike":
                spike = a
                break

        if spike is None:
            print(f"{self.name} has no Data Spikes")
            return

        #Use the Data Spike(remove from storage)
        self.rig.storage.remove(spike)
        print(f"(self.name) launches a Data Spike at {target.name}'s rig!")

        #The target rig takes damage
        target.rig.take_hit()

        #Increase trace level slightly
        self.trace_level += 1

    def extract_assets(self, target):
        """Extract assets from a broken rig using a Removable Drive"""
        if self.trace > 5:
            print(f"{self.name} is too exposed to extract assets!")
            return

        if not target.rig.broken:
            print(f"{target.name}'s rig is not broken")
            return

        #Look for a Removable Drive
        drive = None
        for a in self.rig.storage:
            if a.name == "Removable Drive":
                drive = a
                break

        if drive is None:
            print(f"{self.name} has no Removable Drive to extract")
            return

        #Use the drive
        self.rig.storage.remove(drive)
        print(f"{self.name} uses a Removable Drive to extract assets")

        #Take all unsecured (unencrypted) assets
        for a in target.rig.storage[:]:
            if not a.encrypted:
                self.inventory.append(a)
                target.rig.storage.remove(a)

        #Trace level increases
        self.trace_level += 2

    def encrypt_asset(self, asset_name):
        """Hacker encrypts an asset if there is a Security Chip"""
        #Check if hacker has a Security Chip
        has_chip = any(a.name == "Security Chip" for a in self.inventory)
        if not has_chip:
            print(f"{self.name} has no Security Chip!")
            return

        #Find the asset to encrypt
        for a in self.inventory:
            if a.name == asset_name:
                a.encrypted = True
                print(f"{self.name} encrypted {asset_name}.")
                return
        print(f"{asset_name} not found in inventory")

    def decrypt_asset(self, asset_name):
        """Hacker decrypts an asset """
        has_chip = any(a.name == "Security Chip" for a in self.inventory)
        if not has_chip:
            print(f"{self.name} has no Security Chip!")
            return

        #Find the encrypted asset to decrypt
        for a in self.inventory:
            if a.name == asset_name and a.encrypted:
                a.encrypted = False
                print(f"{self.name} decrypted {asset_name}.")
                return

        print(f"{asset_name} not found or not encrypted.")

    def upgrade_rig(self):
        """Upgrade the rig with a Hardware Patch"""
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
        """Show the hacker's details neatly"""
        inv = [a.name for a in self.inventory]
        rig_name = self.rig.name if self.rig else "None"
        return f"Hacker: {self.name}, Rig: {rig_name}, Trace Level: {self.trace_level}, Inventory: {inv}"
