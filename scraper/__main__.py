from .scraper import scraper
import yaml
import sys

def login_info():
    user = input("Enter username: ")
    pw = input("Enter password: ")
    data = {'email': user, 'password': pw}
    with open('credentials.yaml', 'w') as f:
        yaml.dump(data, f)
        print("Credentials aqquired!")
# https://www.facebook.com/bar.simovich
def enter_input():
    while True:
        url = input("Please enter profile url (or 0 to finish): ")
        if url == '0':
            return
        with open('input.txt', 'a') as f:
            f.write(url+"\n")


def start_scraping():
    scraper()

def quit():
    print("Quitting...")
    sys.exit()

def menu():
    menu = {'1':["Input credentials", login_info], '2':["Enter profiles to search", enter_input],
            '3':["Scrape away!", start_scraping], '4':["Quit", quit]}

    while True:
        print("\nMenu:")
        for key in menu.keys():
            print(key+": "+menu[key][0])
        op = input("Please choose an action\n")
        menu[op][1]()


def main():
    print("Initializing final project...")
    menu()
    print("See ya later alligator")