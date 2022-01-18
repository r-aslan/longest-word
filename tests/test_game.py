# tests/test_game.py
import unittest
import string
import random
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)
    
    def test_game_word_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Forcer la grille à un scénario de test :
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # S'assurer que la grille n'a pas été modifiée
    
    def test_game_word_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Forcer la grille à un scénario de test :
        self.assertIs(new_game.is_valid('SANDWICH'), False)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # S'assurer que la grille n'a pas été modifiée
        
    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Forcer la grille à un scénario de test :
      self.assertIs(new_game.is_valid('FEUN'), False)


