from .scraper import scraper
import yaml
import sys
import os
from random import sample 
from pathlib import Path

def login_info():
    user = input("Enter username: ")
    pw = input("Enter password: ")
    data = {'email': user, 'password': pw}
    with open('credentials.yaml', 'w') as f:
        yaml.dump(data, f)
        print("Credentials aqquired!")


def enter_input():
    while True:
        url = input("Please enter profile url (or 0 to finish): ")
        if url == '0':
            return
        with open('input.txt', 'a') as f:
            f.write(url+"\n")


def start_scraping():
    scraper(friends=True, posts=False)

# This function returns the user's facebook profile username
def get_username():
    path = Path('data')
    return next(os.scandir(path)).name


# This function chooses n random friends from the user friends list and scrapes their posts
def scrape_random():
    print("Please make sure only your profile url is in the input.txt file")
    num_of_friends = input("Number of friends to scrape (0 to go back to the menu): ")
    num_of_friends = int(num_of_friends)
    if num_of_friends == '0':
        return
    # First, get the user's friends list
    scraper(friends=True, posts=False)
    username = get_username()
    friends = Path('data/' + username + '/All Friends.txt')
    with open(friends, 'r', encoding="utf-8",) as f:
        friends_list = f.read().split('\n')
        chosen_friends = sample(friends_list, num_of_friends)

    # Second, choose a random group of friends
    with open('input.txt', 'w') as input_file:
        for friend in chosen_friends:
            input_file.write(friend.split(',')[0] + '\n')

    # Third, scrape the chosen friends' posts
    scraper(friends=False, posts=True)


def quit():
    print("Quitting...")
    sys.exit()


# Function for debugging purposes
def debug():
    print("debugging")


def menu():
    menu = {'1':["Input credentials", login_info], '2':["Enter profiles to search", enter_input],
            '3':["Scrape away!", start_scraping], '4':["Scrape Random", scrape_random], '5':["Quit", quit]}

    while True:
        print("\nMenu:")
        for key in menu.keys():
            print(key+": "+menu[key][0])
        op = input("Please choose an action\n")
        if op == '0':
            debug()
        else: 
            menu[op][1]()


def main():
    print("Initializing final project...")
    menu()
    print("See ya later alligator")