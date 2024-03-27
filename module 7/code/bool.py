class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)

    def __bool__(self):
        return len(self) >= 1




class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return self.score > 0


lst_in = '''
Смолов; 34; 16
Дзюба; 35; 30
Жирков; 40; 2
Малафеев 45; -24
Тарасов; 37; 1
Березуцкий; 41; 0
Акинфеев 37; -95
'''

players = [Player(*i.split('; ')) for i in lst_in]
players_filtered = list(filter(bool, players))
