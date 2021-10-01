import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 7)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.card1.value)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.card1, self.card2)
        self.assertEqual("You have a total of 8", result)

    