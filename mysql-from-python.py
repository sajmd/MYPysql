import os
import pymysql

# Get Uername from gitpod workspace
username = os.getenv('sajmd')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user= username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"                             
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection, regardless of wwhether the above was succesful
    connection.close()        