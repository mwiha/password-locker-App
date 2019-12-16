#!/usr/bin/env python3.6
from user import User

def create_user(fname,lname,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email)
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