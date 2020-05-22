import unittest
import guessingGame

class TestGame(unittest.TestCase):
    def test_input(self):
        result=guessingGame.run_guess_game(5,5)
        self.assertTrue(result)
    
    def test_input1(self):
        result=guessingGame.run_guess_game(5,0)
        self.assertFalse(result)
    
    def test_input2(self):
        result=guessingGame.run_guess_game(5,11)
        self.assertFalse(result)
        
    def test_input3(self):
        result=guessingGame.run_guess_game(5,'11')
        self.assertFalse(result)
    
if __name__=='__main__':
    unittest.main()