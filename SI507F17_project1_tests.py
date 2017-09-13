## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class TestCard(unittest.TestCase):
	def setUp(self):
		self.test_card = Card()
		self.test_card1 = Card(0,1)

	def test_constructor(self):
    	# test for default constructor
		self.assertEqual(self.test_card.suit, "Diamonds")
		self.assertEqual(self.test_card.rank_num, 2)
		self.assertEqual(self.test_card.rank, 2)
        
    	# test for non-default constructor
		self.assertEqual(self.test_card1.suit, "Diamonds")
		self.assertEqual(self.test_card1.rank_num, 1)
		self.assertEqual(self.test_card1.rank, "Ace")

	def tearDown(self):
		pass


class TestDeck(unittest.TestCase):
	def setUp(self):
		self.test_Deck = Deck()
		self.test_Deck1 = Deck()

		# Deck without the "Queen of Clubs" 
		self.test_Deck2 = Deck()
		self.test_Deck2.pop_card(24)

		self.test_Deck3 = Deck()

	def test_pop_card(self):
    	# test pop_card with default input on full deck with 52 cards
		self.test_Deck.pop_card()
    	# pop one last card
		self.assertEqual(len(self.test_Deck.cards),51)
		self.assertEqual(self.test_Deck.cards[-1].suit,"Spades")
    	# pop all cards
		for i in range(0,50):
			self.test_Deck.pop_card()
		self.assertEqual(self.test_Deck.cards[0].rank_num,1)
		self.assertEqual(self.test_Deck.cards[0].suit,"Diamonds")
		self.test_Deck.pop_card()
		self.assertEqual(len(self.test_Deck.cards),0)

        # test pop_card with non-default input
		self.test_Deck1.pop_card(5)
		self.assertEqual(self.test_Deck1.cards[5].rank_num,7)
		self.assertEqual(self.test_Deck1.cards[5].suit,"Diamonds")
		self.test_Deck1.pop_card(0)
		self.assertEqual(self.test_Deck1.cards[0].rank_num,2)
		self.assertEqual(self.test_Deck1.cards[0].suit,"Diamonds")

	def test_replace_card(self):
    	# if the input Card is not in the Deck --> should be put back into the Deck
		self.assertEqual(len(self.test_Deck2.cards),51)	
		self.test_Deck2.replace_card(Card(1,12))
		self.assertEqual(len(self.test_Deck2.cards),52)

		# if the input Card is in the Deck --> no changes
		self.test_Deck2.replace_card(Card(1,12))
		self.test_Deck2.replace_card(Card(3,10))
		self.assertEqual(len(self.test_Deck2.cards),52)

	def test_sort_cards(self):
		# sort with full Deck of cards
		self.test_Deck3.shuffle()
		self.test_Deck3.sort_cards()
		self.assertEqual(self.test_Deck3.cards[0].suit,"Diamonds")
		self.assertEqual(self.test_Deck3.cards[0].rank_num,1)
		self.assertEqual(self.test_Deck3.cards[13].suit,"Clubs")
		self.assertEqual(self.test_Deck3.cards[13].rank_num,1)
		self.assertEqual(self.test_Deck3.cards[-3].suit,"Spades")
		self.assertEqual(self.test_Deck3.cards[-3].rank_num,11)

		# sort with non-full Deck of cards
		self.test_Deck3.pop_card()
		self.test_Deck3.pop_card()
		self.assertEqual(self.test_Deck3.cards[-2].rank_num,10)
		self.assertEqual(self.test_Deck3.cards[-2].suit,"Spades")
		self.test_Deck3.pop_card(0)
		self.test_Deck3.pop_card(5)
		self.test_Deck3.pop_card(20)
		self.test_Deck3.shuffle()
		self.test_Deck3.sort_cards()
		self.assertEqual(self.test_Deck3.cards[-2].rank_num,10)
		self.assertEqual(self.test_Deck3.cards[-2].suit,"Spades")

	def test_deal_hand():

	def tearDown(self):
		pass












unittest.main(verbosity=2)

## Bugs Detected! 1. sort_cards()