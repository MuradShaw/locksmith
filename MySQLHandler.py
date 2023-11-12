import mysql.connector

"""
    Subject to change:
    [0 UserID | 1 Username | 2 Password | 3 Email | 4 Username_HTML_Field | 5 Password_HTML_Field | 6 Email_HTML_Field | 7 URL ]
"""

class MySQLHandler:
    """
        Class for handling MySQL DB
    """

    def __init__(self):
        self.keydb = None
        self.cursor = None

    def connect_db(self, host, user, password):
        """
            Select and Connect to DB
        """

        self.keydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database="keyboard"
        )

        self.cursor = self.keydb.cursor()

    def disconnect_db(self):
        """
            Disconnect from DB
        """
        self.keydb.close()

    # Select from DB
    def select_db(self, search, table, condition_search=None, condition_type=None):
        """

        :param search: What to search for
        :param table: What table to search in
        :param condition_search: What to search for in the condition
        :param condition_type: What type to search for in the condition
        :return:
        """
        if condition_type is not None and condition_search is not None:
            self.cursor.execute(
                f"SELECT {search} FROM {table} WHERE {condition_search} = {condition_type}")
        else:
            self.cursor.execute(
                f"SELECT {search} FROM {table}")

        result = self.cursor.fetchall()
        return result

    # Insert into DB
    def insert_db(self, data, table):
        """

        :param data: Data to insert
        :param table: Table to insert into
        """
        self.cursor.execute(f"INSERT INTO {table} VALUES {data}")
        self.keydb.commit()

    # Update DB
    def update_db(self, data, search, table):
        """

        :param data: Data to update
        :param search: What to search for
        :param table: Table to update
        """
        self.cursor.execute(f"UPDATE {table} SET {search} = {data}")
        self.keydb.commit()

    # Delete from DB
    def delete_db(self, data, condition, table):
        """

        :param data: Data to delete
        :param condition: Condition to delete
        :param table: Table to delete from
        """
        self.cursor.execute(f"DELETE FROM {table} WHERE {condition} = {data}")

    # Custom command to DB
    def custom_command(self, command):
        """

        :param command: Custom command to execute
        """
        self.cursor.execute(command)
        self.keydb.commit()
