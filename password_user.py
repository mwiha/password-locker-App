#!/usr/bin/env python3.6
from password import User, Credential

def create_user(fname,lname,account,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,account,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
    
def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)


def check_existing_user(name):
    '''
    Function that check if a user exists with that name and return a Boolean
    '''
    return User.name_exist(name)


def display_user():
    '''
    Function that returns all the saved names
    '''
    return User.display_users()

def main():
    print("Hello Welcome . What is your name?")
    user_name = input()

    print(f"Hello {user_name}.Welcome")
    print('\n')
    
    while True:
            print("Use these short codes : cu - create a new user, dc - display user, fc -find a user, ex -exit the user list ")

            short_code = input().lower()

            if short_code == 'cc':
                            print("New user")
                            print("-"*10)

                            print ("First name ....")
                            User.fname = input()

                            print("Last name ...")
                            User.lname = input()

                            print("Email address ...")
                            User.e_address = input()
                            
                            print("account ...")
                            User.e_address = input()
                            
                                            
                            # save_users(create_user(fname,lname,account,address)) # create and save new user.
                            # print ('\n')
                            # print(f"New user {fname} {lname} created")
                            print ('\n')
            
            
            elif short_code == 'dc':
    
                        if display_user():
                                print("Here is a list of all your user")
                                print('\n')

                                for contact in display_user():
                                        print(f"{contact.first_name} {contact.last_name} .....{contact.name}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any user saved yet")
                                print('\n')

            elif short_code == 'fc':

                        print("Enter the name you want to search for")

                        search_name = input()
                        
                        if find_user(search_user):
                            search_user = find_user(search_name)
                            print(f"{search_user.first_name} {search_user.last_name}")
                            print('-' * 20)

                            print(f"Password{search_user.name}")
                            print(f"Email address.......{search_user.email}")
                        else:
                                    print("That user does not exist")

            elif short_code == "ex":
                            print("Bye .......")
                            break
            else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == "__main__":
    main()
                            