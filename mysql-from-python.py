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
        list_of_names = ['george', 'George']
        # prepare a string with the same number of placeholdersas in the list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
    # Note that the above will still display a warning (not error) if the
    # table already exists
finally:
    # close the connection, regardless of whether the above was succesful
    connection.close()        