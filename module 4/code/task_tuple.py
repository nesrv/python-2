class Tuple(tuple):
    def __add__(self, other):
        return Tuple(tuple(self) + tuple(other))

# ------------------------------
class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))
    
# ------------------------------

class Tuple(tuple):
    def __add__(self, other):
        tuple_obj = super()
        new_tuple = tuple_obj.__add__(tuple(other))
        return self.__class__(new_tuple)

# ------------------------------


class Tuple(tuple):
    def __add__(self, other): 
        return Tuple((*self,*other))
    
# ------------------------------

class Tuple(tuple):
    def __add__(self, other):
        obj = list(self)
        for i in other:
            obj.append(i)
        return Tuple(obj)


# ------------------------------

class Tuple(tuple):
    def __add__(self, other):
        return self.__class__(tuple(self) + tuple(other))