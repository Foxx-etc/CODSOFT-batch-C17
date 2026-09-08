import random

choices = ["rock", "paper", "scissors"]

print("=" * 40)
print("     ROCK PAPER SCISSORS GAME")
print("          BEST OF 3 ROUNDS")
print("=" * 40)

while True:

    # Reset score for a new game
    user_score = 0
    computer_score = 0

    # Play 3 rounds
    for round_number in range(1, 4):

        print("\n" + "-" * 40)
        print("Round", round_number)
        print("-" * 40)

        # User choice
        user_choice = input(
            "Enter your choice (rock/paper/scissors): "
        ).lower()

        # Check valid choice
        while user_choice not in choices:
            print("Invalid choice! Please try again.")
            user_choice = input(
                "Enter rock, paper, or scissors: "
            ).lower()

        # Computer choice
        computer_choice = random.choice(choices)

        print("\nYou chose      :", user_choice)
        print("Computer chose :", computer_choice)

        # Determine winner
        if user_choice == computer_choice:
            print("Result: It's a TIE!")

        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or
            (user_choice == "paper" and computer_choice == "rock")
            or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("Result: YOU WIN!")
            user_score += 1

        else:
            print("Result: COMPUTER WINS!")
            computer_score += 1

        # Display score
        print("\nCurrent Score:")
        print("You      :", user_score)
        print("Computer :", computer_score)

    # Final result
    print("\n" + "=" * 40)
    print("          FINAL RESULT")
    print("=" * 40)

    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)

    if user_score > computer_score:
        print("\n🎉 YOU WON THE GAME!")
    elif computer_score > user_score:
        print("\n💻 COMPUTER WON THE GAME!")
    else:
        print("\n🤝 THE GAME IS A DRAW!")

    # Play again feature
    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":
        print("\nThanks for playing! Goodbye!")
        break

    print("\nStarting a new game...")


