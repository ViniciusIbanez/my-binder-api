from connectors.mongo import connect
import logging

def insert_user(user_info, mongo_connection):
    response = (
                mongo_connection.find_one_and_update(
                    {'user': user_info.get('user')},
                    {'$set': user_info},
                    upsert = True)
                )
    return response
