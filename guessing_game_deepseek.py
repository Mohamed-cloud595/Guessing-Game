import random
import sys
from typing import List

class GuessingGame:
    def __init__(self):
        self.attempts_list: List[int] = []
        self.high_score: int = 0
        self.current_attempts: int = 0
        self.range_min: int = 1
        self.range_max: int = 10
        self.target_number: int = 0
        self.player_name: str = ""
    
    def show_score(self) -> None:
        """Display the current high score or welcome message if no games played yet."""
        if not self.attempts_list:
            print('No attempts yet, start playing!')
        else:
            print(f"The current high score is {min(self.attempts_list)} attempts.")
    
    def reset_game(self) -> None:
        """Reset game state for a new round."""
        self.current_attempts = 0
        self.target_number = random.randint(self.range_min, self.range_max)
    
    def validate_input(self, user_input: str) -> bool:
        """Validate that user input is within the allowed range."""
        try:
            guess = int(user_input)
            if guess < self.range_min or guess > self.range_max:
                raise ValueError(f'Please enter a number between {self.range_min} and {self.range_max}.')
            return True
        except ValueError as e:
            print(f"Invalid input: {e}")
            return False
    
    def get_user_guess(self) -> int:
        """Prompt user for a guess and return the validated input."""
        while True:
            guess_input = input(f'Pick a number between {self.range_min} and {self.range_max}: ')
            if self.validate_input(guess_input):
                return int(guess_input)
    
    def play_round(self) -> None:
        """Play one round of the guessing game."""
        guess = self.get_user_guess()
        self.current_attempts += 1
        
        if guess == self.target_number:
            print(f'Congratulations, {self.player_name}! You guessed the number in {self.current_attempts} attempts.')
            self.attempts_list.append(self.current_attempts)
            
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again == 'yes':
                self.reset_game()
                self.show_score()
            else:
                print(f'Thanks for playing, {self.player_name}! Your high score was {min(self.attempts_list)} attempts.')
                sys.exit(0)
        elif guess > self.target_number:
            print("It's lower, try again!")
        else:
            print("It's higher, try again!")
    
    def start_game(self) -> None:
        """Start the guessing game."""
        print('Welcome to the Guessing Game!')
        self.player_name = input('What is your name? ').strip() or "Player"
        
        wanna_play = input(
            f'Hello, {self.player_name}! Would you like to play the guessing game? (yes/no): '
        ).lower()
        
        if wanna_play != 'yes':
            print("That's cool, thanks!")
            sys.exit(0)
        
        self.reset_game()
        self.show_score()
        
        while True:
            self.play_round()

if __name__ == "__main__":
    try:
        game = GuessingGame()
        game.start_game()
    except KeyboardInterrupt:
        print("\n\nThanks for playing! Goodbye!")
        sys.exit(0)