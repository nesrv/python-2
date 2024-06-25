
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod

    def check_card_number(number):
        ok = True
        for i in number.split('-'):
            if (i.isdigit() and len(i)==4) == False :
                ok = False 
        return ok

        
    @staticmethod
    def check_name(name):
        ok = True
        x = 0
        for i in name.split(' '):
            if (set(i) <= set(CardCheck.CHARS_FOR_NAME)) == False:
                ok = False
            x += 1
        return x==2 and ok

# -------------------------------------

from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_name(cls, name):
        return len(name.split()) == 2 and all(
            map(lambda x: set(x) < set(cls.CHARS_FOR_NAME), name.split())
        )

    @staticmethod
    def check_card_number(number):
        s = number.split('-')
        return len(s) == 4 and all(map(lambda x: len(x) == 4 and x.isdigit(), s))

# -------------------------------------

import re
from string import ascii_uppercase, digits
class CardCheck:
    CHARS_FOR_NAME = ascii_uppercase + digits + ' '
    @staticmethod
    def check_card_number(number):
        return re.fullmatch(r'(\d{4}-){3}\d{4}', number) != None

    @classmethod
    def check_name(cls, name):
        return len(name.split()) == 2 and all(char in cls.CHARS_FOR_NAME for char in name)
    
    


# telegram

class Telegram:
    lst = []

    @classmethod
    def add_message(cls,msg):
        cls.lst.append(msg)
    @classmethod
    def remove_message(cls,msg):
        cls.lst.remove(msg)

    @classmethod
    def set_like(cls,msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls,number):
        print (cls.lst[-number:])
    
    @classmethod
    def total_messages(cls):
        return len(cls.lst)


class Message:

    def __init__(self,text):
        self.text = text
        self.fl_like = False