import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='aws.connect.psdb.cloud',
                                         database='database_work',
                                         user='dvt52fi4x22vvzuigz3v',
                                         password='pscale_pw_Rjk0JwWEW0qoEWn4S2zTUAHHsCvaAIldDCxiZkSI9f8')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")