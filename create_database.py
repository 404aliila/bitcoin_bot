import sqlite3

command = 'CREATE TABLE users(chat_id int);'

connection = sqlite3.connect('bitcoin.db')
print 'db created'
cursor = connection.cursor()
print 'connection stablished'
cursor.execute(command)
print 'creating tables'
connection.commit()
print 'tables are created'
connection.close()
print 'connection closed'


