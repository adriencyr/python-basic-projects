import colorama, random, time
from words import words
from words import hints
from hangman_visual import lives_visual_dict
import string

win_messages = [
    "Excellent! You're really good at this!",
    "Spot on! You're a natural at guessing.",
    "Fantastic work! You're on a roll.",
    "Brilliant! You really know your stuff.",
    "Perfect! You couldn't have done it better.",
    "Impressive! You're a master at guessing.",
    "Top-notch! You're making this look easy.",
    "Well done! Your guess was right on the money.",
    "Outstanding! Your guess was right on target.",
    "Amazing job! You're killing it with these guesses."
]

lose_messages = [
    "Sorry, that guess was way off the mark.",
    "Nope, that guess wasn't even close. Keep trying!",
    "Oh dear, that guess was a big miss.",
    "You're going to have to do better than that, sorry.",
    "Incorrect, but don't give up just yet.",
    "Not quite right, but you're getting closer.",
    "Almost there, but that guess wasn't quite it.",
    "Better luck next time, that guess wasn't the right answer.",
    "Nice try, but that guess wasn't correct.",
    "Sorry, that guess just wasn't up to par. Keep guessing!"
]


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def generate_hint(word): 
    return hints[word.lower()]

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7
    power_ups = ['Skip', 'Hint'] 
    # This is one of my unique additions. The user can choose to use either the Skip or Hint Power-Up once per game.
    # The Skip Power-Up will automatically guess a correct letter for the user.
    # The Hint Power-Up will give the user a hint of what the chosen word is.
    
    # My other unique addition is implementing the colorama module to give the game a nicer aesthetic.
    
    
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        print('Available Power-Ups: ',' '.join(power_ups))
        
        user_letter = input('Guess a letter OR use a Power-Up: ').upper()
        time.sleep(1)
        if user_letter == 'SKIP' and user_letter.capitalize() in power_ups:
            chosen_letter = list(word_letters)[0]
            used_letters.add(chosen_letter)
            word_letters.remove(chosen_letter)
            print('\n'+colorama.Fore.YELLOW+f'Used the Skip Power-Up! The letter {chosen_letter} was skipped.'+colorama.Fore.WHITE)
            power_ups.remove('Skip')
        elif user_letter == 'HINT' and user_letter.capitalize() in power_ups:
            print(colorama.Fore.LIGHTMAGENTA_EX+generate_hint(word)+colorama.Fore.WHITE)
            power_ups.remove('Hint')
        else:       
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('\n'+colorama.Fore.GREEN+win_messages[random.randint(0, (len(win_messages) - 1))]+colorama.Fore.WHITE)

                else:
                    lives = lives - 1 
                    print('\n'+colorama.Fore.RED+lose_messages[random.randint(0, (len(lose_messages) - 1))])
                    print(f'{colorama.Fore.WHITE}Your letter,', user_letter, 'is not in the word.')

            elif user_letter in used_letters:
                print('\nYou have already guessed that letter.')

            else:
                print('\nThat is not a valid letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('Oof, looks like you died. The word was', word)
        
        again = input("Would you like to play again? (Y/N): ").upper()
        
        if again == 'Y':
            hangman()
        elif again == 'N':
            print('Ok, thanks for playing! Exiting in 3 seconds.')
            time.sleep(3)
            quit()
        else:
            print('Ok, thanks for playing! Exiting in 3 seconds.')
            time.sleep(3)
            quit()      
    else:
        print('Nice job, you guessed the word,', word,)
        
        again = input("Would you like to play again? (Y/N): ").upper()
        
        if again == 'Y':
            hangman()
        elif again == 'N':
            print('Ok, thanks for playing! Exiting in 3 seconds.')
            time.sleep(3)
            quit()
        else:
            print('Ok, thanks for playing! Exiting in 3 seconds.')
            time.sleep(3)
            quit()


if __name__ == '__main__':
    hangman()