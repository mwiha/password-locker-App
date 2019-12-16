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

