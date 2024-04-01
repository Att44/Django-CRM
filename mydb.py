import mysql.connector

dataBase = mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'athmysql12345ATH',
)

cursorObject = dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE testdata")

print("All Done")