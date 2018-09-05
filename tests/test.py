import unittest

from app.signup import SignUp

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.signup = SignUp()
        self.sample_users = dict(
            username = "steve",
            password = "123" ,
            email ="steve@gmail.com"       
        )



    def test_signup_creation(self):        
        self.assertIsInstance(self.signup, SignUp)

   
    def test_add_user(self):
        self.assertEqual(len(self.signup.user_details),0)  
        self.signup.add(**self.sample_users)
        self.assertEqual(len(self.signup.user_details),1)

    def test_user_num_list(self):
        self.assertEqual(len(self.signup.user_details),0)  
        self.signup.add(**self.sample_users)
        self.assertEqual(len(self.signup.user_num_list(5)), 5)

    def test_valid_email(self):         
        self.assertEqual(len(self.signup.user_details),0)  
        self.signup.add(**self.sample_users)
        result = self.signup.validate_email('steve@gmail.com')
        self.assertTrue(result)
