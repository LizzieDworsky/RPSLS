from gesture import Gesture

class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Scissors"
        self.losing_gestures = ["Paper", "Lizard"]