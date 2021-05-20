from connectors.mongo import connect
import logging

def insert_user(user_info, mongo_connection):
    response = (
                mongo_connection.insert_one(user_info))
    return response
