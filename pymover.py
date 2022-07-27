import shutil
import time
import os
import datetime
from configparser import ConfigParser
from discord_webhook import DiscordWebhook


cfig_file = "config.ini"
config = ConfigParser()
config.read(cfig_file)

def logo(path=''):
    print('                                                                                       ')
    print('   ▄███████▄ ▄██   ▄     ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄█    █▄     ▄████████    ▄████████ ')
    print('  ███    ███ ███   ██▄ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███    ███   ███    ███   ███    ███ ')
    print('  ███    ███ ███▄▄▄███ ███   ███   ███ ███    ███ ███    ███   ███    █▀    ███    ███ ')
    print('  ███    ███ ▀▀▀▀▀▀███ ███   ███   ███ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ')
    print('▀█████████▀  ▄██   ███ ███   ███   ███ ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ')
    print('  ███        ███   ███ ███   ███   ███ ███    ███ ███    ███   ███    █▄  ▀███████████ ')
    print('  ███        ███   ███ ███   ███   ███ ███    ███ ███    ███   ███    ███   ███    ███ ')
    print(' ▄████▀       ▀█████▀   ▀█   ███   █▀   ▀██████▀   ▀██████▀    ██████████   ███    ███ ')
    print('                                                                                       ')
logo()
def menu():
    print("[1] Run")
    print("[2] Settings")
    print("[2] Exit\n")

def clear(): 
    os.system('cls')

def main_app(r):
    
    p_timer = int(config["settings"]["sleep_timer"])
    print(p_timer)
    file_source = config["settings"]["source"]
    file_destination = config["settings"]["destination"]
    path_to_watch = file_source
    discordwebhookid = 'MTAwMTkzMTM4MTM4NDk1Nzk4Mg.G-knc8.CyqyaNl4KUAjLfIXFEWlBySu9hROgL_OIom0ko'
    now = datetime.datetime.now()

    get_source = os.listdir(file_source)
    get_destination = os.listdir(file_destination)

    print("Source: ", get_source)
    print("Local: ", get_destination)

    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]

    time.sleep(p_timer)

    if added or r:
        for g in get_source:
            if os.path.exists(file_destination+g):
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Skipped!: ", g)
            else:
                time.sleep(3)
                shutil.move(file_source + g, file_destination)
                print(now.strftime("[%Y-%m-%d %H:%M:%S]"), "Moved:", g)

                webhook = DiscordWebhook(url=(discordwebhookid), content='Moved: ' + g)
                response = webhook.execute()
    
        r = False

menu()

option = int(input("Enter your option: "))

clear()

logo()
print("Type 'exit' to return to the main menu.\n")

ans = True

f_r = True

while ans:
    if option == 1:
        main_app(f_r)
    elif option == 2:
        exit()
    else:
        print("Invalid option.")