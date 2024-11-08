
from pprint import pprint


class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_worlds = {}
        for one_file_name in self.file_names:
            open_file = open(one_file_name, 'r', encoding='utf-8')
            for world in open_file:
                all_worlds[one_file_name] = world.lower()
            open_file.close()
        return all_worlds

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
