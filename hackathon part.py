import random

def draw_card(rank, suit):
    val_map = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    display_val = str(val_map.get(rank, rank)).ljust(2)
    return f"[{display_val}{suit}]"

def play_war():
    suits = ['♥', '♦', '♣', '♠']
    ranks = list(range(2, 15))
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

    p1, p2 = deck[:26], deck[26:]
    round_num = 0

    print("\nGame start, shufflin deck..")

    while p1 and p2:
        round_num += 1
        
        # apparently war games go on for so long AND  end in ties so gunna make the number large
        if round_num > 2000:
            print("Game reached over 2000 rounds. Its a draw, vro.")
            return

        c1, c2 = p1.pop(0), p2.pop(0)
        table = [c1, c2]
        print(f"Round {round_num}: {draw_card(*c1)} vs {draw_card(*c2)}")

        if c1[0] > c2[0]:
            p1.extend(table)
        elif c2[0] > c1[0]:
            p2.extend(table)
        else:
            print("Initiating War.")
            war_on = True
            while war_on:
                # Need at least 2 cards to continue a war (1 face down, 1 face up)
                if len(p1) < 2 or len(p2) < 2:
                    war_on = False
                    break 
                
                table.append(p1.pop(0)) # face down
                table.append(p2.pop(0)) # face down
                
                c1_war, c2_war = p1.pop(0), p2.pop(0) # New battle
                table.extend([c1_war, c2_war])
                print(f"War Battle: {draw_card(*c1_war)} vs {draw_card(*c2_war)}")

                if c1_war[0] > c2_war[0]:
                    p1.extend(table)
                    war_on = False
                elif c2_war[0] > c1_war[0]:
                    p2.extend(table)
                    war_on = False

    if not p1 and not p2:
        print("It's a total tie. No cards left.")
    elif not p1 or not p2:
        winner = "Player 1" if p1 else "Player 2"
        insult = "Wo!" if p1 else "noob."
        print(f"\n{winner} wins in {round_num} rounds. {insult}")

if __name__ == "__main__":
    while True:
        play_war()
        print("-" * 30)
        again = input("Wanna go again? (y/n): ").lower().strip()
        
        if again != 'y':
            print("GG Then.")
            break
