import random

def show_score(attempts_list):
    if not attempts_list:
        print("No high score yet. Be the first to set one!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

def get_valid_guess():
    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("❌ Please enter a number within the range 1 to 10.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def play_game(player_name, attempts_list):
    rand_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = get_valid_guess()
        attempts += 1

        if guess == rand_number:
            print(f"🎉 Congratulations, {player_name}! You guessed the number in {attempts} attempts.")
            attempts_list.append(attempts)
            break
        elif guess > rand_number:
            print("🔻 Too high, try again!")
        else:
            print("🔺 Too low, try again!")

def main():
    print("🎮 Welcome to the Number Guessing Game!")
    player_name = input("What's your name? ").strip()

    if not player_name:
        player_name = "Player"

    wanna_play = input(f"Hello, {player_name}! Would you like to play? (Yes/No): ").strip().lower()

    if wanna_play != 'yes':
        print("👋 No worries! See you next time!")
        return

    attempts_list = []

    while wanna_play == 'yes':
        show_score(attempts_list)
        play_game(player_name, attempts_list)

        wanna_play = input("Would you like to play again? (Yes/No): ").strip().lower()

    print("🛑 Game Over. Thanks for playing!")

if __name__ == "__main__":
    main()
