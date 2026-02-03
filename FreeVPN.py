#!/usr/bin/env python3
import os
import sys
import json
import time
import requests
import random
from datetime import datetime

os.system('clear')

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def show_banner():
    print(f"""{Color.CYAN}
╔══════════════════════════════════╗
║      Free VPN GENERATOR          ║
║           Created By {Color.RED}Red{Color.CYAN}         ║
╚══════════════════════════════════╝{Color.END}
""")

def generate_vpn_key():
    api_url = "https://vpn-telegram.com/api/v1/key-activate/free-key"

    try:
        headers = {'Content-Type': 'application/json'}
        user_id = random.randint(100000000, 999999999)

        data = {
            "public_key": "b7a92b4cd1a2ced29e06059c61f624be",
            "user_tg_id": user_id
        }

        print(f"\n{Color.YELLOW}[•] Connecting to VPN server...{Color.END}")


        dots = ["   ", ".  ", ".. ", "..."]
        for i in range(12):
            print(f"\r{Color.YELLOW}[•] Processing{dots[i % 4]}{Color.END}", end='', flush=True)
            time.sleep(0.2)

        response = requests.post(api_url, json=data, headers=headers, timeout=30)

        if response.status_code == 200:
            result = response.json()

            if result.get('result'):
                return result['data']

        return None

    except:
        return None

def display_key(key_data):
    if not key_data:
        print(f"\n{Color.RED}[✗] Failed to generate key{Color.END}")
        return

    vpn_key = key_data.get('key', '')
    expiry_time = key_data.get('finish_at', 0)

    try:
        expiry_date = datetime.fromtimestamp(int(expiry_time)).strftime('%Y-%m-%d')
    except:
        expiry_date = "Unknown"

    print(f"\n{Color.GREEN}{'═' * 40}{Color.END}")
    print(f"{Color.CYAN}{' ' * 10}YOUR VPN KEY{Color.END}")
    print(f"{Color.GREEN}{'═' * 40}{Color.END}")

    print(f"\n{Color.WHITE} Key:{Color.END}")
    print(f"{Color.YELLOW}{vpn_key}{Color.END}")

    print(f"\n{Color.WHITE} Traffic:{Color.END} {Color.GREEN}5 GB{Color.END}")
    print(f"{Color.WHITE} Expires:{Color.END} {Color.YELLOW}{expiry_date}{Color.END}")

    config_url = key_data.get('config_url', '')
    if config_url:
        print(f"\n{Color.WHITE}  Config URL:{Color.END}")
        print(f"{Color.BLUE}{config_url}{Color.END}")

    print(f"\n{Color.GREEN}{'═' * 40}{Color.END}")

    print(f"\n{Color.YELLOW} To copy key:{Color.END}")
    print(f"{Color.WHITE}Long press on the key text above{Color.END}")
    print(f"{Color.WHITE}Select 'Copy' from the menu{Color.END}")

    print(f"\n{Color.CYAN}  Quick command to download config:{Color.END}")
    print(f"{Color.WHITE}curl -O {config_url}{Color.END}")

def main():
    while True:
        os.system('clear')
        show_banner()

        print(f"{Color.WHITE}[1] {Color.GREEN}Generate VPN Key{Color.END}")
        print(f"{Color.WHITE}[2] {Color.RED}Exit{Color.END}")

        print(f"\n{Color.CYAN}{'─' * 30}{Color.END}")

        choice = input(f"\n{Color.YELLOW}Select option: {Color.END}")

        if choice == '1':
            os.system('clear')
            show_banner()
            key_data = generate_vpn_key()
            display_key(key_data)

            print(f"\n{Color.CYAN}{'─' * 30}{Color.END}")
            input(f"\n{Color.WHITE}Press Enter to continue...{Color.END}")

        elif choice == '2':
            print(f"\n{Color.GREEN}Goodbye!{Color.END}\n")
            sys.exit()
        else:
            print(f"\n{Color.RED}Invalid option!{Color.END}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        try:
            import requests
        except ImportError:
            print(f"{Color.RED}Error: Please install requests module{Color.END}")
            print(f"{Color.YELLOW}Run: pip install requests{Color.END}")
            sys.exit(1)

        main()
    except KeyboardInterrupt:
        print(f"\n{Color.YELLOW}Exiting...{Color.END}")
        sys.exit()
