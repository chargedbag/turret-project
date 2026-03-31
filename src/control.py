class PController:
    def __init__(self, kp):
        self.kp = kp

    def compute(self, error):
        return self.kp * error
