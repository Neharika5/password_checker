import sys
import requests
import hashlib
import os

def request_api_data(first_5_char_hashed_password):
    '''Requesting the data from the API'''
    url = "https://api.pwnedpasswords.com/range/" + first_5_char_hashed_password
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching the data, Response code: {response.status_code}. Check the API and try again later")
    return response

def check_my_password_pwned_count(response_from_api, our_hashed_password_suffix):
    '''Checking if password has ever been pwned or hacked and returning the count'''
    password_tuple = (line.split(":") for line in response_from_api.text.splitlines())
    for suffix, count in password_tuple:
        if suffix == our_hashed_password_suffix:
            return count
    return 0

def check_my_password(password):
    '''Hashes the password and checks if the password is present in the API response'''
    sha1_hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_char = sha1_hashed_password[:5]
    suffix = sha1_hashed_password[5:]
    response = request_api_data(first_5_char)
    return check_my_password_pwned_count(response, suffix)

def personalized_greeting():
    '''Add a personalized greeting'''
    print("Welcome to the Password Checker!")
    print("Please enter a password to check if it has been compromised.")
    print("You can enter '-1' to exit at any time.")

def main_file(filename):
    '''If you want to give a file as input, call this function with the filename as a command line argument. 
    Note that the input file must be present in the same directory that you are currently running this script from'''
    absolute_path = os.path.abspath(filename)
    with open(absolute_path) as file:
        for password in file:
            password = password.strip()
            count = check_my_password(password)
            if count:
                print(
                    f"The password '{password}' has been seen {count} times... You should probably change your password!")
            else:
                print(
                    f"The password '{password}' has not been seen before... You can choose this password ")
    return "Done!"

def main_user_input():
    '''Call this function if you want to manually give the password as input'''
    personalized_greeting()  # Adding a personalized greeting
    while True:
        print("Enter your password:")
        try:
            password = input().strip()
        except:
            print("You must enter a string")
            continue
        if password == "-1":
            break
        count = check_my_password(password)
        if count:
            print(
                f"The password '{password}' has been seen {count} times... You should probably change your password!")
        else:
            print(
                f"The password '{password}' has not been seen before... You can choose this password ")
    return "Done!"

def main_command_line(args):
    ''' Call this function by giving multiple command line arguments'''
    for password in args:
        count = check_my_password(password)
        if count:
            print(
                f"The password '{password}' has been seen {count} times... You should probably change your password!")
        else:
            print(
                f"The password '{password}' has not been seen before... You can choose this password ")
    return "Done"


# main_file(sys.argv[1])

# main_user_input()

# main_command_line(sys.argv[1:])
