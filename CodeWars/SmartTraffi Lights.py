class SmartTrafficLight():
    def __init__(self, st1, st2):
        self.st1_cars=st1[0]
        self.st1_name = st1[1]
        self.st2_cars=st2[0]
        self.st2_name = st2[1]
    def turngreen(self):
        if self.st1_cars>self.st2_cars:
            self.st1_cars=0
            return self.st1_name
        elif self.st1_cars==self.st2_cars:
            return None
        self.st2_cars=0
        return self.st2_name
