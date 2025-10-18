"""
File: rig.py
Description: This is the rig class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset     # Imports the Asset class so rigs can store assets

class Rig:
    def __init__(self, name):
        # The rig's identifying name (string).
        self.name = name
        # Numeric damage counter; starts at 0.
        self.damage = 0
        # Boolean: True if rig is broken and unusable.
        self.broken = False
        # Numeric upgrade level; starts at 0 (no upgrades).
        self.upgrade_level = 0
        # Storage is a list of Asset objects; rig starts with two Data Spikes and a Removable Drive.
        self.storage = [
            Asset("Data Spike", "Used to attack other rigs"),
            Asset("Data Spike", "Used to attack other rigs"),
            Asset("Removable Drive", "Used to extract unsecured assets")
        ]

    # -----------------------------
    # Getter and Setter Methods
    # -----------------------------
    def get_name(self):
        # Returns the rig's name.
        return self.name

    def set_name(self, new_name):
        # Sets or changes the rig's name.
        self.name = new_name

    def get_damage(self):
        # Returns the current damage counter.
        return self.damage

    def set_damage(self, new_damage):
        # Sets damage if the provided value is non-negative; otherwise warn.
        if new_damage >= 0:
            self.damage = new_damage
        else:
            print("Damage cannot be negative.")

    def get_upgrade_level(self):
        # Returns the rig's upgrade level.
        return self.upgrade_level

    def set_upgrade_level(self, level):
        # Sets upgrade level if non-negative; otherwise warn.
        if level >= 0:
            self.upgrade_level = level
        else:
            print("Upgrade level must be zero or higher.")

    def is_broken(self):
        # Returns True if rig is broken, else False.
        return self.broken

    # -----------------------------
    # Core Methods (operate the rig)
    # -----------------------------
    def take_hit(self):
        # Increases damage by 1 when rig is hit.
        self.damage += 1
        # Prints the damage event for visibility in the simulation.
        print(f"{self.name} took a hit! Damage = {self.damage}")
        # Checks if damage reaches or exceeds threshold and mark rig broken.
        # Threshold = 2 + upgrade_level (higher level rigs take more hits).
        if self.damage >= 2 + self.upgrade_level:
            self.broken = True
            print(f"{self.name} is broken!")

    def repair(self):
        # Repairs the rig: if broken, reset damage and broken flag.
        if self.broken:
            self.broken = False
            self.damage = 0
            print(f"{self.name} has been repaired!")
        else:
            # If not broken, indicates no repair is needed.
            print(f"{self.name} does not need repair.")

    def upgrade(self):
        # Increases rig's upgrade level by 1 and inform the user.
        self.upgrade_level += 1
        print(f"{self.name} upgraded to Level {self.upgrade_level}!")

    def condition(self):
        # Returns a short string describing the rig's current condition and level.
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        elif self.damage == 0:
            return f"Pristine (Level {self.upgrade_level})"
        else:
            return f"Damaged ({self.damage}) (Level {self.upgrade_level})"

    # -------------------------
    # String Representation
    # -------------------------

    def __str__(self):
        # Prints the rig's name, condition, and a list of stored asset names.
        stored = [a.name for a in self.storage]  # builds a list of names
        return f"Rig: {self.name}, Condition: {self.condition()}, Storage: {stored}"
