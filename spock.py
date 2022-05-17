from gesture import Gesture

class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Spock"
        self.losing_gestures = ["Scissors", "Rock"]