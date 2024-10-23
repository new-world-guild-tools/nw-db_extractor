import json
from classes.game.Items import Item

def create_item_and_push_it_to_database(item_json_data):
    item = Item(item_json_data["id"], item_json_data["itemType"], item_json_data["perks"],
                item_json_data["icon"], item_json_data["tier"], item_json_data["rarity"],
                item_json_data["gearScore"], item_json_data["gearScoreMin"], item_json_data["gearScoreMax"],
                item_json_data["hasRandomPerks"], item_json_data["perkBuckets"], item_json_data["name"],
                item_json_data["description"])
    item.register_in_database()

def read_items_data(response_from_extractor):
    parsed_data_from_extractor = json.loads(response_from_extractor)
    for item in parsed_data_from_extractor["data"]:
        create_item_and_push_it_to_database(item)


if __name__ == "__main__":
    pass