import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])


def main():
    n = int(input("Введите количество монеток: "))
    
    coins = [Coin() for _ in range(n)]

    for coin in coins:
        coin.flip()

    heads_count = sum(1 for coin in coins if coin.side == 'heads')
    tails_count = sum(1 for coin in coins if coin.side == 'tails')
    total_flips = len(coins)

    heads_percentage = (heads_count / total_flips) * 100
    tails_percentage = (tails_count / total_flips) * 100

    print(f"Соотношение выпавших орлов: {heads_percentage:.2f}%")
    print(f"Соотношение выпавших решек: {tails_percentage:.2f}%")


if __name__ == "__main__":
    main()