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