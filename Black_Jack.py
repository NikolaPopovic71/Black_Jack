import random

def play_blackjack():
    # Initialize deck
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    rank_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    deck = [{'Suit': suit, 'Rank': rank} for suit in suits for rank in ranks]

    # Shuffle deck
    random.shuffle(deck)

    # Function to calculate the score of a hand
    def calculate_score(hand):
        score = 0
        ace_count = 0
        for card in hand:
            rank = card['Rank']
            if rank == 'Ace':
                score += 11
                ace_count += 1
            else:
                score += rank_values[rank]
        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1
        return score

    # Function to display a hand
    def display_hand(hand, player):
        print(f"\n{player}'s hand:")
        for card in hand:
            print(f"{card['Rank']} of {card['Suit']}")
        score = calculate_score(hand)
        print("Score:", score)
        return score

    # Deal initial cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Show initial hands
    player_score = display_hand(player_hand, "Player")
    print("\nDealer's showing:")
    print(f"{dealer_hand[1]['Rank']} of {dealer_hand[1]['Suit']}")

    # Player's turn
    while player_score < 21:
        action = input("Do you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            player_score = display_hand(player_hand, "Player")
        elif action == 's':
            break

    # Dealer's turn
    dealer_score = calculate_score(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)

    # Show dealer's hand
    display_hand(dealer_hand, "Dealer")

    # Determine winner
    if player_score > 21:
        print("You busted! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busted! You win.")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")

def main():
    while True:
        play_blackjack()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
