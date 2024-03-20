490## 1. Подбрасывание монеты
'''
Задание:
```
1. Создайте список из n-монеток, n - вводится с клавиатуры
2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
'''

import random



class Coin:
    def __init__(self):
        self.side = None
        
    @staticmethod
    def get_coins_list():
        while True:
            try:
                number = int(input("Введите количество монет в руке\n"))
                return [Coin() for i in range(number)]
            except ValueError:
                print("Пожалуйста введите целое число\n")
        
    def flip(self) -> None:
        self.side = random.choice(['heads','tails'])
        
class CoinCounter:
    def __init__(self):
        self.dict={
            'heads': [0, 'Орел'],
            'tails': [0, 'Решка']            
        }
        self.len = 0

    def increase_counter(self,index):
        self.dict[index][0] += 1
        self.len += 1

    def get_percent(self,index):
        percent = round(((self.dict[index][0]/self.len) * 100),2)
        print(f"Процент выпадения стороны {self.dict[index][1]} : {percent} %")
    

coinList = Coin.get_coins_list()
coinCounter = CoinCounter()
for coin in coinList:
    coin.flip()
    coinCounter.increase_counter(coin.side)
    
coinCounter.get_percent('heads')
coinCounter.get_percent('tails')
 