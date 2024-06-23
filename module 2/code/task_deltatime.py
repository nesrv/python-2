from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from json import dumps

class FileReader:
    '''читаем текстовый файл, возвращаем список строк'''
    def __init__(self, filename='crm_log.txt'):
        self.filename = filename

    def read(self):
        return open(self.filename, encoding='utf-8').readlines()

class GetDeltaTime:
    '''класс функтор, получаем разницу времени'''
    def __call__(self, str_time1='0:00', str_time2='0:00', min_delta='4:00', *args, **kwargs):
        h1, m1 = map(int, str_time1.split(':'))
        h2, m2 = map(int, str_time2.split(':'))
        h_md, m_md = map(int, min_delta.split(':'))
        t1 = timedelta(hours=h1, minutes=m1)
        t2 = timedelta(hours=h2, minutes=m2)
        d = timedelta(hours=h_md, minutes=m_md)
        duration = t2 - t1
        return duration if duration > d else None

class MixinCsvFileWriter:
    '''класс-примесь (миксин). пишем в файл формата csv'''
    def __init__(self):
        pass
        
    def append_csv(self, fio, res):
        self.strings.append(f'{fio}, {res}')

class FileWriter(ABC):
    '''абстрактный класс'''
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def write(self, str_to_write):
        f = open(self.filename, 'a', encoding='utf-8')
        f.write(str_to_write)


class TxtFileWriter(FileWriter, MixinCsvFileWriter):
    '''пишем в текстовый файл'''
    def __init__(self, filename):
        super().__init__(filename)
        self.strings = []
        self.file_type = self.filename.split('.')[1]
        print(self.file_type)
    
    def append_txt(self, fio, res):
        if self.file_type.upper() == 'TXT':
            print()
            self.strings.append(f'Сотрудник: {fio} провел(а) на работе {res}')
        else:
            super().append_csv(fio, res)

    def write(self, **kwargs):
        super().write('\n'.join(self.strings))

class JsonFileWriter(FileWriter):
    '''пишем в json файл'''
    def __init__(self, filename):
        super().__init__(filename)
        self.json_strings = []
    
    def append_json(self, fio, res):
        json_data = {'fio': fio, 'time': str(res)}
        self.json_strings.append(dumps(json_data, indent=4, ensure_ascii=False))

    def write(self, **kwargs):
        super().write(',\n'.join(self.json_strings))


def main():
    reader = FileReader('crm_log.txt')
    delta = GetDeltaTime()
    writer_txt = TxtFileWriter('best_employees.txt')
    writer_csv = TxtFileWriter('best_employees.csv')
    writer_json = JsonFileWriter('best_employees.json')

    lst_users = reader.read()

    for user in lst_users:
        fio, t1, t2 = user.split(',')
        res = delta(t1, t2, '4:00')
        if res:
            writer_txt.append_txt(fio, res)
            writer_csv.append_csv(fio, res)
            writer_json.append_json(fio, res)

    writer_txt.write()
    writer_csv.write()
    writer_json.write()


main()