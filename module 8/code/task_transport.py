class Model(ABC):
    @abstractmethod
    def get_pk(self):
        print('get_pk')

    @staticmethod
    def get_info(self):
        return f"Базовый класс {__class__.__name__}"


class ModelForm(Model):
    x = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = ModelForm.x # id(self)
        ModelForm.x += 1
    
    def get_pk(self):
        return self._id