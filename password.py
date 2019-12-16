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
    pass

