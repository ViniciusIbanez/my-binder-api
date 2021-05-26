from pymongo import database
from connectors.mongo import connect
import logging

def insert_cards(cards_object: dict,
             mongo_connection) ->str:
    try:
        for card in cards_object.get('cards'):
            response = (
                mongo_connection
                .find_one_and_update(
                    {'id': cards_object.get('user')},
                    {'$push': {'cards': card}},
                    upsert = True) )
        return response
    except Exception as ex:
        logging.error(f'MongoHelper:{ex}')

def retrieve_cards_from_user(user_id, mongo_connection):
    try:
        response  = (
            mongo_connection
            .find({'id': user_id})
        )
        cards = None
        for record in response:
            cards = record.get('cards')
        return cards
    except Exception as ex:
        logging.error(f'MongoHelper:{ex}')

def retrieve_cards_by_id(cards_list, mongo_connection):
    try:
        response  = (
            mongo_connection.find({"data.multiverse_id": {'$in': cards_list}})
        )
        cards = []
        for record in response:
            print(f'Record: {record}')
            for card in record.get('data'):
                if card.get('multiverse_id') in cards_list:
                    print(f'Adding: {card}')
                    cards.append(card)
        return cards
    except Exception as ex:
        logging.error(f'MongoHelper:{ex}')