class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = [name for name in filenames]

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as fs:
                text = fs.read().lower()
                for sep in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                    text = text.replace(sep, ' ')
                all_words[filename] = text.split()

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        found = {}
        for key, value in all_words.items():
            found[key] = next((ind for ind in range(len(value)) if value[ind] == word.lower()), -1)+1
        return found

    def count(self, word):
        all_words = self.get_all_words()
        found = {}
        for key, value in all_words.items():
            found[key] = len([val for val in value if val == word.lower()])
        return found


if __name__ == '__main__':
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))

    finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    print(finder1.get_all_words())
    print(finder1.find('Child'))
    print(finder1.count('Child'))

    finder1 = WordsFinder('Rudyard Kipling - If.txt', )
    print(finder1.get_all_words())
    print(finder1.find('if'))
    print(finder1.count('if'))

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder1.get_all_words())
    print(finder1.find('captain'))
    print(finder1.count('captain'))

    #finder2 = WordsFinder('test_file.txt')
    #print(finder2.get_all_words())  # Все слова
    #print(finder2.find('TEXT'))  # 3 слово по счёту
    #print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
