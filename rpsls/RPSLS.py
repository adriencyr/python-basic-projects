import random, time
import colorama as color
from playsound import playsound

moves = {
    'rock': {
        'Strong':['scissors','lizard'],
        'Weak':['paper','spock'],
        'Color':color.Fore.RED,
    },
    'paper': {
        'Strong':['rock','spock'],
        'Weak':['scissors','lizard'],
        'Color':color.Fore.GREEN,
    },
    'scissors': {
        'Strong':['paper','lizard'],
        'Weak':['rock','spock'],
        'Color':color.Fore.YELLOW,
    },
    'lizard':{
        'Strong':['paper','spock'],
        'Weak':['rock','lizard'],
        'Color':color.Fore.BLUE,
    },
    'spock':{
        'Strong':['rock','scissors'],
        'Weak':['paper','lizard'],
        'Color':color.Fore.MAGENTA,
    },
}


round_tally = 1
user_win_tally = 0
cpu_win_tally = 0

color.init(autoreset=True)
print(f"""
      {color.Fore.RED} Rock, {color.Fore.GREEN} Paper, {color.Fore.YELLOW} Scissors, {color.Fore.BLUE} Lizard, {color.Fore.MAGENTA} Spock!
      
      {color.Fore.WHITE}
      """)
print("""
      Welcome to Rock Paper Scissors Lizard Spock! 
      This is a fun interactive Python game where you play the game of Rock Paper Scissors Lizard Spock with the Computer!
      The rules of RPSLS are simple. Rock beats Scissors and Lizard, Paper beats Rock and Spock, Scissors beats Paper and Lizard, Lizard beats Paper and Spock, and Spock beats Rock and Scissors.
      
      First, select a difficulty for the game. The higher the difficulty, the more accurate the Computer's guesses become. Challenge yourself!
      
      Difficulty Chart:
      1 - Easy
      2 - Normal
      3 - Hard
      4 - Impossible
      5 - You'll never win
      """)

difficulty = None
while difficulty not in ['1', '2', '3', '4', '5']:
    difficulty = input("Difficulty: ")
print(f"Difficulty {difficulty} selected!")

while True:
    print(f"Round {round_tally}\nScores (You/CPU): {user_win_tally}-{cpu_win_tally}")
    move_list = list(moves.keys())
    user_move = input("Your Move: ").lower()
    if user_move in move_list:
        user_move_index = move_list.index(user_move)
        move_list.insert(0, move_list.pop(user_move_index))
        cpu_choice = random.randint(0, (len(move_list) - int(difficulty))) 
        cpu_move = move_list[cpu_choice]
        move_dict = moves[cpu_move]
        
        print("Rock...")
        time.sleep(1)
        print("Paper...")
        time.sleep(1)
        print(f"{move_dict['Color']}{cpu_move.capitalize()}!")
        
        if user_move != cpu_move:
            strong = move_dict['Strong']
            weak = move_dict['Weak']
            
            if user_move in weak:
                print(f"Nice job, {color.Fore.LIGHTGREEN_EX}You Won!")
                playsound('win.mp3')
                user_win_tally += 1
                round_tally += 1
            else:
                print(f"Ouch, looks like {color.Fore.LIGHTRED_EX}You Lost!")
                playsound('lose.mp3')
                cpu_win_tally += 1  
                round_tally += 1         
        else:
            print(f"What are the odds? Looks like it's a {color.Fore.LIGHTYELLOW_EX}Tie!")
            round_tally += 1
            # loopback to input
    elif user_move == 'q':
        print("Quitting in 5 seconds.")
        print(f"Final Scoreboard:\nDifficulty: {difficulty}\nRounds Played: {round_tally}\nScores (You/CPU): {user_win_tally}-{cpu_win_tally}")
        time.sleep(5)
        quit()
    else:
        print("Invalid choice, please try again.")
    