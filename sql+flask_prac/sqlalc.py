from sqlalchemy import create_engine
DATABASE_URL = "jdbc:mysql://mysql-33d76eb2-alustudent-26bb.f.aivencloud.com:18954/"

engine = create_engine(DATABASE_URL)

try:
    # Attempt to establish a connection
    connection = engine.connect()
    print("Successfully connected to the MySQL database!")
    
    # You can now use the 'connection' object to execute SQL queries
    # Example:
    # result = connection.execute(text("SELECT * FROM some_table"))
    # for row in result:
    #     print(row)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed when done
    if 'connection' in locals() and connection:
        connection.close()
        print("Connection closed.")