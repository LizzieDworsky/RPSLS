from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        input_valid = False
        while input_valid == False:
            user_selection = input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: ")
            if user_selection == "0" or user_selection == "1" or user_selection == "2" or user_selection == "3" or user_selection == "4":
                user_selection = int(user_selection)
                self.chosen_gesture = self.all_gestures[user_selection]
                input_valid = True
            else:
                user_selection = print ("Sorry we didn't get that. Please try again.")

