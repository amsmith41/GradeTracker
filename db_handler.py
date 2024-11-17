import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# Create a cursor object
cur = conn.cursor()

# Execute an SQL query
cur.execute("SELECT * FROM mytable;")

# Fetch the results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
cur.close()
conn.close()
