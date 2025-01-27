import random

your_cards = []
opponents_card = []
game_over = False

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate(cards):
    """Calculates the score for the given list of cards."""
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(score1, score2):
    """Compares the player's score with the opponent's score."""
    if score1 == score2:
        return "Draw"
    elif score2 == 0:
        return "Lose, opponent has a blackjack!"
    elif score1 == 0:
        return "Win with a blackjack!"
    elif score1 > 21:
        return "Over 21! You lose."
    elif score2 > 21:
        return "Opponent went over! You win."
    elif score1 > score2:
        return "You win!"
    else:
        return "You lose."

# Initial dealing
for _ in range(2):
    your_cards.append(deal_card())
    opponents_card.append(deal_card())

while not game_over:
    your_score = calculate(your_cards)
    opponents_score = calculate(opponents_card)

    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Opponent's first card: {opponents_card[0]}")

    if your_score == 0 or opponents_score == 0 or your_score > 21:
        game_over = True
    else:
        another = input("Draw another card? (yes/no): ").lower()
        if another == "yes":
            your_cards.append(deal_card())
        else:
            game_over = True

# Opponent's turn
while opponents_score != 0 and opponents_score < 17:
    opponents_card.append(deal_card())
    opponents_score = calculate(opponents_card)

print(f"Your final hand: {your_cards}, final score: {your_score}")
print(f"Opponent's final hand: {opponents_card}, final score: {opponents_score}")
print(compare(your_score, opponents_score))
