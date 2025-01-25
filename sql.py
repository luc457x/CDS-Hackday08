import psycopg2

# Define your connection parameters
conn_params = {
    'dbname': 'hackday-bookstore-cds',
    'user': 'alunocds',
    'password': 'hackday2025',
    'host': '34.55.27.249',
    'port': '5432'
}

try:
    conn = psycopg2.connect(**conn_params)
    print("Connection successful")
except Exception as e:
    print(f"Error connecting to the database: {e}")



finally:
    if conn:
        conn.close()
        print("Connection closed")
