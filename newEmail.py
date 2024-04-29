from validateEmail import *

# user provides email address
def email_input ():
    email = input("Type your email address: ")
    print()
    return email 

# user confirms email 
def review_email (email):
    # user reviews email 
    user_check = input("Let's make sure I got that right. Your email address is " + email + "\nRight? (y/n)\n" )
    print()
    return user_check

# user can update email with a limited number of tries 
def update_email (email, tries, limit):
    while tries < limit - 1: 
        is_correct = review_email(email)
        if is_correct == "y": 
            up_email = email
            print("Great!")
            break
        elif is_correct == "n": 
            up_email = email_input()
            tries += 1
            email_errors = validate_email(up_email) 
            print_errors(email_errors)
            update_email(up_email, tries, limit - tries)
        else: 
            print("Invalid input")
            up_email = email_input()
            tries += 1 
            email_errors = validate_email(up_email) 
            print_errors(email_errors)
            update_email(up_email, tries, limit - tries)
    return up_email

# add email address to a list of email addresses 
def add_email (email):
    em_list = set()
    em_list.add(email)
    return em_list
