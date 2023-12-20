from itertools import permutations

def get_rank(hand):
    ranks = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
    sorted_hand = sorted(hand, key=lambda x: ranks[x[0]], reverse=True)
    counts = [sorted_hand.count(card[0]) for card in sorted_hand]
    
    if 5 in counts:
        return 9, [sorted_hand[0][0]]  # Five of a kind
    elif 4 in counts:
        return 8, [card[0] for card in sorted_hand if sorted_hand.count(card[0]) == 4]  # Four of a kind
    elif sorted(counts) == [3, 2]:
        return 7, [card[0] for card in sorted_hand if sorted_hand.count(card[0]) == 3]  # Full house
    elif 3 in counts:
        return 6, [card[0] for card in sorted_hand if sorted_hand.count(card[0]) == 3]  # Three of a kind
    elif sorted(counts) == [2, 2, 1]:
        return 5, [card[0] for card in sorted_hand if sorted_hand.count(card[0]) == 2]  # Two pair
    elif sorted(counts) == [2, 1, 1, 1]:
        return 4, [card[0] for card in sorted_hand if sorted_hand.count(card[0]) == 2]  # One pair
    else:
        return 3, [card[0] for card in sorted_hand]  # High card

def calculate_winnings(hands, bids):
    total_winnings = 0
    for bid in bids:
        hand, amount = bid.split()
        amount = int(amount)
        rank, _ = get_rank(hand)
        total_winnings += amount * rank
    return total_winnings

def main():
    # Your puzzle input goes here
    hands = ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]
    bids = ["765", "684", "28", "220", "483"]

    total_winnings = calculate_winnings(hands, bids)
    print("Total Winnings:", total_winnings)

if __name__ == "__main__":
    main()