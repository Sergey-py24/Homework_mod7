
class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        str_punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as opened:
                for line in opened:
                    line = line.lower()
                    for punc in str_punc:
                        if punc in line:
                            line = line.replace(punc, ' ')
                    split_line = line.split(sep=' ')
                    words.append(split_line)
        sorted_list = [x for y in words for x in y]
        all_words[self.file_name] = sorted_list
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        list_ = []
        for name, words in dict_.items():
            for wrd in words:
                if word.lower() in wrd:
                    index = words.index(wrd)
                    list_.append(self.file_name)
                    list_.append(index+1)
                    break
        return list_

    def count(self, word):
        dict_ = self.get_all_words()
        list_ = []
        count = 0
        for name, words in dict_.items():
            for wrd in words:
                if word.lower() in wrd:
                    count += 1
        list_.append(self.file_name)
        list_.append(count)
        return list_


finder2 = WordsFinder('testing.txt')
print(finder2.get_all_words())
print(finder2.find('НАйти'))
print(finder2.count('teXT'))

