import string
from pprint import pprint

class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
           with (open(file_name, 'r', encoding='utf-8') as open_file):
                words_content = open_file.read().lower()

                str_punk = str.maketrans(',', ',', string.punctuation + '-')
                words_content = words_content.translate(str_punk)
                words = words_content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
                if word in words:
                    result[file_name] = words.index(word)+1
                return word, result


    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
            return result

finder2 = WordsFinder('test_file.txt', 'test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
