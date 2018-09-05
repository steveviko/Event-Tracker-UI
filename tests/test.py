import unittest

from app.signup import SignUp

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.signup = SignUp()

    def test_signup_creation(self):        
        self.assertIsInstance(self.signup, SignUp)

   
    def test_add_user(self):
        self.assertEqual(len(self.signup.user_details),0)  
        self.signup.add("steve","123")
        self.assertEqual(len(self.signup.user_details),1)
    
    def test_return_password(self):         
         self.signup.add("ven","12345")
         self.assertEqual(self.signup.get_password("ven","12345"))
