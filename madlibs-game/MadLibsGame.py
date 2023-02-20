import re
import time 

print("""Welcome to the MadLibs interactive python game!
      MadLibs is a game where you will input nouns, adjectives, objects, numbers, places and -ing verbs
      to form your own story in a template!
      
      We have three stories to choose from. To select the story, type in the number of that story.
      1 - Story 1
      2 - Story 2
      3 - Story 3
      
      If you are playing by yourself, play the 'Singleplayer' (S) mode. If you are playing with a friend,
      play the 'Multiplayer' (M) mode, then pass the screen to them! They will be able to see the story template
      and guide you through the prompt. Otherwise, playing Singleplayer mode will not reveal the story to
      you until it is completed.
      
      Type Q to quit the prompt.
      
      
      Have fun!
      """)
option = input("Please input a story selection: ")
pref1 = ""

if option.upper() != "Q": # Makes sure that we only ask the user the desired mode if they actually want to play
    pref1 = input("Please select a mode (S/M): ")


# Dictionary containing all of the stories.
# The dictionary is structured very simply to allow for the addition of more stories, by following
# the aforementioned structure, which contains simply each number of the story, which the numbers
# themselves are keys containing a nested dictionary of the story title and template.
# The program is written to accomodate for any existing stories, which means all you would have
# to do to add a new story is just add a new key underneath the stories dictionary, and follow
# the nested structure for the program to recognize a new story.
stories = {
    "1": {
        "title": "Story 1",
        "template": """There was once a magical ____ (noun) that could talk. The ____ (noun) lived in a magical ____ (place), surrounded by all kinds of creatures like ____ (plurnoun) and tiny ____ (plurnoun).

Despite being able to talk, the ____ (noun) was very ____ (adj) and didn't like to speak very often. Instead, it would just watch the other creatures in the ____ (place) and listen to their conversations.

One day, a group of travelers stumbled upon the magical ____ (place). They were amazed to see a talking ____ (noun) and asked it all kinds of questions. But the ____ (noun) just sat quietly, ____ (verb) and observing the travelers.

As the travelers left the ____ (place), they wondered what the ____ (noun) was thinking. Little did they know that the ____ (noun) was actually a wise sage, and it had many secrets to share. But it would only reveal them to those who were patient and willing to listen.""",
    },
    "2": {
        "title": "Story 2",
        "template": """Deep in the heart of the forest, there was a haunted ____ (place). Legend had it that the ____ (place) was cursed, and anyone who entered it would never come out.

Despite the warnings, a brave adventurer decided to explore the ____ (place). They brought with them only a map, a compass, and a sense of curiosity.

As they entered the ____ (place), they could feel a chill in the air. The walls were covered in creepy ____ (plurnoun), and the floors creaked underfoot. But the adventurer pressed on, ____ (verb) their way through the maze of rooms and corridors.

Suddenly, they heard a sound. It was a ghostly moan, echoing through the halls. The adventurer froze, but then they remembered their courage. They took a deep breath and continued on, determined to uncover the secrets of the haunted ____ (place).

Their ____ (bodypart) was shaking with fear, but they kept going. As they reached the heart of the ____ (place), they found a hidden room. Inside was an ancient artifact that would change their life forever. From that day on, the brave adventurer became a legend in their own right.""",
    },
    "3": {
        "title": "Story 3",
        "template": """Once upon a time, there was a ____ (bodypart) that loved to jump. It would leap and bound through the air, ____ (verb) with joy.

The other ____ (plurnoun) in the town didn't quite know what to make of the jumping ____ (bodypart). Some were afraid of it, while others thought it was just plain weird.

But the jumping ____ (bodypart) didn't care. It kept on ____ (verb), leaping over fences and bouncing off walls. It was as if the whole world was a giant trampoline, and the jumping ____ (bodypart) was having the time of its life.

Eventually, the jumping ____ (bodypart) became a bit of a local celebrity. People came from all over just to see it in action. They even built a special platform for it to jump off of, and the jumping ____ (bodypart) became a symbol of freedom and joy.""",
    },
}


