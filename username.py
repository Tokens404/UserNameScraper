import managers.utilities as utilities
import threading
from colorama import Fore, Style, init
import os
import json
import httpx
from time import sleep
import names
init()

blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE
os.system(f'cls & mode 90,25 & title [Username Gen] - Menu')
print(f'''
{blue}
        ██▒   █▓ ▒█████   ██▓▓█████▄    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
        ▓██░   █▒▒██▒  ██▒▓██▒▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
         ▓██  █▒░▒██░  ██▒▒██▒░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
          ▒██ █░░▒██   ██░░██░░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
           ▒▀█░  ░ ████▓▒░░██░░▒████▓      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
           ░ ▐░  ░ ▒░▒░▒░ ░▓   ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
           ░ ░░    ░ ▒ ▒░  ▒ ░ ░ ▒  ▒        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
             ░░  ░ ░ ░ ▒   ▒ ░ ░ ░  ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
              ░      ░ ░   ░     ░                    ░ ░      ░ ░      ░  ░      ░                                                 
                                              
                                              
{blue}         [-] {white}Username Gen v1 By : {blue}V O ! D#6969 

''')
members = int(input("         -> Enter The Number Of Threads : "))
type = int(input("         -> 0 For Real Names And 1 For Random Usernames : "))
generatedname = 0

def GenReal():
    try:
      global generatedname
      username = names.get_full_name()
      print(Fore.GREEN + "[+] Generated - " + username)
      generatedname += 1
      os.system(f"title Astroz Username Gen v1 - Generated: {generatedname}")
      file = open("usernames.txt", 'a')
      file.write(f"{username}\n")
    except Exception as e:
      print(f"{Fore.YELLOW}{Style.BRIGHT}[-] Error: {e}{Style.RESET_ALL}")

def GenRandom():
    try:
      global generatedname
      username = json.loads(httpx.get("https://apis.kahoot.it/namerator", timeout=None).text)['name']
      print(Fore.GREEN + "[+] Generated - " + username)
      generatedname += 1
      os.system(f"title Astroz Username Gen v1 - Generated: {generatedname}")
      file = open("usernames.txt", 'a')
      file.write(f"{username}\n")
    except Exception as e:
      print(f"{Fore.YELLOW}{Style.BRIGHT}[-] Error: {e}{Style.RESET_ALL}")

while members>=0:
  if type == 0:
    threading.Thread(target=GenReal).start()
  if type == 1:
    threading.Thread(target=GenRandom).start()
