##imports
import mysql.connector
import socket
import sys, os
import random
import getpass
import public_ip as ip
import time 
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

os.system("git fetch && git pull")


##variables/global variables
SERVER_HOST = "170.187.241.20"
SERVER_PORT = 5002
separator_token = "<SEP>"
admin = "admin"
s = socket.socket()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
        Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
        Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
        Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]
client_color = random.choice(colors)

##functions
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




def MAIN():

    init()
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    t = Thread(target=listen_for_messages)
    t.daemon = True
    t.start()



    start_not = ""+username+" has joined the chat"
    exit_not = ""+username+" has left the chat"
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {admin}{separator_token}{start_not}{Fore.RESET}"
    s.send(to_send.encode())

    while True:
        to_send = getpass.getpass(prompt = "")
        if to_send.lower() == 'exit':
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"{client_color}[{date_now}] {admin}{separator_token}{exit_not}{Fore.RESET}"
            s.send(to_send.encode())
            time.sleep(3)
            START()
            break
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        to_send = f"{client_color}[{date_now}] {username}{separator_token}{to_send}{Fore.RESET}"
        s.send(to_send.encode())
    s.close()








def LOGIN():

    login_username_input = input("Username:")
    ##if username entered exists in coloumn of sql database give access
    login_password_input = getpass.getpass(prompt = "Password: ")

    if(login_username_input == "" or login_password_input == ""): 
        print("please complete required fields!!")

    else:
        global username
        vals = (login_username_input,)
        select_query = "SELECT * FROM `USERS` WHERE `username` = %s"
        mydb = mysql.connector.connect(
        host = "sql12.freemysqlhosting.net",
        user = "sql12603798",
        password = "FH2C6SMWLs",
        database="sql12603798")
        mycursor = mydb.cursor()
        mycursor.execute(select_query, vals)
        user1 = mycursor.fetchone()

        
        

        if user1 is not None:
            username = login_username_input
            MAIN()
            return True
        else:
            print("Username or Password is wrong. Or user does not exist.")
            START()
            return False


def START():
    print("1. Login\n2.Signup\n3.Help\n4.Exit")
    start_input = input("Enter Option: ")
    if (start_input == '1'):
        LOGIN()
    elif (start_input == '2'):
        SIGNUP()
    elif (start_input == '3'):
        print("TODO")
        START()
    elif (start_input == '4'):
        exit(0)
    else:
        print("invalid option choose again")
        START()



    
          

def SIGNUP():

    
    username = input("Enter your Username: ")
    global firstname
    firstname = input("Enter your First Name: ")
    global lastname
    lastname = input("Enter your Last Name:")
    global email
    email = input("Enter your email:")
    global phone_num
    phone_num = input("Enter your phone number:")
    global ip_addr
    ip_addr = ip.get()
    global passwd
    passwd = getpass.getpass(prompt = "Enter a Strong Password: ")
    
    
    USER_POST(username,firstname,lastname,email,phone_num,ip_addr,passwd)
    START()







##START()


