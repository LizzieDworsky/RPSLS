
from human import Human
from ai import AI

class RunGame:
    def __init__(self):
        self.player1 = Human()
        self.player2 = ""
    
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
        print ("Best two of three, lets begin!")

    def run_game(self):
        self.welcome()
        self.select_players()
        self.run_rounds()
    
    def assign_player_two(self, number_of_players):
        if number_of_players == "1":
            self.player2 = AI()
        elif number_of_players == "2":
            self.player2 = Human()

    def select_players(self):
        is_valid = False
        while is_valid == False:
            user_input = input ("How many players, one or two? ")
            if user_input == "1" or user_input == "2":
                self.assign_player_two(user_input)
                is_valid = True
            else:
                print ("Sorry we didn't get that.")

    def run_rounds(self):
        round_count = 0
        while self.player1.win_count < 2 and self.player2.win_count < 2:
            round_count += 1
            print ("")
            print (f"The current standing for round {round_count} is Player One has {str(self.player1.win_count)} wins and Player Two has {str(self.player2.win_count)} wins.")
            print("Player one make a selection")
            self.player1.choose_gesture()
            print("Player two make a selection")
            self.player2.choose_gesture()
            player_one_choice = self.player1.chosen_gesture
            player_two_choice = self.player2.chosen_gesture

            if player_one_choice == player_two_choice:
                print("It's a Tie!")
            elif player_one_choice == "Rock" and player_two_choice == "Scissors":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Scissors" and player_two_choice == "Paper":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Paper" and player_two_choice == "Rock":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Rock" and player_two_choice == "Lizard":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Lizard" and player_two_choice == "Spock":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Spock" and player_two_choice == "Scissors":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Scissors" and player_two_choice == "Lizard":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Lizard" and player_two_choice == "Paper":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Paper" and player_two_choice == "Spock":
                print("Player One Wins")
                self.player1.win_count += 1
            elif player_one_choice == "Spock" and player_two_choice == "Rock":
                print("Player One Wins")
                self.player1.win_count += 1
            else:
                print("Player Two Wins")
                self.player2.win_count += 1
        if self.player1.win_count == 2:
            print("Yay Player One won!")
        else:
            print("Yay Player Two won!")