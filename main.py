"""
File: main.py
Description: This is the main code file
Author: Tanzina Billah
ID: 110458303
Username: bilty009
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# main.py
# Main test program for the Cyberpunk Hacker Simulation

from hacker import Hacker
from asset import Asset

# Prints a header to indicate the start of the simulation.
print("\n==========================")
print("CYBERPUNK HACKER SIMULATION START")
print("==========================")

# === Creates two hackers ===
# Instantiates Hacker object named "NeonRaven".
h1 = Hacker("NeonRaven")
# Instantiates Hacker object named "CyberWolf".
h2 = Hacker("CyberWolf")

# === Acquires rigs for each hacker ===
# NeonRaven attempts to buy a rig (consumes CryptoToken if present).
h1.acquire_rig()
# CyberWolf attempts to buy a rig.
h2.acquire_rig()

# Prints current hacker summaries.
print("\n-- Current Hackers --")
print(h1)  # Uses Hacker.__str__ to show basic status.
print(h2)

# === Gives NeonRaven some extra assets ===
# Adds a Security Chip to NeonRaven's inventory.
h1.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt"))
# Adds a Hardware Patch to NeonRaven's inventory.
h1.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs"))

# === Upgrades rig for NeonRaven ===
print("\n-- Rig Upgrade --")
# NeonRaven uses the Hardware Patch to upgrade their rig.
h1.upgrade_rig()
# Prints the rig object to show new condition/level (uses Rig.__str__).
print(h1.rig)

# === Attacks another hacker ===
print("\n-- Attack Simulation --")
# NeonRaven launches a Data Spike at CyberWolf's rig.
h1.attack(h2)
# Launches a second Data Spike.
h1.attack(h2)
# Prints CyberWolf's rig to show damage/broken status.
print(h2.rig)

# === Extracts unsecured assets if target's rig is broken ===
print("\n-- Extraction Attempt --")
# NeonRaven attempts extraction from CyberWolf's rig using a Removable Drive.
h1.extract_assets(h2)
# Prints NeonRaven's hacker summary to show inventory changes.
print(h1)

# === Encryption & Decryption ===
print("\n-- Encryption / Decryption Test --")
# NeonRaven encrypts the Security Chip in their inventory (requires Security Chip present).
h1.encrypt_asset("Security Chip")
# NeonRaven decrypts it afterward.
h1.decrypt_asset("Security Chip")

# === Shows final status of h1 and h2 ===
print("\n-- Final Hacker Status --")
print(h1)
print(h2)

# ==================================================
# EDGE CASE TESTS - variables h3 and h4
# ==================================================

print("\n==========================")
print("EDGE CASE 1: Upgrade without a rig")
print("==========================")

# Creates a hacker named Patchless who has not bought a rig.
h3 = Hacker("Patchless")
# Tries to upgrade when there is no rig: should print an error message.
h3.upgrade_rig()
print()  # blank line for readability

print("\n==========================")
print("EDGE CASE 2: Encrypt without a Security Chip")
print("==========================")

# Create a hacker named NoChip.
h4 = Hacker("NoChip")
# Optionally give NoChip a rig so the output shows rig acquisition (not required for encryption test).
h4.acquire_rig()
# Adds an asset 'Sensitive Data' to NoChip's inventory to attempt encryption.
h4.inventory.append(Asset("Sensitive Data", "Very secret"))
# Attempts to encrypt 'Sensitive Data' without having a Security Chip (should fail).
h4.encrypt_asset("Sensitive Data")
print()  # blank line for readability

print("\n==========================")
print("EDGE CASE 3: Launch attack with high trace level")
print("==========================")

# Recreates h3 and h4 as attacker/defender for clarity in this test.
h3 = Hacker("RiskTaker")
h4 = Hacker("TargetDummy")

# Both obtain rigs for the test.
h3.acquire_rig()
h4.acquire_rig()

# Artificially sets the attacker's trace above the safe threshold (use setter method).
h3.set_trace(6)  # using Hacker.set_trace to set trace to 6
# Prints the current trace via getter for confirmation.
print(f"{h3.get_name()}'s trace level set to {h3.get_trace()} (too high!)")

# Attempts an attack while trace is too high; action should be blocked.
h3.attack(h4)
print()  # blank line for readability

# Lowers trace using setter and attempts the attack again (should now succeed).
h3.set_trace(2)
print(f"Trace lowered to {h3.get_trace()}, trying again...")
h3.attack(h4)
print()  # blank line for readability

# ==================================================
# OPTIONAL: Test Getter and Setter Methods
# ==================================================

print("\n==========================")
print("TESTING GETTERS AND SETTERS")
print("==========================")

# Creates a test Asset and demonstrate getters/setters.
asset_test = Asset("CryptoToken", "Used for upgrades")
# Prints its original string form.
print("Original asset:", asset_test)
# Encrypts via setter method.
asset_test.set_encrypted(True)
# Prints the asset's string form now encrypted.
print("Encrypted asset:", asset_test)
# Uses the asset getters to show values.
print("Getter test - is_encrypted:", asset_test.is_encrypted())
# Renames and changes description via setters.
asset_test.set_name("Digital Token")
asset_test.set_description("Virtual currency for hackers")
# Prints updated name and description via getters.
print("Updated asset info:", asset_test.get_name(), "-", asset_test.get_description())

# Tests hacker/rig getters and setters as a small demo.
# Sets a new trace using setter.
h1.set_trace(3)
# Prints trace using getter.
print(f"\n{h1.get_name()}'s new trace level (via getter):", h1.get_trace())
# Prints the rig name via getter on the Rig object.
print(f"Rig name (via getter):", h1.get_rig().get_name())

# Prints footer to indicate simulation end.
print("\n==========================")
print("CYBERPUNK HACKER SIMULATION END")
print("==========================")