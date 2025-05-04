import pymysql
import pymysql.cursors

# 1 db connection
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1q2w3e4r',
    db = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# CRUD
cursor = connection.cursor()

sql = "SELECT * FROM customers"
cursor.execute(sql)

customers = cursor.fetchone()
print("cutomers : ", customers)
print("cutomers : ", customers['customerNumber'])
print("cutomers : ", customers['customerName'])
print("cutomers : ", customers['country'])