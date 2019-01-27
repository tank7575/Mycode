class Bird:
    '''A base class to define bird properties!'''
    count = 0

    def __init_(self,chat):
        self.sound = chat
        Bird.count += 1

    def talk(self):
        return self.sound
