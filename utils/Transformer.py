import json
from classes.game.Items import Item

def create_item_and_push_it_to_database(item_json_data):
    item = Item(item_json_data["id"], item_json_data["itemType"], item_json_data["perks"],
                item_json_data["icon"], item_json_data["tier"], item_json_data["rarity"],
                item_json_data["gearScore"], item_json_data["gearScoreMin"], item_json_data["gearScoreMax"],
                item_json_data["hasRandomPerks"], item_json_data["perkBuckets"], item_json_data["name"],
                item_json_data["description"])
    item.register_in_database()

def create_ability_and_push_it_to_database(ability_json_data):
    print(ability_json_data)

def create_perk_and_push_it_to_database(perk_json_data):
    print(perk_json_data)

def read_data(response_from_extractor, loader_function):
    parsed_data_from_extractor = json.loads(response_from_extractor)
    for item in parsed_data_from_extractor["data"]:
        loader_function(item)


if __name__ == "__main__":
    pass