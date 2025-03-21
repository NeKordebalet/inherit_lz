from poker import TexasHoldem, OmahaHoldem
def main():

    texas_hand = TexasHoldem("A", "♠", "K", "♥")
    print("Texas")
    print(texas_hand.pocket_info())
    print(texas_hand.win_chance())
    omaha_hand = OmahaHoldem("A", "♠", "K", "♥", "Q", "♦", "J", "♣")
    print("Omaha")
    print(omaha_hand.pocket_info())
    print(omaha_hand.win_chance())
if __name__ == "__main__":
    main()