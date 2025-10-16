"""
File: Asset.py
Description: This is the asset class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# asset.py
# Represents a digital asset in the hacker simulation.

class Asset:
    def __init__(self, name, description):
        # Sets the visible name for this asset(string)
        self.name = name
        # Sets the description for this asset(string)
        self.description = description
        #Boolean flag: True when asset is encrypted, False otherwise
        self.encrypted = False

    # ---------------------------
    # Getter amd Setter Methods
    # ---------------------------

    def get_name(self):
        # Returns the asset's name.
        return  self.name

    def set_name(self, new_name):
        # Changes the asset's name to new_name.
        self.name = new_name

    def get_description(self):
        # Returns the asset's description.
        return self.description

    def set_description(self, new_description):
        # Changes the asset's description to new_description.
        self.description = new_description

    def is_encrypted(self):
        # Returns True if encrypted, else False.
        return self.encrypted

    def set_encrypted(self, status):
        # Sets encryption status to True/False, validating the input.
        if isinstance(status, bool):
            self.encrypted = status
        else:
            # If someone passes a non-boolean, prints a helpful message.
            print("Encryption status must be True or False.")

    # -----------------------------
    # String Representation
    # -----------------------------
    def __str__(self):
        # Returns a human-readable string for printing the asset.
        # Includes "[Encrypted]" if the asset is encrypted.
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"
