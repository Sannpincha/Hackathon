import random

def get_card_value(card):
    """Calculates the value of a single card string."""
    rank = card[1:]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    return int(rank)

def calculate_score(hand):
    """Calculates total hand score, adjusting Aces from 11 to 1 if needed."""
    score = sum(get_card_value(card) for card in hand)
    aces = sum(1 for card in hand if 'A' in card)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def play_blackjack():
    # PART 2: Have Clear Rules
    print("\n" + "="*30)
    print("WELCOME TO MULTIPLAYER BLACKJACK")
    print("Rules: Beat the dealer by getting closest to 21 without busting.")
    print("Aces are 1 or 11; Face cards are 10. Dealer stands on 17.")
    print("="*30)

    # PART 4: EC - Multiple Users & Win Tracking
    player_names = []
    while True:
        try:
            num_players = int(input("How many players are joining? "))
            if num_players > 0: break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 2).")

    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ").strip()
        player_names.append(name if name else f"Player {i+1}")

    # Initialize win tracking dictionary
    win_stats = {name: 0 for name in player_names}
    win_stats["Dealer"] = 0

    # PART 4: EC - Use four decks
    base_deck = (
        '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K', '♠A',
        '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A',
        '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K', '♣A',
        '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K', '♦A'
    )
    shoe = list(base_deck) * 4
    random.shuffle(shoe)

    while True:
        player_hands = {name: [shoe.pop(), shoe.pop()] for name in player_names}
        dealer_hand = [shoe.pop(), shoe.pop()]

        # Individual player turns
        for name in player_names:
            print(f"\n--- {name.upper()}'S TURN ---")
            while True:
                score = calculate_score(player_hands[name])
                print(f"{name}'s Hand: {player_hands[name]} (Score: {score})")
                print(f"Dealer shows: {dealer_hand[0]}")

                if score >= 21: break
                
                # PART 2: Validate Inputs
                choice = input("Type 'hit' or 'stand': ").strip().lower()
                if choice == 'hit':
                    player_hands[name].append(shoe.pop())
                elif choice == 'stand':
                    break
                else:
                    print("Invalid choice! Type 'hit' or 'stand'.")

        # Dealer Turn (only if at least one player didn't bust)
        dealer_score = calculate_score(dealer_hand)
        print("\n--- DEALER'S TURN ---")
        while dealer_score < 17:
            dealer_hand.append(shoe.pop())
            dealer_score = calculate_score(dealer_hand)
        print(f"Dealer's Final Hand: {dealer_hand} (Score: {dealer_score})")

        # Determine winners and update stats
        print("\n--- ROUND RESULTS ---")
        for name in player_names:
            p_score = calculate_score(player_hands[name])
            if p_score > 21:
                print(f"{name} Busted! Dealer wins.")
                win_stats["Dealer"] += 1
            elif dealer_score > 21 or p_score > dealer_score:
                print(f"{name} wins!")
                win_stats[name] += 1
            elif p_score < dealer_score:
                print(f"Dealer beats {name}.")
                win_stats["Dealer"] += 1
            else:
                print(f"{name} pushed (tied) with Dealer.")

        # Display current win counts
        print("\n--- CURRENT SESSION WINS ---")
        for key, val in win_stats.items():
            print(f"{key}: {val}")

        # PART 2: Offer an Exit Strategy
        while True:
            choice = input("\n'play' for another round or 'menu' to exit: ").lower()
            if choice == 'play':
                break
            elif choice == 'menu':
                # Return data for the Role A Menu history log
                # We return the first player's stats as a sample for the log
                return ("Blackjack", calculate_score(player_hands[player_names[0]]), "Multi-Player Session")
            else:
                print("Error: Please enter 'play' or 'menu'.")

if __name__ == "__main__":
    play_blackjack()

