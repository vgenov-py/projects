class Dea:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, user_x, user_y):
        c1 = (user_x - self.x) ** 2
        c2 = (user_y - self.y) ** 2
        return (c1+c2)**0.5