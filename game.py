import random
import string
import enchant
#from PyDictionary import PyDictionary

class Game:
    
    
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]
    
    def is_valid(self, word):
        d = enchant.Dict("en_US")
        is_valid = True
        #test if letters are formed with given list
        lWord = list(word)
        nbLetters = len(lWord)
        model = self.grid.copy()
        if d.check(word) is False:
            return False
        
        for i in range(nbLetters):
            if lWord[i] in model:
                model.remove(lWord[i])
                is_valid = True
            else:
                is_valid = False
        
        return is_valid