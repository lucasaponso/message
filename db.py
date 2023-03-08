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

def USER_POST(username,firstname,lastname,email,phone_num,ip_addr,passwd):
    SQL_CRED("INSERT INTO USERS (username,firstname,lastname,email,phone_num,ip_addr,passwd) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
    ('' + username + '', '' + firstname + '', '' + lastname + '', '' + email + '', '' + phone_num + '', '' + ip_addr + '', '' + passwd))
    print("Welcome "+firstname+", to this messaging application!! Have fun!!")

def SQL_CRED(sql, val):
    mydb = mysql.connector.connect(
	host = "sql12.freemysqlhosting.net",
	user = "sql12603798",
	password = "FH2C6SMWLs",
	database="sql12603798")
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



    username = input("Enter your Username: ")
    firstname = input("Enter your First Name: ")
    lastname = input("Enter your Last Name:")
    email = input("Enter your email:")
    phone_num = input("Enter your phone number:")
    ip_addr = ip.get()
    passwd = getpass.getpass(prompt = "Enter a Strong Password: ")
   
   
    USER_POST(username,firstname,lastname,email,phone_num,ip_addr,passwd)


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
    to_send = f"{client_color}[{date_now}] {username}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())
s.close()