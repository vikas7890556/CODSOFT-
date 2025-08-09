import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("🎮 Rock-Paper-Scissors Game")
    score_player = 0
    score_computer = 0

    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
        if player_choice == "q":
            print(f"🏆 Final Score - You: {score_player} | Computer: {score_computer}")
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)
        print(result)

        if "You win" in result:
            score_player += 1
        elif "Computer wins" in result:
            score_computer += 1

        print(f"📊 Current Score - You: {score_player} | Computer: {score_computer}\n")

if __name__ == "__main__":
    main()
