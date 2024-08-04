# Домашнее задание по теме "Оператор "with".

parse_simb = [',', '.', '=', '!', '?', ';', ':', ' - ']
class WordsFinder():
    def __init__(self,*args):
        self.filenames = list(args)
        # print(self.filenames)
    def get_all_words(self):
        all_words = {}
        for file_name_ in self.filenames:
            with open(file_name_,"r",encoding='utf-8') as file:
                string_ = file.read()
                string_ = string_.lower()
                # print(string_)
                for simb in parse_simb:
                    string_ = string_.replace(simb,' ')
                    strings =  string_.split()
                # print(strings)
                all_words.update({(file_name_):strings})
        return all_words
    def find(self,word):
        for items_ in self.get_all_words().items():
            i = 0
            for word_ in items_[1]:
                i += 1
                if  word_.lower() == word.lower():
                    return {(items_[0]):i}
    def count(self, word):
        dict_ = {}
        for items_ in self.get_all_words().items():
            count_ = 0
            for word_ in items_[1]:
                if word_.lower() == word.lower():
                    count_ += 1
                dict_.update({(items_[0]):count_})
        return dict_



# finder_ = WordsFinder('product.txt','test.txt')
# print(finder_.get_all_words())
# print(finder_.find('2'))
# print(finder_.count('2'))

#  по заданию
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего