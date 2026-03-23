#Jasmine Besley
#P7
#Hackathon
import random
import pickle
import os
SAVE_FILE = "game_data.dat"

def save_game(data):
    """Saves the score dictionary to a binary file."""
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(data, f)
def load_game():
    """Loads the score dictionary; returns defaults if file doesn't exist."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            return pickle.load(f)
    return {"win": 0, "lose": 0}
def play_card_game():
    scores = load_game()
    win_score=scores['win']
    lose_score=scores['lose']
    print(f"--- Loaded Saves ---")
    print(f"Wins: {win_score} | Losses: {lose_score}\n")
    suits = ('♠', '♥', '♣', '♦')
    ranks = ('A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    rank_values = {rank: i for i, rank in enumerate(ranks)}
    while True:
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        your_card = deck.pop()
        computer_card = deck.pop()
        print('You gess the computer card is higher or lower than your card.(Ace is count as 1)')
        for i in range(1):
            print(f"\nYour card: {your_card[0]}{your_card[1]}")
            player_choice = input(f"Is it the card high or low? high/low: ")
        your_rank_value = rank_values[your_card[0]]
        computer_rank_value = rank_values[computer_card[0]]
        print(f"Your card: {your_card[0]}{your_card[1]}")
        print(f"Computer's card: {computer_card[0]}{computer_card[1]}")
        if player_choice=='high':
            if your_rank_value>computer_rank_value:
                print('You lose!')
                lose_score+=1
            if your_rank_value < computer_rank_value:
                print('You win!')
                win_score+=1
            if your_rank_value == computer_rank_value:
                 print('It\'s a tie!')
        if player_choice=='low':
            if your_rank_value<computer_rank_value:
                print('You lose!')
                lose_score +=1
            if your_rank_value > computer_rank_value:
                print('You win!')
                win_score+=1
                if your_rank_value == computer_rank_value:
                    print('It\'s a tie!')
        else:
            print("Invalid choice, please enter 'high' or 'low'.")
        print(f"Score -> Wins: {win_score} | Losses: {lose_score}")
        continue_or_not=input('Do you want to quit? (yes/no): ')
        save_game({"win": win_score, "lose": lose_score})
        if continue_or_not=='yes':
            break


if __name__ == "__main__":
    play_card_game()
