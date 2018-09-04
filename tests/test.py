import unittest

from app.signup import SignUp

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.signup = SignUp()

    def test_signup_creation(self):        
        self.assertIsInstance(self.signup, SignUp)

   
    
