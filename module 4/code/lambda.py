string = string.split()
res = filter(lambda s: s not in stop_list, string)

res = ' '.join(res)


class Indexator:

    def __init__(self, stop_words):
        self.stop_words = stop_words

    def __call__(self, string):
        return ' '.join(filter(lambda s: s not in self.stop_words, string.split()))


list_of_stop_words = ["в", "и", "по", "за", "на"]

string_to_process = ("Сервис по поиску работы и сотрудников "
                     "HeadHunter опубликовал подборку"
                     " высокооплачиваемых вакансий в России за ноябрь 2024 года"
                     "в Москве. На первых строчках IT-архитекторы и техлиды  ")
#
# string = string_to_process.split()
# res = filter(lambda s: s not in list_of_stop_words, string)
#
# res = ' '.join(res)

# print(res)

my_indexator = Indexator(list_of_stop_words)
res = my_indexator(string_to_process)

print(res)
