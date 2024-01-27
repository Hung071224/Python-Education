


"""
class counter:
    def __init__(self, count):
        self.count = count
    
    def __tick__(self):
        self.count += 1
    
    def __reset__(self): 
        self.count = 0
    
obj = counter(0)

"""












#BAI 2  

class clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes = 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
    def display(self):
        print(f"{self.hours :02d}:{self.minutes:02d}:{self.seconds:02d}:")































































