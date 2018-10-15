def main():
    dog1 = dog('chihuahua', 'playful', 'brown')
    string = ''
    self = dog1
    self.givetreat(dog1)
    self.makestr(dog1)
    print(string)
    self.givetoy(dog1)
    self.makestr(dog1)
    print(string)
    self.giveblanket(dog1)
    self.makestr(dog1)
    print(string)
class dog:
    def __init__(self, breed, mood, color):
        self.breed = breed
        self.mood = mood
        self.color = color

    def breed(self):
        return self.breed
    
    
    def setmood(self):
        lis = ('friendly', 'playful', 'sleepy')
        if self.mood in lis:
            return self.mood
    
    def setcolor(self):
        return self.color
    def givetreat(self):
        self.mood = 'friendly'
        return(self.mood)
    def givetoy(self):
        self.mood = 'playful'
        return(self.mood)
    def giveblanket(self):
        self.mood = 'sleepy'
        return(self.mood)
    def makestr(self):
        string = (f'The {self.color} {self.breed} is {self.mood}.')
        return(string)

main()


