from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.all_gestures)
        print(f'AI chose {self.chosen_gesture}')