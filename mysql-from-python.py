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
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
        connection.commit()
    # Note that the above will still display a warning (not error) if the
    # table already exists
finally:
    # close the connection, regardless of whether the above was succesful
    connection.close()        