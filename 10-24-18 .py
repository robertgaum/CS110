def main():
    dog1 = dog('chihuahua', 'playful', 'brown')
    dog2 = small('chihuahua','playful','red')
    dog3 = big('lab','playful','black')
    string = ''
    dog1.givetreat()
    print(dog1.makestr())
    dog1.givetoy()
    print(dog1.makestr())
    dog1.giveblanket()
    print(dog1.makestr())
    dog2.givecostume()
    print(dog2.makestr())
    try:
        dog2.givebone()
    except AttributeError:
        print('Bark!')
    dog3.givebone()
    print(dog3.makestr())
    try:
        dog3.givecostume()
    except AttributeError:
        print('Bark!')
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
class small(dog):
    def givecostume(self):
        self.mood = 'spooky'
        return(self.mood)
class big(dog):
    def givebone(self):
        self.mood = 'hungry'
        return(self.mood)
main()


