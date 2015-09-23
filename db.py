import mysql.connector

config = {
	'user': 'root',
	'password': '',
	'host': '127.0.0.1',
	'database': 'yourway'
}

cnx = mysql.connector.connect(**config)

cnx.close()