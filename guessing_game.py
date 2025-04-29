import random 

attempts_list = []

def show_score():
    if not attempts_list:
        print('No attempts yet , start playing!')
    
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")
    

attempts = 0 
rand_number = random.randint(1, 10)

print('Welcome to the guessing game!')
player_name = input('What is your name? ')
wanna_play = input(f'Hello, {player_name}! Do you want to play the guessing game? (Enter Yes/No) ')

if wanna_play.lower() != 'yes':
    print("That's cool, Thanbks!")
    exit()
else:
    show_score()
    
while wanna_play.lower() == 'yes':
    try:
        guess = int(input('Pick a number between 1 and 10: '))
        if(guess < 1 or guess > 10):
            raise ValueError('Please enter a number within the given range.')
        
        attempts += 1
        attempts_list.append(attempts)
        
        if guess == rand_number:
            print(f'Congratulations, {player_name}! You guessed the number in {attempts} attempts.')
           
            wanna_play = input("Would you like to play again? (Enter Yes/No) ")
            if wanna_play.lower() =='no':
                print('Thanks for playing! See you next time!')
                
            else:
                attempts = 0 
                rand_number = random.randint(1, 10)
                show_score()
                continue
                         
        elif guess > rand_number:
            print("It's higher, try again!")
        else:
            print("It's lower, try again!")
                                    
    except ValueError as error:
        print(error)
    
    
    