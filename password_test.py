import unittest
from password import User, Credential
import pyperclip

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Alice","Mwihaki", "account","alicemwihaki99@gmail.com") 
        self.new_credential = Credential("Alice", "account","alicemwihaki99@gmail.com")     
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Alice")
        self.assertEqual(self.new_user.last_name,"Mwihaki")
        self.assertEqual(self.new_user.email,"alicemwihaki99@gmail.com")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
        
    def test_save_credential(self):
        '''
        test case to test if the credential object is saved into
         the  credential list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_list),1)
     
      
     
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","account","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
            
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","account","test@user.com") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
            
               
            
    def tearDown(self):
            '''
          tearDown method that does clean up after each test case has run.
        '''
            User.user_list = []
            
            
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","account","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
            
            
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","account","test@user.com") # new user
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)
            
            
    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by user name and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","account","test@user.com") # new name
        

        found_user = User.find_by_name("Alice")

        self.assertEqual(found_user.email,test_user.email)
        
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","account","test@user.com") # new user
        test_user.save_user()

        user_exists = User.name_exist("Alice")

        self.assertTrue(user_exists)
        
        
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the password.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","account","test@user.com") # new credential
        test_credential.save_credential()

        credential_exists = Credential.password_exist("password")

        self.assertTrue(credential_exists)
    
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found name
        '''

        self.new_user.save_user()
        User.copy_email("")

        self.assertEqual(self.new_user.email,pyperclip.paste())


    def test_display_all_credential(self):
         """
         returns a list of all password saved.
         """
         
         self.assertEqual(Credential.display_credential(),
                          Credential.credential_list)

if __name__ == '__main__':
    unittest.main()