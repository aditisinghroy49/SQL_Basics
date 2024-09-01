import sqlite3

# Connect to an SQLite database
connection = sqlite3.connect('example.db')

cursor = connection.cursor()

# Create a Table
cursor.execute('''
Create Table If Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    age Integer,
    department text
    )
''')

# Commit the changes
connection.commit()

# Insert the data into the SQLite table
cursor.execute('''
Insert Into employees(name,age,department)
               values('Krish',32,'Data Scientist')
''')

cursor.execute('''
INSERT INTO employees (name, age, department)
VALUES ('Bob', 25, 'Engineering')
''')

cursor.execute('''
INSERT INTO employees (name, age, department)
VALUES ('Charlie', 35, 'Finance')
''')

# Commit the changes
connection.commit()

# Query the data from the table
cursor.execute('Select * from employees')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)

# Update the data in the table
cursor.execute('''
UPDATE employees
Set age=34
where name="Krish"
''')

connection.commit()

# Query the data from the table
cursor.execute('Select * from employees')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)

# Delete the data from the table
cursor.execute('''
Delete from employees
               where name ='Bob'
''')

connection.commit()

# Query the data from the table
cursor.execute('Select * from employees')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)

# Working With Sales Data
# Connect to an SQLite database
connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

# Create a table for sales data
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT
)
''')

# Insert data into the sales table
sales_data = [
    ('2023-01-01', 'Product1', 100, 'North'),
    ('2023-01-02', 'Product2', 200, 'South'),
    ('2023-01-03', 'Product1', 150, 'East'),
    ('2023-01-04', 'Product3', 250, 'West'),
    ('2023-01-05', 'Product2', 300, 'North')
]

cursor.executemany('''
Insert into sales(date,product,sales,region)
                   values(?,?,?,?)
''', sales_data)

connection.commit()

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)

# Close the connection
connection.close()
