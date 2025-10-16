"""
File: Hacker.py
Description: This is the hacker class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# hacker.py
# The Hacker class represents a person who can buy rigs, attack others and use assets.

from Asset import Asset # Imports asset so hackers can hold assets.
from Rig import Rig     # Imports rig so hackers can own rigs.

class Hacker:
    def __init__(self, name):
        # Hacker's name (string).
        self.name = name
        # Inventory is a list of Asset objects; starts with one CryptoToken.
        self.inventory = [Asset("CryptoToken", "Used to buy or repair rigs")]
        # Initially, hacker has no rig (must acquire one).
        self.rig = None
        # Trace level measures exposure; starts at 0.
        self.trace = 0

    # -----------------------------
    # Getter and Setter Methods
    # -----------------------------
    def get_name(self):
        # Returns hacker's name.
        return self.name

    def set_name(self, new_name):
        # Changes hacker's name.
        self.name = new_name

    def get_trace(self):
        # Returns current trace level.
        return self.trace

    def set_trace(self, new_trace):
        # Sets trace level if non-negative; otherwise warns.
        if new_trace >= 0:
            self.trace = new_trace
        else:
            print("Trace cannot be negative.")

    def get_inventory(self):
        # Returns the inventory list (list of Asset objects).
        return self.inventory

    def set_inventory(self, new_inventory):
        # Replaces inventory with a new list (caller must provide Asset objects).
        self.inventory = new_inventory

    def get_rig(self):
        # Returns the hacker's rig object (or None if no rig).
        return self.rig

    def set_rig(self, new_rig):
        # Assigns a rig object to the hacker.
        self.rig = new_rig

    # -----------------------------
    # Core Methods (hacker actions)
    # -----------------------------
    def acquire_rig(self):
        # Tries to buy a rig by consuming one CryptoToken from inventory.
        for a in self.inventory:
            if a.name == "CryptoToken":
                # Removes the CryptoToken from inventory.
                self.inventory.remove(a)
                # Creates a new Rig and assigns it to this hacker.
                self.rig = Rig(self.name + "'s Rig")
                # Informs the user that the rig has been acquired.
                print(f"{self.name} has acquired a new rig!")
                return
        # No CryptoToken was found, so purchase fails.
        print(f"{self.name} has no CryptoToken to buy a rig.")

    def attack(self, target):
        # Uses one Data Spike from this hacker's rig to hit the target's rig.
        # Blocks action if attacker has no rig.
        if self.rig is None:
            print(f"{self.name} has no rig to attack from!")
            return
        # Blocks action if the attacker is too exposed (trace > 5).
        if self.trace > 5:
            print(f"{self.name} is too exposed to attack!")
            return

        # Finds a Data Spike in attacker's rig storage.
        spike = None
        for a in self.rig.storage:
            if a.name == "Data Spike":
                spike = a
                break

        # If no Data Spike is available, informs the user.
        if spike is None:
            print(f"{self.name} has no Data Spikes!")
            return

        # Consumes the Data Spike (removes from storage).
        self.rig.storage.remove(spike)
        # Announces the launch.
        print(f"{self.name} launches a Data Spike at {target.name}'s rig!")
        # Applies a hit to the target rig.
        target.rig.take_hit()
        # Increases attacker's trace by 1 for performing a risky action.
        self.trace += 1

    def extract_assets(self, target):
        # Extracts unencrypted assets from a broken target rig using a Removable Drive.
        # Blocks if attacker is too exposed.
        if self.trace > 5:
            print(f"{self.name} is too exposed to extract assets!")
            return
        # Target rig must be broken to extract assets.
        if not target.rig.broken:
            print(f"{target.name}'s rig is not broken!")
            return

        # Finds a Removable Drive in attacker's rig storage.
        drive = None
        for a in self.rig.storage:
            if a.name == "Removable Drive":
                drive = a
                break
        # If no drive available, extraction fails.
        if drive is None:
            print(f"{self.name} has no Removable Drive to extract!")
            return

        # Consumes the Removable Drive.
        self.rig.storage.remove(drive)
        print(f"{self.name} uses a Removable Drive to extract assets!")
        # Transfers any unencrypted assets from the target rig to attacker's inventory.
        for a in target.rig.storage[:]:
            if not a.encrypted:
                self.inventory.append(a)
                target.rig.storage.remove(a)
        # Increases trace more for extraction.
        self.trace += 2

    def encrypt_asset(self, asset_name):
        # Encrypts an asset in the hacker's inventory if a Security Chip is available.
        has_chip = any(a.name == "Security Chip" for a in self.inventory)
        # If no Security Chip present, prints a message and stop.
        if not has_chip:
            print(f"{self.name} has no Security Chip!")
            return
        # Finds the named asset in inventory and sets its encrypted flag.
        for a in self.inventory:
            if a.name == asset_name:
                a.encrypted = True
                print(f"{self.name} encrypted {asset_name}.")
                return
        # Asset not found in inventory.
        print(f"{asset_name} not found in inventory.")

    def decrypt_asset(self, asset_name):
        # Decrypts an asset if a Security Chip is available.
        has_chip = any(a.name == "Security Chip" for a in self.inventory)
        if not has_chip:
            print(f"{self.name} has no Security Chip!")
            return
        # Finds the named asset and clears its encrypted flag if it is encrypted.
        for a in self.inventory:
            if a.name == asset_name and a.encrypted:
                a.encrypted = False
                print(f"{self.name} decrypted {asset_name}.")
                return
        # Asset not found or not encrypted.
        print(f"{asset_name} not found or not encrypted.")

    def upgrade_rig(self):
        # Upgrades the hacker's rig using a Hardware Patch in inventory.
        # If no rig exists, informs the user.
        if self.rig is None:
            print(f"{self.name} has no rig to upgrade!")
            return
        # Looks for a Hardware Patch and consumes it to perform an upgrade.
        for a in self.inventory:
            if a.name == "Hardware Patch":
                self.inventory.remove(a)
                self.rig.upgrade()
                return
        # No Hardware Patch found.
        print(f"{self.name} has no Hardware Patch!")

    # -----------------------------------------
    # String Representation for hacker summary
    # -----------------------------------------
    def __str__(self):
        inv = [a.name for a in self.inventory]                  # list of asset names
        rig_name = self.rig.name if self.rig else "None"        # rig name or "None"
        return f"Hacker: {self.name}, Rig: {rig_name}, Trace: {self.trace}, Inventory: {inv}"
