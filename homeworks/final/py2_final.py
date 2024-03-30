payment_systems = {
        "2": "Мир",
        "30": "Diners Club",
        "36": "Diners Club",
        "38": "Diners Club",
        "31": "JCB International",
        "34": "American Express",
        "37": "American Express",
        "4": "VISA",
        "50": "Maestro",
        "56": "Maestro",
        "57": "Maestro",
        "58": "Maestro",
        "51": "MasterCard",
        "52": "MasterCard",
        "53": "MasterCard",
        "54": "MasterCard",
        "55": "MasterCard",
        "60": "Discover",
        "62": "China UnionPay",
        "63": "Maestro",
        "67": "Maestro",
        "7": "УЭК (Универсальная электронная карта)"
    }


def Luhn(card_number_str):
    card_number_list = list(card_number_str)
    card_number_list.reverse()
    for i in range(len(card_number_list)):
        d = int(card_number_list[i])
        if i % 2 != 0:
            d *= 2
            if d > 9:
                d = d // 10 + d % 10
        card_number_list[i] = d
    if sum(card_number_list) % 10 == 0:
        return True
    return False

def pay_sys_chk(card_number_str):
    for key, value in payment_systems.items():
        if str(card_number_str).startswith(key):
            return value
    return "Неизвестнгая платежная система"


def main():
    cards_list = []
    while True:
        name = input("Введите имя и фамилию: ")
        num = input("Введите номер карты: ")

        if name.upper() == 'SHOW' or num.upper() == 'SHOW':
            for i in range(len(cards_list)):
                print(f"{cards_list[i][0]:<35}{cards_list[i][1][:4]} {cards_list[i][1][4:8]} {cards_list[i][1][8:12]} {cards_list[i][1][12:]}     {pay_sys_chk(cards_list[i][1])}")
        elif name.upper() == 'STOP' or num.upper() == 'STOP':
            return
        else:
            if Luhn(num):
                cards_list.append((name, num))
            else:
                print("Номер карты введен неверно")


main()