from pymongo import database
from connectors.mongo import connect
import logging
from random import randint

def insert_cards(cards_object: dict,
             mongo_connection) ->str:
    try:
        response = None
        for card in cards_object.get('cards'):
            response = (
                mongo_connection
                .find_one_and_update(
                    {'id': cards_object.get('user')},
                    {'$addToSet': {'cards': card}},
                    upsert = True) )
        return response
    except Exception as ex:
        logging.error(f'insert_cards:{ex}')

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
        logging.error(f'retrieve_cards_from_user:{ex}')

def retrieve_cards_by_id(cards_list, mongo_connection):
    try:
        response  = (
            mongo_connection.find({"data.multiverse_id": {'$in': cards_list}})
        )
        cards = []
        for record in response:
            name = record.get('name')
            for card in record.get('data'):
                if card.get('multiverse_id') in cards_list:
                    card['name'] = name
                    cards.append(card)
        return cards
    except Exception as ex:
        logging.error(f'retrieve_cards_by_id:{ex}')

def retrieve_random_card(cards_list, mongo_connection):
    
    if cards_list:
        response = (
            mongo_connection.find({"data.multiverse_id": {'$nin': cards_list}})
        )
    else: 
        response = (
            mongo_connection.find()
        )

    id_list = []
    for element in response:
        id_list.append(element.get('data')[0].get('multiverse_id'))
    
    return id_list[randint(0, len(id_list))]

def retrieve_all_cards(mongo_connection):
    
    response  = (
        mongo_connection.find()
    )

    cards =  []
    for element in response:
        for set in  element.get('data'):
            card_object  = {
                'name': element.get('name'),
                'set_name':  set.get('set_name'),
                'multiverse_id': set.get('multiverse_id'),
                'image_url': set.get('image_url')
            }
            cards.append(card_object)
    
    

    return cards

    