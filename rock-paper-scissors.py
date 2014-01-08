__author__ = 'spex'

# Random generator for the move of the opponent
import random

# Print out the title when the application first starts up
print "============================================="
print "===         Welcome to                    ==="
print "=== Rock, Paper, Scissors, Lizard, Spock! ==="
print "=============================================\n"


# Now we print out the possible text inputs the player can type in
possibleInputs = ("quit","rock","paper","scissors","lizard","spock", "help")
alternativeInputs = ("q","r","p","s","l","sp", "h")

# Declare the starting variables and give them default values
playerWins = 0
aiWins = 0
quit = False

# While the player has NOT quit the game, continue playing
while not(quit):

    # Set the user input variable to blank
    userinput = ''
    # While the user input isn't valid, keep asking them what they want to do
    while (userinput not in possibleInputs) and (userinput not in alternativeInputs):
        userinput = raw_input("\n\nChoices: rock, paper, scissors, lizard, spock, help, and quit.\nYour Move?\n> ")

    # Get the ID of the user's input
    if userinput in possibleInputs:
        userinput = possibleInputs.index(userinput)
    else:
        userinput = alternativeInputs.index(userinput)

    # If the user chose "QUIT", then we're going to quit the game
    if userinput == possibleInputs.index("quit"):
        quit = True

    # If the user chose "Help", we just display the HELP message
    elif userinput == possibleInputs.index("help"):
        print"Just like 'Rock, Paper, Scissors', but we now have 'Lizard' and 'Spock'\nThis is how it is played:\n" + \
             "Rock crushes Scissors\nRock smashes Lizard\nPaper covers Rock\nPaper disproves Spock\nScissors cuts Paper" + \
            "\nScissors stabs Lizard\nLizard eats Paper\nLizard poisons Spock\nSpock vaporizes Rock\nSpock dismantles Scissors\n " + \
            "\nYou may also use the first letter of your choice (lowercase)\nExcept for 'spock', that choice is 'sp' instead of 's'."

    # If they're not quitting or asking for help, the only other choice is a move. Let's calculate the win/loss scenarios
    else:

        # Generate a random move for the computer
        aiMove = random.randint(1,5)

        # If the user input is the same as the ai input, it's A TIE
        if aiMove == userinput:
            print "You both chose " + possibleInputs[userinput]
            print "It was a tie!\n"
            print "Score:"
            print "You: %d" % (playerWins)
            print "Enemy: %d\n\n" % (aiWins)

        # Check every possible win scenario (Couldn't find a better way to organize this)
        elif (((input == 1) and (aiMove == 3)) or  # Rock crushes Scissors
        ((userinput == 1) and (aiMove == 4)) or  #Rock smashes Lizard
        ((userinput == 2) and (aiMove == 1)) or  #Paper covers Rock
        ((userinput == 2) and (aiMove == 5)) or  #Paper Disproves Spock
        ((userinput == 3) and (aiMove == 2)) or  #Scissors cuts Paper
        ((userinput == 3) and (aiMove == 4)) or  #Scissors stabs Lizard
        ((userinput == 4) and (aiMove == 2)) or  #Lizard eats Paper
        ((userinput == 4) and (aiMove == 5)) or  #Lizard poisons Spock
        ((userinput == 5) and (aiMove == 1)) or  #Spock vaporizes Rock
        ((userinput == 5) and (aiMove == 3))):   #Spock destroys Scissors
            print "You chose " + possibleInputs[userinput] + \
                "\nYour enemy chose " + possibleInputs[aiMove] + \
                "\nYou Win!"
            playerWins += 1
            print "Score:"
            print "You: %d" % (playerWins)
            print "Enemy: %d" % (aiWins)

        # If it's not a tie, and you didn't win. Then it must be a loss
        else:
            print "You chose " + possibleInputs[userinput] + \
                "\nYour enemy chose " + possibleInputs[aiMove] + \
                "\nYou Loose!"
            aiWins += 1
            print "Score:"
            print "You: %d" % (playerWins)
            print "Enemy: %d" % (aiWins)


# To reach this point, the user must have selected quit to exit the while loop.
# Print out the goodbye statement
print "\n\n"
print "==============================="
print "===                   ___   ==="
print "=== Have a nice day! (^_^)/ ==="
print "===                  /| |   ==="
print "==============================="