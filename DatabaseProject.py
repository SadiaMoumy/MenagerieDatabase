import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YU_oppdivide!20",
  database = "menagerie"
)
x = mydb.cursor()

'''
x.execute('SHOW DATABASES')

for i in x:
  print(i)
'''
'''
x.execute("SELECT * FROM pet")
structure = x.fetchall()
for record in structure:
    print(record)

    x.close()
    mydb.close()
'''
'''
x.execute("DESCRIBE pet")

# Fetch all the results
results = x.fetchall()

# Print the results
print("+------------+-------------+------+-----+---------+-------+")
print("| Field      | Type        | Null | Key | Default | Extra |")
print("+------------+-------------+------+-----+---------+-------+")

for row in results:
    
    formatted_row = "| {:<10} | {:<11} | {:<4} | {:<3} | {:<7} | {:<5} |".format(
        *(str(col) if col is not None else 'NULL' for col in row)
    )
    print(formatted_row)

print("+------------+-------------+------+-----+---------+-------+")

# Close the cursor and connection
x.close()
mydb.close()
'''
'''
x.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
structure = x.fetchall()
for record in structure:
    print(record)

    x.close()
    mydb.close()
'''
'''
x.execute("SELECT name, birth FROM pet;")
structure = x.fetchall()
for record in structure:
    print(record)

    x.close()
    mydb.close()
'''
'''
x.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner;")
structure = x.fetchall()
for record in structure:
    print(record)

    x.close()
    mydb.close()
'''

x.execute("SELECT name, birth, MONTH(birth) AS month FROM pet")

# Fetch all the results
results = x.fetchall()

# Print the results
print("+----------+------------+--------------+")
print("| name     | birth      | MONTH(birth) |")
print("+----------+------------+--------------+")

for row in results:
    print(f"| {row[0]:<8} | {row[1]} | {row[2]:>12} |")

print("+----------+------------+--------------+")

# Close the cursor and connection
x.close()
mydb.close()


