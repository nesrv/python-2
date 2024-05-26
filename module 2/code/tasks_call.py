from random import choice, randint


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        lenPass = randint(self.min_length,  self.max_length)        
        return ''.join(choice(self.psw_chars) for _ in range(lenPass))
    


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*" 

rnd = RandomPassword(psw_chars, min_length, max_length)   
lst_pass  = [rnd() for _ in range(3)]

print(lst_pass)
print(rnd())
print(rnd())

# ---------------------------------------

from random import sample, randint

class RandomPassword:

    def __init__(self, psw_chars: str, min_length: int, max_length: int) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs) -> str:
        return "".join(sample(self.psw_chars, randint(self.min_length, self.max_length)))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for _ in range(3)]


# Фильтрация файлов

class ImageFileAcceptor:

    def __init__(self, extensions):
        self.extensions = extensions


    def __call__(self, name, *args, **kwds):
        start = name.rfind(".")
        ext = name[start+1:]
        return ext in self.extensions
    
    
# Преобразования типов

class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except ValueError:
            return None
        
        
# --------------------


class DigitRetrieve:
    def __call__(self, st, *args, **kwargs):
        if (st[1:] if st.startswith('-') else st).isdigit():
            return int(st)