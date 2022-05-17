from gesture import Gesture

class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Rock"
        self.losing_gestures = ["Scissors", "Lizard"]