import mysql.connector
import socket
import sys, os
import random
import getpass
import public_ip as ip
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

SERVER_HOST = "170.187.241.20"
SERVER_PORT = 5002
separator_token = "<SEP>"




    




def USER_POST(first_name, last_name, phone_num, password, ipaddress_client, user_name):
    SQL_CRED("INSERT INTO users (first_name, last_name, phone_num, password, ipaddress_client, user_name) VALUES (%s, %s, %s, %s, %s, %s)", 
    ('' + first_name + '', '' + last_name + '', '' + phone_num + '', '' + password + '', '' + ipaddress_client + '', '' + user_name + ''))
    print("Welcome "+first_name+", to this messaging application!! Have fun!!")

def SQL_CRED(sql, val):
    mydb = mysql.connector.connect(
	host = "sql12.freemysqlhosting.net",
	user = "sql12601298",
	password = "PBE2mmJPax",
	database="sql12601298")
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Success")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

init()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

client_color = random.choice(colors)
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")



user_input = input("Login(L)/Signup(S):")
if (user_input == "S" or user_input == "s"):

    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name:")
    phone_num = input("Enter your phone number:")
    password = getpass.getpass(prompt = "Enter a Strong Password: ")
    ipaddress_client = ip.get()
    user_name = input("Enter your Username: ")
    USER_POST(first_name, last_name, phone_num, password, ipaddress_client, user_name)


elif (user_input == "L" or user_input == "l"):
    print("Still under construction")
    exit()


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = getpass.getpass(prompt = "")
    if to_send.lower() == 'exit':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {user_name}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())
s.close()