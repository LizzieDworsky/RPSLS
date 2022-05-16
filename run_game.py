
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

    def run_game(self):
        self.welcome()
        self.single_multi_player()

    def single_multi_player(self):
        is_valid = False
        while is_valid == False:
            user_input = input ("How many players, one or two? ")
            if user_input == "1":
                self.single_player()
                is_valid = True
            elif user_input == "2":
                self.two_player()
                is_valid = True
            else:
                print ("Sorry we didn't get that.")

    def single_player(self):
        while self.player1.win_count < 2 and self.ai.win_count < 2:
            self.player1.choose_gesture()
            self.ai.choose_gesture()
            gesture_choice = self.player1.chosen_gesture
            ai_choice = self.ai.chosen_gesture

            if gesture_choice == ai_choice:
                print("It's a Tie!")

            elif gesture_choice == "Rock" and ai_choice == "Scissors":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Scissors" and ai_choice == "Paper":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Paper" and ai_choice == "Rock":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Rock" and ai_choice == "Lizard":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Lizard" and ai_choice == "Spock":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Spock" and ai_choice == "Scissors":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Scissors" and ai_choice == "Lizard":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Lizard" and ai_choice == "Paper":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Paper" and ai_choice == "Spock":
                print("Player Wins")
                self.player1.win_count += 1
            elif gesture_choice == "Spock" and ai_choice == "Rock":
                print("Player Wins")
                self.player1.win_count += 1
            else:
                print("AI Wins")
                self.ai.win_count += 1
        if self.player1.win_count == 2:
            print("Yay Player one you won!")
        else:
            print("All the tears for player one")


    def two_player(self):
        while self.player1.win_count < 2 and self.player2.win_count < 2:
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
            print("Yay Player one you won!")
        else:
            print("Yay Player two you won!")