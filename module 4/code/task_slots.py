
class Person:
    __slots__ = "_fio", "_old", "_job"

    def __init__(self, *args):
        self._fio, self._old, self._job = args


text = """Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель"""
persons = [*map(lambda row: Person(*row.split(', ', 2)), text.split('\n'))]


# ---------------------------------------------------
class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


lst_in = """Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Иванов, 34, программист и преподаватель
Пушкин, 32, поэт и писатель"""
persons = [Person(*x.split(", ", maxsplit=2)) for x in lst_in.splitlines()]