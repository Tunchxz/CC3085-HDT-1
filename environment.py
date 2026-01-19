import random

class Environment(object):
    def __init__(self):
        self.temperature = random.randint(-10, 40)
    
    def get_percept(self):
        return self.temperature
    
    def update(self, action):
        if action == "enfriar":
            self.temperature -= 1
        elif action == "calentar":
            self.temperature += 1
