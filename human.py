from player import Player
from user_interface import UserInterface

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        input_valid = False
        while input_valid == False:
            selection_options = ["0", "1", "2", "3", "4"]
            user_selection = UserInterface.take_input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: ")
            if user_selection in selection_options:
                user_selection = int(user_selection)
                self.chosen_gesture = self.all_gestures[user_selection]
                input_valid = True
            else:
               print("Sorry we didn't get that. Please try again.")
