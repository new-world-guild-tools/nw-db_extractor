from classes.extractors.AbilitiesExtractor import AbilitiesExtractor
from classes.extractors.ItemsExtractor import ItemsExtractor
from classes.extractors.PerksExtractor import PerksExtractor
import os
from dotenv import load_dotenv


def main():
    #item_extractor = ItemsExtractor()
    #item_extractor.extract_items()
    #ability_extractor = AbilitiesExtractor()
    #ability_extractor.extract_items()
    load_dotenv()
    MY_ENV_VAR = os.getenv('TEST')

    print(MY_ENV_VAR)
    #perk_extractor = PerksExtractor()
    #perk_extractor.extract_items()

if __name__ == '__main__':
    main()