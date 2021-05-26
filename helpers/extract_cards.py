from mtgsdk import Card
from connectors.mongo import connect
import logging

def extract_set(set_code:str) -> dict:
    set_cards = Card.where(set=f'{set_code}').all()
    cards_object = {

    }
    for card in set_cards:
        if card.name not in cards_object:
            cards_object[card.name] = []

        data = {
            'set_name': card.set_name,
            'multiverse_id': card.multiverse_id,
            'image_url': card.image_url   
        }
        cards_object[card.name] = data

    return cards_object

def load_set(cards_object: dict,
             mongo_connection) ->str:
    try:
        for card_name, data in cards_object.items():
            print(data)
            response = (
                mongo_connection
                .find_one_and_update(
                    {'name': card_name},
                    {'$addToSet': {'data': data}},
                    upsert = True))
            
        return response
    except Exception as ex:
        logging.error(f'MongoHelper:{ex}')
    
