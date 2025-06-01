from art import logo
from random import choice

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
cpu_cards = []

def hit_cpu():
    cpu_cards.append(choice(deck))

def hit_player():
    your_cards.append(choice(deck))

def calculate_score(cards):
    score = sum(cards)
    # Convert 11 to 1 if the score is over 21
    for i in range(cards.count(11)):
        if score > 21:
            cards[cards.index(11)] = 1
            score = sum(cards)
    return score

def show_score(pl_cards, cp_cards):
    print(f"\t Your cards: {pl_cards}, current score: {calculate_score(pl_cards)}")
    print(f"\t Computer's first card: {cp_cards[0]}")

def cpu_respond(cp_cards):
    while calculate_score(cp_cards) < 17:
        cp_cards.append(choice(deck))

def final_score(pl_cards, pl_score, cp_cards, cp_score):
    print(f"\tYour final hand: {pl_cards}, final score: {pl_score}")
    print(f"\tComputer's final hand: {cp_cards}, final score: {cp_score}")

def blackjack():
    while True:
        # reset all decks
        your_cards.clear()
        cpu_cards.clear()

        # First round of the game:
        # asking and 2-card hits on both player and cpu

        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'y':
            print(20 * "\n")
            print(logo)

            for i in range(2):
                hit_player()
                hit_cpu()

            #Calculate scores

            your_score = calculate_score(cards=your_cards)
            cpu_score = calculate_score(cards=cpu_cards)

            # Check if there is first-round blackjack from both player and cpu.
            # If not, continue with the game
            if cpu_score == 21:
                final_score(your_cards, your_score, cpu_cards, cpu_score)
                print("-" * 30)
                print("Computer wins... Blackjack!")
                continue
            elif your_score == 21 and cpu_score != 21:
                final_score(your_cards, your_score, cpu_cards, cpu_score)
                print("-" * 30)
                print("Blackjack! You win")
                continue
            else:
                show_score(your_cards, cpu_cards)
                print("-" * 30)

                # Ask whether player wants to hit
                game_over = False
                while not game_over:
                    hit = input("Type 'y' to get another card, type 'n' to pass: \n")
                    if hit == 'y':
                        hit_player()
                        # DOUBLE SHOWING WHEN PASS AFTER HIT - need to fix this
                        your_score = calculate_score(your_cards)
                        show_score(your_cards, cpu_cards)

                        if your_score == 21:
                            final_score(your_cards, your_score, cpu_cards, cpu_score)
                            print("-" * 30)
                            print("Blackjack! You win!")
                            game_over = True
                        elif your_score > 21:
                            final_score(your_cards, your_score, cpu_cards, cpu_score)
                            print("-" * 30)
                            print("Your total is higher than 21. You lose.")
                            game_over = True

                    elif hit == 'n':
                        game_over = True
                        cpu_respond(cp_cards=cpu_cards)
                        cpu_score = calculate_score(cpu_cards)
                        your_score = calculate_score(your_cards)
                        final_score(your_cards, your_score, cpu_cards, cpu_score)
                        print("-"*30)
                        if cpu_score > 21:
                            print("Computer went over 21. You win!")
                        elif cpu_score > your_score and cpu_score <= 21:
                            print("Computer wins.")
                        elif cpu_score < your_score:
                            print("You win!")
                        else:
                            print("It's a draw.")

                    else:
                        print("Invalid input. Please type 'y' or 'n'.")

        elif play == 'n':
            print(20 * "\n")
            print(logo)
            print("Goodbye")
            break
        else:
            print("\nYou typed an invalid command. \nPlease type 'y' to start or 'n' to exit the game.\n")

blackjack()
