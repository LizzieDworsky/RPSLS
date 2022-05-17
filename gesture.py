
class Gesture:
    def __init__(self):
        self.name = ""
        self.beats = []
        self.win = False
        self.tie = False
    
    def comparison(self, other_gesture):
        if other_gesture.name in self.beats:
            self.win = True
        elif self.name == other_gesture.name:
            self.tie = True