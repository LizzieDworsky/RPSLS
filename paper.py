from gesture import Gesture

class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "Paper"
        self.losing_gestures = ["Rock", "Spock"]