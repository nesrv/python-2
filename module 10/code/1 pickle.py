import pickle
 
FILENAME = "user.dat"
 
name = "Иван"
age = 20
 
with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
 
with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)



FILENAME = "users1.dat"
 
users = [
    ["Иван", 28, True],
    ["Ольга", 23, False],
    ["Борис", 34, False]
]
 
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)
 
 
with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат/замужем:", user[2])
        
        
### 


class Virus:
    def __init__(self, *args, **kwds):
        print ("я вирус")
    def __call__(self, count):
        for i in range(count):
            print (i, "я размножаюсь")

virus = Virus()


with open('pickle_virus', 'wb') as f:
    pickle.dump(virus, f)


input_file = open('pickle_virus', 'rb') 
func = pickle.load(input_file)
func(10)
    