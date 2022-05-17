from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock


class Player:
    def __init__(self):
        self.all_gestures = [Rock(), Paper(), Scissors(), Lizard(), Spock()]
        self.chosen_gesture = ""
        self.win_count = 0

    def choose_gesture(self):
        pass

