import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def lambda_handler(event, context):
    connection = mysql.connector.connect(host ='app1project1db.ce3sbej7nxkz.us-east-1.rds.amazonaws.com',
                                         database = 'employeedb',
                                         user = 'admin',
                                         password = 'Lambda#2024')
    mysql_empsql_insert_query = "INSERT IGNORE INTO employee (empid, empname, empaddress) VALUES (%s, %s, %s)"
    rows = [['300', 'arth', 'Pune'], ['400', 'Priyanka', 'Nagpur']]
    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query,rows)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into employee table")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }