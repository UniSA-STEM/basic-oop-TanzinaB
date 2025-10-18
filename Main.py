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
unitary method worksheet
h1.acquire_rig(self)
h2.acquire_rig(self)

print(h1)
print(h2)

h1.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt"))
h1.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs"))

h1.upgrade_rig(self)
print(h1.rig)

h1.attack(h2)
h1.attack(h2)
print(h2.rig)

h1.extract_assets(h2)
print(h1)

h1.encrypt_asset("Security Chip")
h1.decrypt_asset("Security Chip")

print(h1)
print(h2)

h1.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt"))
h1.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs"))

print("\n-- Rig Upgrade --")

h1.upgrade_rig()
print(h1.rig)

print("\n -- Attack Simulation --")

h1.attack(h2)
h1.attack(h2)

print(h2.rig)

print("\n -- Extraction Attempt --")

h1.extract_assets(h2)

print(h1)

print("\n -- Encryption / Decryption Test")

h1.encrypt_asset("Security Chip")
h1.decrypt_asset("Security Chip")

print("\n -- Final Hacker States --")
print(h1)
print(h2)

h3 = Hacker("Patchless")
h3.upgrade_rig()
print()

h4 = Hacker("NoChip")
h4.acquire_rig()
h4.inventory.append(Asset("Sensitive Data", "Very secret"))

h4.encrypt_asset("Sensitive Data")
print()

h3 = Hacker("RiskTaker")
h4 = Hacker("TargetDummy")

h3.acquire_rig()
h4.acquire_rig()

h3.set_trace(6)
print(f"{h3.get_name()}'s trace level set to {h3.get_trace()} (too high!)")

h3.attack(h4)
print()

h3.set_trace(2)
print(f"Trace lowered to {h3.get_trace()}, trying again...")
h3.attack(h4)
print()

asset_test = Asset("CryptoToken", "Used for upgrades")
print("Original asset:", asset_test)
asset_test.set_encrypted(True)
print("Encrypted asset:", asset_test)
print("Getter test - is_encrypted:", asset_test.is_encrypted())
asset_test.set_name("Digital Token")
asset_test.set_description("Virtual currency for hackers")
print("Updated asset info:", asset_test.get_name(), "-", asset_test.get_description())

h1.set_trace(3)
print(f"\n{h1.get_name()}'s new trace level (via getter):", h1.get_trace())
print(f"Rig name (via getter):", h1.get_rig().get_name())