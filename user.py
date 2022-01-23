from unittest import result
from winreg import QueryInfoKey
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# GET
    @classmethod
    def get_all(cls): # function to receive data from database
        query = "SELECT * FROM users;"   # this is an id but it is also the database statement
        results = connectToMySQL("new_users").query_db(query)   # not sure what this is again
        users = []  # an empty to list to add all the data from the database
        for user in results:  # will iterate through the info received from db and add it to the empty list
            users.append(cls(user))
        return users # returns the populated list

# CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(nemail)s, NOW(), NOW());"
        return connectToMySQL("new_users").query_db(query, data)

# READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("new_users").query_db(query, data)
        return cls(results[0])

# UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email= %(nemail)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL("new_users").query_db(query, data)

# DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("new_users").query_db(query, data)