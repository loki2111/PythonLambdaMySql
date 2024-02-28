import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host ='app1project1db.ce3sbej7nxkz.us-east-1.rds.amazonaws.com',
                                         database = 'employeedb',
                                         user = 'admin',
                                         password = 'Lambda#2024')
    mysql_empsql_insert_query = "INSERT INSERT INTO employee (empid, empname, empaddress) VALUES (%s, %s, %s)"
    # rows = [['100', 'vamsi', 'AP'], ['200', 'krishna', 'Karnataka']]
    rows=[]
    with open('empdata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(list(row.values()))

    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query,rows)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into employee table")

    sql_select_Query = "select * from employee"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Employee Table is:", cursor.rowcount)

    print("\nPrinting each employee record ")
    for row in records:
        print("empid =", row[0],)
        print("empname =", row[1])
        print("empaddress =", row[2])

except mysql.connector.Error as error:
    print("Failed to insert record into employee table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")