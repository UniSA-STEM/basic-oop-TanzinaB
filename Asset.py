"""
File: Asset.py
Description: This is the asset class file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""

    # This class represents a digital asset
class Asset:
    def __init__(self, name, description):

    #Each asset has a name and a description#
    self.name = name
    self.description = description
    self.encrypted = False  #By default, an asset starts unencrypted#

    # This method returns the description of the asset
    # If the asset is encrypted, that is shown in the text

    def __str__(self):
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"
