# Домашка 1. Монеты.

from random import choice


class Coin:
    def __init__(self):
        self.side = None

    def __repr__(self):
        return f"Сторона монеты - {self.side}"

    def flip(self) -> None:
        self.side = choice(["heads", "tails"])  # random: heads/tails


try:
    n = int(input("Введите количество монет: "))
except ValueError:
    print("Нужно ввести число")
else:
    coins = [Coin() for i in range(n)]
    h_count = 0
    t_count = 0
    for coin in coins:
        coin.flip()
        if coin.side == "heads":
            h_count += 1
        elif coin.side == "tails":
            t_count += 1

    print(f"Орлов {round(h_count * 100 / n)} %, решек {round(t_count * 100 / n)} %")
