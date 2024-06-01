class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
        
    @property
    def total_weight(self):
        return sum(x for _, x in self._things)
        
    def add_thing(self, thing):
        name, weight = thing
        if self.total_weight + weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(thing)
        
class BoxDefender:
    def __init__(self, box):
        self.box = box
        self.things = box._things.copy()
        
    def __enter__(self):
        return self.box
    
    def __exit__(self, e_type, e_obj, trace):
        if e_type:
            self.box._things[:] = self.things
        return False
    
# -----------------------------------------

class Box:

    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        current_weight = [x[1] for x in self._things]
        if obj[1] + sum(current_weight) > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst):
        self._things = lst


class BoxDefender:

    def __init__(self, box):
        self._box = box
        self._things = box.things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self._things
        return False