#!/usr/bin/env python3

import subprocess
import re
import argparse

def change_mac(interface, mac_address):
    print(f"[+] Changing MAC Address for {interface} to {mac_address}")
    try:
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", mac_address], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
    except subprocess.CalledProcessError:
        print("[-] Failed to change MAC Address. Check your inputs or permissions.")

def validate_mac(mac):
    return re.match(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$", mac) is not None

def main():
    parser = argparse.ArgumentParser(description="Simple MAC Address Changer")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address (e.g., 00:11:22:33:44:55)")
    
    args = parser.parse_args()

    if not validate_mac(args.mac):
        print("[-] Invalid MAC Address format.")
        return

    change_mac(args.interface, args.mac)

if __name__ == "__main__":
    main()
