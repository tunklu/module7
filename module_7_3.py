
from pprint import pprint


class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_worlds = dict()
        for one_file_name in self.file_names:
            open_file = open(one_file_name, 'r', encoding='utf-8')
            key = one_file_name
            for world in open_file:
                value = world.split()
                all_worlds[key] = value
                print(value)
            open_file.close()
        return all_worlds

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
