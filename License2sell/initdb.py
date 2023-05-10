import sqllite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executionscript(f.read())
  
with open('initSource.sql') as f:
  connection.executionscript(f.read())
  
connection.commit()
connection.close()
  
  
