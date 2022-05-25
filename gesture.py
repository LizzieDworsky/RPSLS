
class Gesture:
    def __init__(self):
        self.name = ""
        self.losing_gestures = []
        self.win = False
        self.tie = False
    
    def comparison(self, other_gesture):
        self.win = False
        self.tie = False
        if other_gesture.name in self.losing_gestures:
            self.win = True
        elif self.name == other_gesture.name:
            self.tie = True