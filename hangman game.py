"""
Programmer:Loren
Date:12/7/2018
Purpose:To simulate a hangman guessing game where the user will try to guess all
the letters in a random word

"""
import random

# global constants 
LIST_OF_WORDS=["toothbrush","lightsabre","suitofarmor","python",
                               "toilet","physics","machine","bedrock","looking",
                               "dominant","elastic","war","list","others",
                               "people","lighthouse","world","motherboard",
                               "option","essay","america","unitedstates",
                               "homeless","celebrity","hammer","teeth",
                               "washingmachine","order","python","tuple",
                               "hanging","open","breakfast","island","internet",
                               "chose","insomanic","deravitive","beach","gothic",
                               "port","religious","top","hiking","operation"]

DASH="_"

# global variables 
word_list=[]
dashes=[]
guesses_left=10
guessed_letters=0
guessed_letters_list=[]
win=False
lose= False
play_again=True
word=""

# update player 
def update_dashes():

    for letter in guessed_letters_list:
        for char in range(len(dashes)):
            if word_list[char] == letter:
                dashes[char] = letter
         
    return dashes 

def display_main_menu():
    '''This function will display the main options menu for this program'''
    print("\n")
    print("HANGMAN GAME")
    print("\n")
    print("Select:")
    print("1 to start")
    print("2 for help menu")
    print("\n")
    
def display_help_menu():
    '''This function will display the instruction on how to play the game
        for anyone who doesn't know'''
    print("\n")
    print("HELP")
    print("\n")
    print("This is a hangman game")
    print("1. The computer will choose a random word from a list of words")
    print("2.You will have to try to guess all the letters in the word")
    print("3.You win the game if you guess all the letters in the word without guessing 10 incorrect letters")
    print("4.You will lose the game if you guess 10 incorrect letters")
    print("\n")

# while loop will ruin infinitely to make sure
#program never stops running

while True:
    display_main_menu()
    option=str(input("Choose an option"))
    
    # case when user chooses to play 
    if option=="1":

        # run as long as user wants to play again 
        while play_again:
            
            word=random.choice(LIST_OF_WORDS)

            # create list of words
            for letter in word:
                word_list.append(letter)
            
            # prepare list of dashes 
            for letter in word_list:
                dashes.append(DASH)
            
            # main game loop 
            while not win and not lose:

                print(update_dashes())

                # get user input 
                letter=str(input("Enter a letter")).lower()

                # if guess is correct
                if letter in word_list:
                    if letter in guessed_letters_list:
                        print("Letter was already chosen")
                    else:
                        print("Correct letter")
                        guessed_letters_list.append(letter)
                        guessed_letters+=word_list.count(letter)

                        # has user won 
                        if guessed_letters == len(word_list):
                            win = True
                            
                # if guess is wrong 
                else:
                    print("Wrong letter")
                    guesses_left-=1
                    print("You have "+str(guesses_left)+" guesses left")

                    # has user lost 
                    if guesses_left==0:
                        lose= True 
                      
             # when game ends               
            if lose:
                print("Sorry, you lost")
            elif win:
                print("Congragulations you won")

            # reset variables after game 
            dashes=[]
            guesses_left=10
            guessed_letters=0
            guessed_letters_list=[]
            word_list=[]
            win= False
            lose = False
                
            choice=str(input("Would you like to play again?Y or y for yes and N or n for no(default value is yes)"))

            if choice=="N" or choice== "n":
                play_again= False 
                           
        play_again = True

    # case when user chooses to see instructions 
    elif option=="2":
        display_help_menu()
   
                           
    


    

                           

    
