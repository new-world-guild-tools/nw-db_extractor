from classes.extractors.AbilitiesExtractor import AbilitiesExtractor
from classes.extractors.ItemsExtractor import ItemsExtractor
from classes.extractors.PerksExtractor import PerksExtractor
from utils.Loader import get_instance
from dotenv import load_dotenv


def main():
    #item_extractor = ItemsExtractor()
    #item_extractor.start_extraction()
    #ability_extractor = AbilitiesExtractor()
    #ability_extractor.start_extraction()
    #perk_extractor = PerksExtractor()
    #perk_extractor.start_extraction()
    load_dotenv()
    loader = get_instance()
    loader.connect_to_api()
if __name__ == '__main__':
    main()