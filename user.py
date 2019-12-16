import pyperclip

class User:
    """
    Class that generates new instances of user
    """
    
    user_list = [] 

    def __init__(self,first_name,last_name,email):

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
    def copy_email(cls,name):
        user_found = name.find_by_name(name)
        pyperclip.copy(user_found.email)