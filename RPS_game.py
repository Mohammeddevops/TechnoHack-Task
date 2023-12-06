import random

def print_header():
    print("****************************************")
    print("        Rock, Paper, Scissors Game       ")
    print("****************************************")

def print_choices():
    print("User choices:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def print_results(user_choice, computer_choice, result):
    print("\nResults:")
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    if result == "ties":
        print("It's a tie!")
    elif result == user_choice:
        print("You win!")
    else:
        print("Computer wins!")

def print_scores(user_score, comp_score, ties):
    print("\nScores:")
    print(f"Your score: {user_score}")
    print(f"Computer score: {comp_score}")
    print(f"Ties: {ties}")

def print_winner(user_score, comp_score):
    if user_score > comp_score:
        print("\nCongratulations! You are the overall winner!")
    elif comp_score > user_score:
        print("\nComputer is the overall winner! Better luck next time.")
    else:
        print("\nIt's a tie in the overall score. Well played!")

def print_goodbye():
    print("\nThank you for playing Rock, Paper, Scissors! Goodbye.")

def play_game():
    user_score = 0
    comp_score = 0
    ties = 0

    print_header()

    while True:
        print_choices()
        choice = int(input("Enter the number from 1-3 (or 0 to quit): "))

        if choice == 0:
            print_goodbye()
            break

        if choice < 1 or choice > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        user_choice = ["Rock", "Paper", "Scissors"][choice - 1]
        print("\nYou chose:", user_choice)

        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        print("Computer's choice:", computer_choice)

        if user_choice == computer_choice:
            result = "ties"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = user_choice
        else:
            result = "Computer"

        if result != "ties":
            print(f"\n{result} wins this round!")

        if result == user_choice:
            user_score += 1
        elif result == "Computer":
            comp_score += 1
        else:
            ties += 1

        print_scores(user_score, comp_score, ties)

        if user_score >= 5 or comp_score >= 5:
            print_winner(user_score, comp_score)
            break

if __name__ == "__main__":
    play_game()
