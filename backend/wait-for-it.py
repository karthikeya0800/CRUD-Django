import time
import MySQLdb
from MySQLdb import OperationalError

def wait_for_mysql(host, user, password, database):
    while True:
        try:
            connection = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
            if connection.open:
                print("MySQL is up - executing command")
                break
        except OperationalError:
            print("MySQL is unavailable - sleeping")
            time.sleep(5)

if __name__ == "__main__":
    wait_for_mysql("mysql", "myuser", "mypassword", "crud")
