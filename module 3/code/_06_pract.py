# 1

# filename = input()
# lines, words, symbols = 0, 0, 0
# with open(filename, 'r', encoding='utf-8') as file:
#     for i in file:
#         lines += 1
#         words += len([w for w in i.split() if w.isalpha()])
#         symbols += len([s for s in i if s.isalnum()])
# print(f'Количество строк в файле {filename}: {lines}\n'
#       f'Количество слов: {words}\n'
#       f'Число символов: {symbols}\n'
#      )
import json

json_obj = '["Hello", 179, 0.5, true, null, [1, 2, 3], {"key": "value"}]'


# json_loads = json.loads(json_obj)
#
# print(json_loads)


class JsonEditor:

    def __init__(self, js_obj):
        self.js_loads = json.loads(json_obj)

    def edit(self):
        new_json = []
        for item in self.js_loads:
            if type(item) == str:
                new_json.append(f'{item}!')
            elif type(item) == int:
                new_json.append(item + 1)
            elif type(item) == bool:
                new_json.append(not item)
            elif type(item) == list:
                new_json.append(item * 2)
            elif type(item) == dict:
                item['newkey'] = None
                new_json.append(item)
        return json.dumps(new_json, indent=4)


res = JsonEditor(json_obj)

print(res.edit())


class JsonEditor:

    def __init__(self, js_obj):
        self.js_loads = json.loads(json_obj)
        self.js_obj = []

    def __edit(self):
        for item in self.js_loads:
            if type(item) == str:
                self.js_obj.append(f'{item}!')
            elif type(item) == int:
                self.js_obj.append(item + 1)
            elif type(item) == bool:
                self.js_obj.append(not item)
            elif type(item) == list:
                self.js_obj.append(item * 2)
            elif type(item) == dict:
                item['newkey'] = None
                self.js_obj.append(item)

    def get_json(self):
        self.__edit()
        return json.dumps(self.js_obj, indent=4)


res = JsonEditor(json_obj)

print(res.get_json())


# ===============================================================

f = open('.txt.txt', encoding="utf-8")


class FileReader:

    def __init__(self, filename):
        self.__text = open(filename, encoding="utf-8").readlines()

    @property
    def text(self):
        return self.__text

    # def get_text(self):
    #     return self.text


class Counter:

    def __init__(self, txt):
        self.txt = txt

    def get_lines(self):
        return len(self.txt)

    def get_words(self):
        words = 0
        for row in self.txt:
            words += len([w for w in row.split() if w.isalpha()])
        return words

    def get_symblols(self):
        symbols = 0
        for row in self.txt:
            symbols += len([s for s in row if s.isalnum()])
        return symbols


txt_reader = FileReader('txt.txt')
# txt = txt_reader.get_text()
txt = txt_reader.text
print(txt)
my_counter = Counter(txt)
print(my_counter.get_lines())
print(my_counter.get_words())
print(my_counter.get_symblols())
