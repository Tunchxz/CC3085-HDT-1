class Agent(object):
    def __init__(self):
        pass
        
    def act(self, perception):
        if perception < 18:
            return "calentar"
        elif perception > 25:
            return "enfriar"
        else:
            return "esperar"
