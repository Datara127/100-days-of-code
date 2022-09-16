import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare():
    your_cards = []
    enemy_cards = []
    for _ in range(2):
        your_cards.append(deal_card())
        enemy_cards.append(deal_card())
    print(
        f"Твои карты: [{your_cards}], Сумма: {sum(your_cards)}\nКарты противника {enemy_cards}, Сумма {sum(enemy_cards)}.")
    if sum(your_cards) > 21:
        print("Перебор")
    elif sum(your_cards) == 21 and sum(enemy_cards) == 21:
        print("Ничья")
    elif sum(your_cards) == 21:
        print("Вы выиграли!")
    elif sum(enemy_cards) == 21:
        print("Вы проиграли!")
    else:
        resume_game = input(f"Если нужна карта введите 'y', а если хватит 'n'\n")
        while resume_game == "y" and sum(your_cards) < 22 and sum(enemy_cards):
            your_cards.append(deal_card())
            if sum(enemy_cards) < 16:
                enemy_cards.append(deal_card())
            resume_game = input(f"Твои карты: [{your_cards}], Сумма: {sum(your_cards)}.\n"
                                f"Карты противника {enemy_cards}, Сумма {sum(enemy_cards)}.\n"
                                f"Если нужна карта введите 'y', а если хватит 'n'\n")
        if resume_game == "n":
            while sum(enemy_cards) < 16:
                enemy_cards.append(deal_card())

        if 22 > sum(your_cards) > sum(enemy_cards) or sum(enemy_cards) >= 22 > sum(your_cards):
            print(f"Вы победили\nТвои карты: [{your_cards}], Сумма: {sum(your_cards)}\n"
                  f"Карты противника {enemy_cards}, Сумма {sum(enemy_cards)}.")
        elif sum(your_cards) == sum(enemy_cards):
            print(f"Ничья\nТвои карты: [{your_cards}], Сумма: {sum(your_cards)}\n"
                  f"Карты противника {enemy_cards}, Сумма {sum(enemy_cards)}.")
        else:
            print(f"Вы проиграли\nТвои карты: [{your_cards}], Сумма: {sum(your_cards)}\n"
                  f"Карты противника {enemy_cards}, Сумма {sum(enemy_cards)}.")

    return input("\nRestart? Write 'y' or 'n'.\n")


def main():
    start_game = input("Do you want to play a blackjack? Write 'y' or 'n'.\n")
    while start_game == "y":
        start_game = compare()


if __name__ == '__main__':
    main()
