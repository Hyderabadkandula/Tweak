import mysql.connector
import pandas as pd

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='chirakuu@18',
        database='python'
    )
    if con.is_connected():
        print('connected successfully')

    cursor=con.cursor()
    query = "SELECT * FROM students;"

    # query='insert into students(sid,sfirst_name,slast_name,saddress) values(%s,%s,%s,%s)'
    # data=[(101,'Sri','Devi','AAA'),(102,'Nandu','Priya','BBB'),(103,'Pinky','Kavya','CCC')]

    # cursor.executemany(query,data)
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    con.commit()

    print(f"{cursor.rowcount} record inserted, ID:{cursor.lastrowid}")

    df = pd.DataFrame(result, columns=columns)
    df.to_excel("students_data_mysql.xlsx", index=False)
    print("Data saved to Excel successfully!")

except mysql.connector.Error as err:
    print(f"Error:{err}")
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySQL connection is closed.")