def startGame(story, mode): # Main function of the game
    while True:
        def createStory(selection): # This function will take in the story selection, and return the template. Additional functionality to display the template for multiplayer mode
            print(f"{stories[selection]['title']} selected!\n\n")
            
            # Fetching the story template
            template = stories[selection]["template"]
            
            # Checking if multiplayer mode is enabled and if true, displays the story after a 5-second warning
            if mode.upper() == "M":
                print("Multiplayer mode is active! Make sure only your friend can see the screen!\nDisplaying the story in 5 seconds.\n")
                time.sleep(5)
                print("Template:\n", template, "\n")
    
    
            return template
          
        if story.upper() == "Q": # Quit the prompt
            quit()
        elif (story.isnumeric() and story in stories) == True: # Checks if the story variable is a number and if the inputted variable is in the stories dictionary
            template = createStory(story)
            
            # Gathering the words from the user
            print("Now, please input the words to replace the template.")
            words = {
                'noun': str(input("Noun: ")),
                'adj': str(input("Adjective: ")),
                'plurnoun': str(input("Plural Noun: ")),
                'bodypart': str(input("Part of Body: ")),
                'number': str(input("Number: ")),
                'place': str(input("Place: " )),
                'verb': str(input("Verb (ending in -ing): " ))
            }
        
            # Checking if the verb does not end with -ing, if so, appends 'ing' to the verb
            if (words['verb'][-1].lower() == 'g' and words['verb'][-2].lower() == 'n' and words['verb'][-3].lower() == 'i') == False: 
                words['verb'] += 'ing'
            
            # Checking if the inputted number is not a valid number, if so, will continuously ask the user for a valid number until they input one
            while words['number'].isnumeric() == False:
                words['number'] = str(input("You did not input a valid number, please try again: "))
            
                
            # Replacing the blanks in the template with the user's inputs
            for key, value in words.items():
                # The pattern is constructed using a raw string (r), allowing us to use slashes without escaping
                # The \b flag matches the boundary of ____, allowing us to find the blank lines and replace them
                # The \s compensates for any spaces in the code which previously would've caused us to find nothing
                pattern = r"\b____\s*\(\s*" + key + r"\s*\)"
                template = re.sub(pattern, value, template)
            
            # Displaying the completed template    
            print("\nAlright, here's your completed story! Looks good!")
            print("-------------------------------------------")
            print("Completed MadLib:\n")  
            print(template)
            postGame()
        else: 
            # Prompts the user to input again   
            story = input("Invalid selection, please choose again: ")

def postGame(): # Function that prompts the user if they would like to play again, and if so, calls the startGame() function again. Essentially allowing for the user to play for as many rounds as they desire
    again = input("Would you like to play again? (Y/N): ")

    if again.upper() == "Y":
        print("""Welcome to the MadLibs interactive python game!
        MadLibs is a game where you will input nouns, adjectives, objects, numbers, places and -ing verbs
        to form your own story in a template!
        
        We have three stories to choose from. To select the story, type in the number of that story.
        1 - Story 1
        2 - Story 2
        3 - Story 3
        
        If you are playing by yourself, play the 'Singleplayer' (S) mode. If you are playing with a friend,
        play the 'Multiplayer' (M) mode, then pass the screen to them! They will be able to see the story template
        and guide you through the prompt. Otherwise, playing Singleplayer mode will not reveal the story to
        you until it is completed.
        
        Type Q to quit the prompt.
        
        
        Have fun!
        """)
        option = input("Please input a selection: ")
        pref1 = ""

        if option.upper() != "Q":
            pref1 = input("Please select a mode (S/M): ")
            
        startGame(option, pref1)
    elif again.upper() == "N":
        quit()
    else:
        quit()



startGame(option, pref1) # Starting the first game. Subsequent games are started in the postGame() function - its exact functionality is annotated above