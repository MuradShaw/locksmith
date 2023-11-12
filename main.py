from LockSmith import LockSmith
from MySQLHandler import MySQLHandler
from colorama import Fore
from getpass import getpass

# Continuously check for a key insert/disconnect and proceed accordingly
if __name__ == '__main__':
    lock_smith = LockSmith()
    mysql_handler = MySQLHandler()
    inserted = False

    p = "@shawww_428490"
    mysql_handler.connect_db("localhost", "key_user", p)
    mysql_handler.insert_db("(1, 'Test', 'Test')", "users")
    while True:
        if lock_smith.directory_exists(lock_smith.keydir):
            if not inserted:
                inserted = True
                lock_smith.key_inserted()
        else:
            if inserted:
                inserted = False
                print(Fore.YELLOW + "Success | Key Disconnected > Main.py")
