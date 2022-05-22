import requests
import time
import sys
import os

os.system("cls")
os.system("title Tellonym Username Checker")
    
red = "\x1b[38;5;203m"
green = "\x1b[1;32m"
reset = "\x1b[0m"

valid = 0
invalid = 0
count = 0

usernames = open("usernames.txt", "r").read().splitlines()
with open("usernames.txt", "r") as f:
    usernames_count = f.read().splitlines()
usernames_found = 0
for i in usernames_count:
    usernames_found = usernames_found + 1

text = f"""
{red}┏━━┓{reset}╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋{red}┏━┳┓{reset}╋╋╋╋{red}┏┓
┗┓┏┻┳┓┏┓┏━┳━┳┳┳┳━━┓┃┏┫┗┳━┳━┫┣┳━┳┳┓
{reset}╋{red}┃┃┻┫┗┫┗┫╋┃┃┃┃┃┃┃┃┃┃┗┫┃┃┻┫━┫━┫┻┫┏┛
{reset}╋{red}┗┻━┻━┻━┻━┻┻━╋┓┣┻┻┛┗━┻┻┻━┻━┻┻┻━┻┛
{reset}╋╋╋╋╋╋╋╋╋╋╋╋╋{red}┗━┛{reset}by speezy
"""
print(text)
print(f"{reset}[{red}*{reset}]{red} Usernames Found: {reset}"+str(usernames_found)+"")
delay = float(input(f"{reset}[{red}*{reset}]{red} Delay:{reset} "))
print("")

for username in usernames:
    url = f"https://tellonym.me/{username}"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": f"__cf_bm=_{os.urandom(190).hex()}",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "naviguate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }
    
    time.sleep(delay)
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        count += 1
        invalid += 1
        print(f"{reset}[{red}-{reset}]{red} TAKEN ({reset}{username}{red}){reset} | {count}")
    elif r.status_code == 404:
        count += 1
        valid += 1
        print(f"{reset}[{green}+{reset}]{green} AVAILABLE ({reset}{username}{green}){reset} | {count}")
        with open("data/available.txt", "a") as v:
            v.write(f"{username}\n")
            
time.sleep(0.5)            
print(f"{reset}[{green}+{reset}] Finished checking | Valid(s): {green}{valid}{reset} | Invalid(s): {red}{invalid}{reset} | Total: {count}")
input("Press enter to exit")
print(f"{reset}[{red}*{reset}]{red} Thanks for using my checker!")
time.sleep(0.5)
sys.exit()