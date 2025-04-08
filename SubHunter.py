import requests
import sys
import socket
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.BLUE + """
   _____       __    __  __            __
  / ___/__  __/ /_  / / / /_  ______  / /____  _____
  \__ \/ / / / __ \/ /_/ / / / / __ \/ __/ _ \/ ___/
 ___/ / /_/ / /_/ / __  / /_/ / / / / /_/  __/ /
/____/\__,_/_.___/_/ /_/\__,_/_/ /_/\__/\___/_/

            """ + Fore.BLUE + "[ " + Fore.WHITE + "www.kirovgroup.org" + Fore.BLUE + " ]")

if len(sys.argv) < 2:
    print("\nВведите целевой поддомен ")
    print("\nкак бегать  :")
    print("   python3 SubHunter.py <domain>")
    print("\nпример :")
    print("   python3 SubHunter.py ukraine.ua")
    sys.exit(1)

API = [
    f"https://api.hackertarget.com/hostsearch/?q={sys.argv[1]}"
    f"https://otx.alienvault.com/api/v1/indicators/domain/{sys.argv[1]}/passive_dns",
]

def get_subdomains(domain):
    print(f"\n🟡 Сканирование {domain}...\n")
    subdomains = set()

    for url in API:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json() if "alienvault" in url else response.text
                if isinstance(data, dict):
                    for entry in data.get("passive_dns", []):
                        subdomains.add(entry["hostname"])
                else:
                    for line in data.split("\n"):
                        parts = line.split(",")
                        if parts:
                            subdomains.add(parts[0])
        except requests.exceptions.RequestException:
            pass

    return sorted(subdomains)

def check_live_subdomains(subdomains):
    live_data = []
    for i, sub in enumerate(subdomains, start=1):
        try:
            response = requests.get(f"http://{sub}", timeout=3)
            status = response.status_code
        except requests.exceptions.RequestException:
            status = "???"

        try:
            ip = socket.gethostbyname(sub)
        except socket.gaierror:
            ip = "N/A"

        if status == 200:
            color = Fore.GREEN
        elif status in [404, 429]:
            color = Fore.YELLOW
        else:
            color = Fore.RED

        print(f"{Fore.GREEN}[{Fore.WHITE}{i}{Fore.GREEN}]{Style.RESET_ALL} {sub} ▶ {color}{status}{Style.RESET_ALL} IP {Fore.GREEN}▶ {Fore.CYAN}{ip}")
        live_data.append(f"{sub}  ▶ {ip}")
    return live_data

target_domain = sys.argv[1]
subdomains = get_subdomains(target_domain)

if subdomains:
    print(f"\nНайденный {len(subdomains)} поддомен\n")
    clean_list = check_live_subdomains(subdomains)

    choice = input(f"\n{Fore.CYAN}[?] Сохранить в файл?? [Y/n] ").strip().lower()
    if choice in ['', 'y', 'yes']:
        filename = input("имя файла > ").strip()
        try:
            with open(filename, 'w') as f:
                for sub in clean_list:
                    f.write(sub + '\n')
            print(f"{Fore.GREEN}[✓] Результаты сохраняются в {filename}")
        except Exception as e:
            print(f"{Fore.RED}[!] Не удалось сохранить файл : {e}")
else:
    print("не могу найти поддомен ")
