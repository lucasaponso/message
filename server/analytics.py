import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
	host = "sql12.freemysqlhosting.net",
	user = "sql12603798",
	password = "FH2C6SMWLs",
	database="sql12603798")

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM USERS
                               ''', mydb)

df = pd.DataFrame(sql_query, columns = ['username', 'firstname', 'lastname', 'email', 'phone_num', 'ip_addr', 'passwd'])
print (df['username'].value_counts())