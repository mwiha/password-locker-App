import pyperclip
import random
import string
from password import user, Credential

class User:
    """
    Class that generates new instances of user
    """
    
    user_list = [] 

    def __init__(self,account,first_name,last_name,email):
        self.account=account
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def save_user(self):
    
        '''
        save_user method saves user objects into password_list
        '''

        User.user_list.append(self)
        
        
    def delete_user(self):
    
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    
    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a user that matches that name.

        Args:
            name: user to search for
        Returns :
            user of person that matches the name.
        '''

        for user in cls.user_list:
            if user.user_name == name:
                return user


    @classmethod
    def name_exist(cls,name):
        '''
        Method that checks if a user exists from the name list.
        Args:
            name: user name to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.name == name:
                    return True

        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list


    @classmethod
    def copy_email(cls,name):
        user_found = name.find_by_name(name)
        pyperclip.copy(user_found.email)
        
        
    class Credential:
       """
       Class that generates new instances of credential
       """
    
    credential_list = [] 

    # def __init__(self,account,first_name,last_name,email):
        
    #     self.account=account
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
        
    def save_credential(self):
    
        '''
        save_user method saves user objects into password_list
        '''

        Credential.credential_list.append(self)
        
        
    def delete_credential(self):
    
        '''
        delete_credential method deletes a saved password from the credential_list
        '''
        Credential.credential_list.remove(self)
        
    def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        """
        function that generates passwords
        """

        gen_pass = ''.join(random.choice(char)for _ in range(size))
        return gen_pass
    
    @classmethod
    def find_by_credential(cls,password):
        '''
        Method that takes in a password and returns a credential that matches that password.

        Args:
            password: user to search for
        Returns :
            credential of person that matches the password.
        '''

        for user in cls.user_list:
            if Credential.credential_password == password:
                return user


    @classmethod
    def password_exist(cls,password):
        '''
        Method that checks if a user exists from the name list.
        Args:
            name: user name to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False
    
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credentialc list
        '''
        return cls.credential_list


    