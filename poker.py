import random

class TexasHoldem:
    def __init__(self, first_card_value, first_card_suit, second_card_value, second_card_suit):
        self.first_card_value = first_card_value
        self.first_card_suit = first_card_suit
        self.second_card_value = second_card_value
        self.second_card_suit = second_card_suit

    def pocket_info(self):
        return (f"Карты на руках: {self.first_card_value}{self.first_card_suit}, "
                f"{self.second_card_value}{self.second_card_suit}")
    def win_chance(self):
        return f"Шансы на победу: {self.calculate_win_chance()}%"
    def calculate_win_chance(self):
        total_cards = 52 #52 всего
        player_cards = 2  # 2 карты в Texas
        remaining_cards = total_cards - player_cards  # Оставшиеся карты в колоде
        winning_combinations = 0
        total_combinations = 0

        # Перебираем возможные карты, которые могут проап руку
        for _ in range(10000):  
            random_card_value = random.choice(['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'])
            random_card_suit = random.choice(['♠', '♥', '♦', '♣'])
            total_combinations += 1
            if random_card_value in [self.first_card_value, self.second_card_value]:
                winning_combinations += 1
        #вероятность
        if total_combinations > 0:
            win_chance = (winning_combinations / total_combinations) * 100
        else:
            win_chance = 0
        return round(win_chance, 2)
class OmahaHoldem(TexasHoldem):
    def __init__(self, first_card_value, first_card_suit, second_card_value, second_card_suit,
                 third_card_value, third_card_suit, forth_card_value, forth_card_suit):
        super().__init__(first_card_value, first_card_suit, second_card_value, second_card_suit)
        self.third_card_value = third_card_value
        self.third_card_suit = third_card_suit
        self.forth_card_value = forth_card_value
        self.forth_card_suit = forth_card_suit

    def pocket_info(self):
        return (super().pocket_info() + 
                f", {self.third_card_value}{self.third_card_suit}, "
                f"{self.forth_card_value}{self.forth_card_suit}")

    def win_chance(self):
        return f"Шансы на победу: {self.calculate_win_chance()}% (Omaha)"

    def calculate_win_chance(self):
        total_cards = 52 #52 карты всего
        player_cards = 4  # 4 карты в Omaha
        remaining_cards = total_cards - player_cards  # Оставшиеся карты в колоде
        winning_combinations = 0
        total_combinations = 0
        # Перебираем карты, которые могут проапгрейдить руку
        for _ in range(10000):
            random_card_value = random.choice(['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'])
            random_card_suit = random.choice(['♠', '♥', '♦', '♣'])
            total_combinations += 1
            if random_card_value in [self.first_card_value, self.second_card_value,
                                      self.third_card_value, self.forth_card_value]:
                winning_combinations += 1
        # считаю вероятность
        if total_combinations > 0:
            win_chance = (winning_combinations / total_combinations) * 100
        else:
            win_chance = 0
        return round(win_chance, 2) 
if __name__ == "__main__":
    texas_hand = TexasHoldem("5", "♠", "6", "♥")
    print(texas_hand.pocket_info())
    print(texas_hand.win_chance())
    omaha_hand = OmahaHoldem("10", "♠", "9", "♥", "Q", "♦", "J", "♣")
    print(omaha_hand.pocket_info())
    print(omaha_hand.win_chance())
