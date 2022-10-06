'''
hilo.py plays the hilo game. It only relies on the highscore.json file to track the score. 
'''

# random and json are needed for the code to function properly.
import random
import json

def main():
    '''
    main() creates the menu that leads the hilo_game() function where the game is played. 
    It also can display the high-score and exit the program.
    '''
    # First menu is initialized as the sentinel for the menu loop.
    menu = True

    # Now we print the intro and rules for the user to see.
    print("Welcome to the HiLo game!\n-------------------------")
    print("You are given a card, and you must guess if the next card\nwill be higher or lower.\n* You start with 300 points.\n* If you are correct you earn 100 points.\n* If you are wrong you lose 75.")
    
    # The menu loop begins.
    while menu == True:

        # We print the menu for the user.
        print("\nWhat would you like to do?\n1. Play the game\n2. View high-score\n3. Quit")

        # Now we take the user's selection.
        menu_selection = int(input("> "))

        # If they chose 1, they are brought to the game within hilo_game().
        if menu_selection == 1:
            hilo_game(high_score())
        
        # If they chose 2, they are presented with the high scorer and their score.
        elif menu_selection == 2:
            print(f"\n{high_score()[0]} with a score of {high_score()[1]}")
        # Any other input ends the menu anf thus the program.
        else:
            menu = False
    
def hilo_game(high_score_data):
    '''
    hilo_game() runs the actual gameplay loop. It taks high_score_data as a parameter so that it
    can compare the users score with the high-score to see if the user has a new high-score.
    '''

    # The play sentinel is initialized.
    play = True

    # The base score is set.
    score = 300

    # The play loop begins.
    while play == True:

        # initial_card and new_card grab two random cards from the get_card() function.
        initial_card = get_card()
        new_card = get_card()

        # The user is told the first card.
        print(f"\nThe card is: {initial_card}")

        # They are asked if they think the next card will be higher or lower
        guess = input("Higher or lower? [h/l]: ")

        if initial_card < new_card:

            # If the initial_card is less than new_card and the user guessed "h" (for higher) they get 100 points. 
            if guess.lower() == "h":
                score += 100

            # If not, they got it wrong and lose 75 points.
            else:
                score -= 75

        elif initial_card > new_card:
            # This works the same as the IF statement above but flipped. If initial_card is more than new_card.

            if guess.lower() == "l":
                score += 100
            else:
                score -= 75

        else:
            # If neither of the above IF or ELIF statements happen, the cards were a tie. No points are lost or gained.

            # The user is told there was a tie.
            new_card = "Tie!"

        # The new_card is revealed and the user is shown their new score.
        print(f"Next card was: {new_card}")
        print(f"Your score is: {score}")

        # After all that if the score is < 0, the loop ends and the game is over.
        if score <= 0:
            print("GAME OVER! Score too low")
            break

        # If the score is not < 0 the user is given the option to stop, or go again.
        play_again = input("Keep playing? [y/n]: ")

        # If they say yes, the loop restarts.
        if play_again.lower() == "y":
            play = True
        
        # If they say no...
        elif play_again.lower() == "n":

            # the program checks to see if their score is higher than the new score.
            if score > high_score_data [1]:

                # If it is, the user is told who's score they beat, and what that score was.
                print(f"You beat {high_score_data[0]}'s score of: {high_score_data[1]}!")

                # They are then directed into the add_high_score() function.
                add_high_score(score)

            # play is set to False so the loop ends.
            play = False

def get_card():
    '''get_card() creates a random card and returns it.'''

    # The card is generated from 1 -13.
    card = random.randint(1,13)

    # It's value is returned.
    return card

def high_score():
    '''
    high_score() grabs the user who got the score, and their score from the
    highscore.json file.
    '''

    # The file is opened.
    file = open("highscore.json", "r")

    # The data is loaded into data.
    data = json.load(file)

    # The high_score_data is grabbed from the data.
    high_score_data = data["high-score"]

    # The user's name is saved as "high_name".
    high_name = high_score_data[0]

    # Their score is saved as "high_score"
    high_score = high_score_data[1]
    
    # The name and score are returned.
    return(high_name, high_score)

def add_high_score(score):
    '''
    add_high_score() replaces the old user's name and highscore with the new user's name and highscore
    in the highscore.json file.
    '''

    # The file is opened as readable.
    file = open("highscore.json", "r")

    # The data is saved into high_score_data.
    high_score_data = json.load(file)

    # The file is closed.
    file.close()

    # It is opened again as writeable.
    file = open("highscore.json", "w")

    # The user enters their name
    name = input("Enter name here: ")

    # They are congratulated on their score.
    print(f"Congratulations on your highscore {name} of {score}!")

    # The data in the file is replaced with the new file
    high_score_data["high-score"] = [name, score]
    json.dump(high_score_data, file)

# main() is run.
if __name__ == "__main__":
    main()