from typing import Any
from datetime import time, timedelta
import json
import csv

class FileReader:
    def __init__(self, path):
        self.file = open(path, 'r', encoding='utf-8')

    def __call__(self):
        return  list(map(lambda x: x.replace('\n', '').split(", "),
                          self.file.readlines()))
        

class GetDeltaTime:
    @staticmethod
    def get_delta(first_time, second_time):
        first_time = time.fromisoformat(first_time)
        second_time = time.fromisoformat(second_time)
        return timedelta(hours=second_time.hour - first_time.hour,
                         minutes=second_time.minute - first_time.minute)


class MixinCsvFileWriter:
    def export_to_csv(self, path, lines):
        with open(f'{path}.csv', 'w', newline='', encoding='utf-8') as f:
            f = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for item in lines:
                delta = GetDeltaTime.get_delta(item[1], item[2])
                if delta >= timedelta(hours=4):
                    f.writerow(item)


class FileWriter:
    def __call__(self):
        raise NotImplementedError("Метод не определен")


class TxtFileWriter(FileWriter, MixinCsvFileWriter):
    def __call__(self, path, lines):
        with open(f"{path}.txt", "w", encoding='utf-8') as f:
            for item in lines:
                delta = GetDeltaTime.get_delta(item[1], item[2])
                if delta >= timedelta(hours=4):
                    f.write(f"Сотрудник: {item[0]} провел(а) на работе {delta}\n")


class JsonFileWriter(FileWriter):
    def __call__(self, path, lines):
        with open(f'{path}.json', 'w', encoding='utf-8') as f:
            for item in lines:
                delta = GetDeltaTime.get_delta(item[1], item[2])
                if delta >= timedelta(hours=4):
                    data = {
                        'fio': item[0],
                        'time': str(delta)
                    }
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    f.write("\n")
                    

FR = FileReader("crm_log.txt")
TXT = TxtFileWriter()
JSON = JsonFileWriter()
lines = FR()
JSON('result', lines)
TXT('result', lines)
TXT.export_to_csv('result', lines)