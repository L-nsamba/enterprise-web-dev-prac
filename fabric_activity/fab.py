import fabric
import datetime
from fabric import Connection

with open('fabric_activity/password.txt') as f:
    password = f.read().strip()

# Connecting to localhost as my user
connection = Connection(
    host = '127.0.0.1',
    user = 'leonnsamba',
    connect_kwargs = {'password': password}
)

time_mod = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def install_mysql():
    # Installation of mysql server
    connection.run("sudo apt-get update -y")
    connection.run("sudo apt-get install -y mysql-server")

def create_database(db_name="fabric_class_activity"):
    # Creation of database
    connection.run(f"sudo mysql -e 'CREATE DATABASE IF NOT EXISTS {db_name};'")

def load_random_sql_dump(db_name="fabric_class_activity", dump_path=r"C:\Users\nsleo\_localhost-2026_02_10_23_01_50-dump.sql"):
    # Loading AirBnb dump
    connection.run(
        f"sudo mysql {db_name} < {dump_path}"
    )

def setup_mysql():
    #Running the commands
    install_mysql()
    create_database("fabric_class_activity")
    load_random_sql_dump("fabric_class_activity", r"C:\Users\nsleo\_localhost-2026_02_10_23_01_50-dump.sql")

setup_mysql()