import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.choice(["Орел", "Решка"])
    
    def __repr__(self) -> str:
        return str(self.side)

n = int(input())
coins = [Coin() for _ in range(n)]
list(map(Coin.flip, coins)) # необычное решение по подкидыванию монет
heads = len(list(filter(lambda coin: coin.side == "Орел", coins)))
tails = n - heads
print(f"Орел: {round(heads / n * 100, 2)}%") #округление с помощью f-строк более удобно
print(f"Решка: {round(tails / n * 100, 2)}%")
