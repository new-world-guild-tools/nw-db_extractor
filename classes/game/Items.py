class Item:
    def __init__(self, id, item_type, perks, icon, tier, rarity, gear_score,
                 gear_score_min, gear_score_max, has_random_perks, perks_bucket, name, description):
        self.__id = id
        self.__item_type = item_type
        self._perks = perks
        self.__icon = icon
        self.__tier = tier
        self.__rarity = rarity
        self.__gear_score = gear_score
        self.__gear_score_min = gear_score_min
        self.__gear_score_max = gear_score_max
        self.__has_random_perks = has_random_perks
        self.__perks_bucket = perks_bucket
        self.name = name
        self.description = description


    def register_in_database(self):
        print("Item Name : " + self.name + "; Item Description : " + self.description)

