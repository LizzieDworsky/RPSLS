
from human import Human

from human import Human
from ai import AI

class RunGame:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()
        self.ai = AI()
    
    def welcome(self):
        print ("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print ("")
        print ("To begin you select Rock, Paper, Scissors, Lizard, or Spock.")
        print ("Rock crushes Scissors")        
        print ("Scissors cuts Paper")        
        print ("Paper covers Rock")
        print ("Rock crushes Lizard")
        print ("Lizard poisons Spock")
        print ("Spock smashes Scissors")
        print ("Scissors decapitates Lizard")
        print ("Lizard eats Paper")
        print ("Paper disproves Spock")
        print ("Spock vaporizes Rock")
        print ("")

    def single_multi_player(self):
        is_valid = False
        while is_valid == False:
            user_input = input ("How many players, one or two? ")
            if user_input == "1":
                #run ai game
                is_valid = True
            elif user_input == "2":
                #run human v human game
                is_valid = True
            else:
                print ("Sorry we didn't get that.")