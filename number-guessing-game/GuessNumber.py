import random, time


def initialize():
    print("""Welcome to the Python Random Number Guessing game! In this game, you will either guess the computer's number, or the computer will try to guess yours! 
      Please note that the number will be between 1 and 100. 
      
      If you would like to guess a number, input "G". If you would like the computer to guess your number, input "C". Input "Q" to quit the prompt. 
      Have Fun! 
      """)

    
    return input("Please choose a game to play (G/C/Q): ").upper()

def getInt(str):
    # This function is used to prompt the user for their number, with the string inputted in str. 
    # It also checks if it is a valid number (isnumeric), and will either prompt again or return the integer type conversion.
    # This is called in the userGuess() function to ensure no matter what the user input will be a proper number to evaluate.
    inputV = input(str)
    while True:
        if not inputV.isnumeric():
            inputV = input("That was not a valid number. Please try again: ")
        else: 
            return int(inputV)
        
def userGuess(): # This is the function for the user guessing number game. The program will generate a random number between 1-100, and accept guesses until the user correctly guesses.
    randint = random.randint(1, 100)
    
    guess = getInt("\nOk! I have chosen a number between 1-100. Please input your guess for the number: ")
    
        
    while int(guess) != randint:
        
        if int(guess) > randint:
            guess = getInt("Sorry, but that number is too big. Please guess again: ")
            
        elif int(guess) < randint:
            guess = getInt("Sorry, but that number is too small. Please guess again: ")
        else:
            guess = getInt("That was not a valid guess. Please try again: ")
    
    print(f"Congrats! You successfully guessed the number. The number was indeed {randint}.")
    time.sleep(2)
    again = input("Would you like to play again? Y to play again. N to quit. R to return to the main menu.\n").upper()

    # Asking if they want to play again, and restarting the game if so. If not, quits the program, OR returns to the menu.
    if again == "Y":
        userGuess()
    elif again == "N":
        print("Thanks for playing! Exiting program in 5 seconds...")
        time.sleep(5)
        quit()
    elif again == "R":
        startGame()
    else:
        startGame()

def computerGuess(min, max): # This is the function for the CPU guessing number game. The program will attempt to guess the user's number.
    guess = random.randint(min, max)
    prev_guesses = [] # We will store any previous unique guesses in here. This list is checked for each guessing operation to ensure no duplicate guesses are made.
    
    print("\nOk, I will now attempt to guess your number. Please remember it needs to be between 1-100.")
    
    while True:
        ans = input(f"Is your number {guess}?\nPlease input H for too high, L for too low, or C for correct.\n").upper()
        
        # If the guess is too (H)igh, the program will update the max value to equal guess - 1. This ensures that subsequent guesses do not exceed n - 1, 
        # in other words, ensuring guesses do not exceed numbers that are established as too high.
        # Likewise, if the guess is too (L)ow, the program updates the min value to equal guess + 1, ensuring that subsequent guesses exceed n + 1,
        # or, ensuring that the subsequent guesses will be greater than numbers established as too low.
        if ans == "H":
            max = guess - 1
            guess = random.randint(min, max)
            while guess in prev_guesses:
                guess = random.randint(min, max)
            prev_guesses.append(guess) 
        elif ans == "L":
            min = guess + 1
            guess = random.randint(min, max)
            while guess in prev_guesses:
                guess = random.randint(min, max)
            prev_guesses.append(guess)
        elif ans == "C":
            print(f"Woot! I guessed your number, {guess}!")
            time.sleep(2)
            again = input("Would you like to play again? Y to play again. N to quit. R to return to the main menu.\n").upper()
            
            # Asking if they want to play again, and restarting the game if so. If not, quits the program, OR returns to the menu.
            if again == "Y":
                computerGuess(1, 100)  # Reset the range to default values.
            elif again == "N":
                print("Thanks for playing! Exiting program in 5 seconds...")
                time.sleep(5)
                quit()
            elif again == "R":
                startGame()
            else:
                startGame()
        else: 
            # This will only run if the user did not answer either (H)igh, (L)ow, or (C)orrect.
            # Thanks to the loop logic, we only have to tell the user their response is wrong. The program will loopback to the input prompt automatically.
            print("Whoops! Looks like that response isn't quite right.")


    
def startGame(): # This function is used to start the game by prompting the user to play. It is also called if the user chooses to play again, thus enabling replayability
    choice = initialize() # Calls the init function which will explain the game, and ask the user to choose which mode (G/C/Q) to play, which is then started up here.
    if choice == "G":
        userGuess()
    elif choice == "C":
        computerGuess(1, 100)
    elif choice == "Q":
        quit()

startGame() # We only have to call this once. Subsequent rounds (if any) are handled using recursion.