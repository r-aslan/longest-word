import random
import string
class Game:
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]
    
    def is_valid(self, word):
        is_valid = True
        #test if letters are formed with given list
        lWord = list(word)
        nbLetters = len(lWord)
        model = self.grid.copy()
        if not word:
            is_valid = False
        for i in range(nbLetters):
            if lWord[i] in model:
                model.remove(lWord[i])
                is_valid = True
            else:
                is_valid = False
        
        return is_valid