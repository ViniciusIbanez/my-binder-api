from mtgsdk import Card
from .connectors.mongo import connect

def extract_set(set_code:str):
    cards = Card.where(set=f'{set_Code}').all()
    final_cards = {

    }
    for card in cards:
        if card.name not in final_cards:
            final_cards[card.name] = []

        data = {
            'set_name': card.set_name,
            'multiverse_id': card.multiverse_id,
            'image_url': card.image_url   
        }
        final_cards[card.name].append(data)
    return final_cards

def load_set(set_cards,mongo_connection):
    try:
        response = mongo_connection.insert(set_cards)
        return response.
    except Exception as ex:
        logging.error(f'MongoHelper:{ex}')
    
