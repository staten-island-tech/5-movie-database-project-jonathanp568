class pet():
    def __init__(self, food):
        self.food = food
        return self.food
    def feed(self, feed):
        self.feed = feed 
        return self.food + self.feed
pet.__init__(10)