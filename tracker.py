import requests
import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}" + r"""
  ____  _   _     _____ ____      _    ____ _  _______ ____  
 / ___|| | | |   |_   _|  _ \    / \  / ___| |/ / ____|  _ \ 
 \___ \| |_| |_____| | | |_) |  / _ \| |   | ' /|  _| | |_) |
  ___) |  _  |_____| | |  _ <  / ___ \ |___| . \| |___|  _ < 
 |____/|_| |_|     |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\
    """)
    print(f"{Fore.YELLOW}          [+] Precision IP Tracker for beginners and experts [+]          ")
    print(f"{Fore.CYAN}               Created by: Muhammad Zeeshan Haider               \n")

def get_precise_data(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,hosting,query"
    
    try:
        print(f"{Fore.BLUE}[*] Fetching live data for {ip}...")
        time.sleep(1)
        response = requests.get(url)
        data = response.json()

        if data.get('status') == 'fail':
            print(f"{Fore.RED}[!] Error: {data.get('message', 'Invalid IP Address')}")
            input(f"\n{Fore.YELLOW}Press Enter to return...")
            return

        print(f"{Fore.GREEN}\n[#] HIGH-PRECISION REPORT [#]")
        print(f"{Fore.WHITE}="*50)
        print(f"{Fore.YELLOW}Target IP      : {Fore.CYAN}{data.get('query')}")
        print(f"{Fore.YELLOW}Hostname       : {Fore.CYAN}{data.get('reverse', 'N/A')}")
        print(f"{Fore.YELLOW}Country        : {Fore.CYAN}{data.get('country')} ({data.get('countryCode')})")
        print(f"{Fore.YELLOW}Region/City    : {Fore.CYAN}{data.get('regionName')} / {data.get('city')}")
        print(f"{Fore.YELLOW}District/Zip   : {Fore.CYAN}{data.get('district', 'N/A')} / {data.get('zip')}")
        print(f"{Fore.WHITE}-"*50)
        
        lat, lon = data.get('lat'), data.get('lon')
        print(f"{Fore.YELLOW}Latitude       : {Fore.CYAN}{lat}")
        print(f"{Fore.YELLOW}Longitude      : {Fore.CYAN}{lon}")
        print(f"{Fore.YELLOW}ISP/Org        : {Fore.CYAN}{data.get('isp')}")
        
        vpn = f"{Fore.RED}YES" if data.get('proxy') else f"{Fore.GREEN}NO"
        mob = f"{Fore.RED}YES" if data.get('mobile') else f"{Fore.GREEN}NO"
        print(f"{Fore.YELLOW}VPN/Proxy Check: {vpn}")
        print(f"{Fore.YELLOW}Mobile Data    : {mob}")
        
        print(f"{Fore.WHITE}="*50)
        print(f"{Fore.MAGENTA}[*] Map Link: https://www.google.com/maps?q={lat},{lon}")
        print(f"{Fore.WHITE}="*50)
        
        input(f"\n{Fore.YELLOW}Press Enter to return to Menu...")

    except Exception as e:
        print(f"{Fore.RED}[!] System Error: {e}")
        time.sleep(2)

def main_menu():
    while True:
        banner()
        print(f"{Fore.WHITE}[01] {Fore.GREEN}Track IP Address")
        print(f"{Fore.WHITE}[02] {Fore.RED}Exit Tool")
        print("")
        
        choice = input(f"{Fore.GREEN}┌──({Fore.CYAN}SH-Tracker{Fore.GREEN})─[{Fore.WHITE}Select-Option{Fore.GREEN}]\n└─{Fore.CYAN}$ {Fore.WHITE}")

        if choice in ['1', '01']:
            ip_input = input(f"\n{Fore.GREEN}Enter Target IP: {Fore.WHITE}")
            get_precise_data(ip_input)
        elif choice in ['2', '02']:
            print(f"\n{Fore.YELLOW}[*] Shutting down...")
            time.sleep(1)
            print(f"{Fore.CYAN}{Style.BRIGHT}\nThanks for using SH-IP-Tracker. Best of luck!\n")
            sys.exit()
        else:
            print(f"{Fore.RED}\n[!] Invalid Option!")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
