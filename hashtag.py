

class Hastag():
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.hastagName = '#'+name
        self.popularWord = []

    def addPopularWord(self, word):
        self.popularWord += word

    def __str__(self):
        returnedStr = "Hastag \"{0}\" \n\twith count {1} \n\thas popular words: {2}"\
                    .format(self.hastagName, self.count, self.popularWord)
        return returnedStr