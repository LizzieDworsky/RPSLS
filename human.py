from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        user_selection = int(input('Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: '))
        self.chosen_gesture = self.all_gestures[user_selection]
        print(f'You chose {self.chosen_gesture}')



