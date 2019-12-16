import unittest
from password import password

class TestContact(unittest.TestCase):
    
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = password("Evans","Nyambane","0712345678","evans@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"Evans")
        self.assertEqual(self.new_password.last_name,"Nyambane")
        self.assertEqual(self.new_password.phone_number,"0712345678")
        self.assertEqual(self.new_password.email,"evans@ms.com")

if __name__ == '__main__':
    unittest.main()