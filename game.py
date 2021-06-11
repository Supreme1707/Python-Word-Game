from time import sleep
from termcolor import colored
import requests
import random
import enchant
import string
import json
import hashlib

output_opt = True


class Start:

    def __init__(self):
        with open("score.json", "r") as f:
            self.jsonfile = json.load(f)

    def login(self):
        global username
        print_delay("Enter Username", 'magenta')
        username = str(input())
        print_delay("Enter Password", 'magenta')
        password = str(input())
        password_hash = hashlib.sha512(str(password).encode("utf-8")).hexdigest()
        if str(username.lower()) not in self.jsonfile['users']:
            self.jsonfile['users'][username.lower()] = {
                "password": password_hash
            }
            with open("score.json", "w") as f:
                json.dump(self.jsonfile, f, indent=4)
            print_delay("Successful Login.", 'green')
        else:
            if hashlib.sha512(str(password).encode("utf-8")).hexdigest() == self.jsonfile['users'][username.lower()][
                'password']:
                print_delay("Successful Login Yay.", 'green')
            else:
                print_delay("Password is wrong.", 'red')
                self.login()

    def intro(self):
        start_string = "Hello there! Welcome to the Word Game. Here, you will be given a letter and a single digit " \
                       "number.\nYou have to input a word from the selected English Dictionary with the number of " \
                       "characters being the digit given.\n"

        # print(start_string)
        print_delay(start_string, 'yellow')

    def dict_select(self):
        global selected_dict
        english_dictionary = "Enter 1 for US dictionary and 2 for UK dictionary.\n"

        # print(english_dictionary)
        print_delay(english_dictionary, 'blue')

        selected_dict_num = input()

        if int(selected_dict_num) == 1:
            selected_dict = enchant.Dict("en_US")
            print_delay("Selected US English Dictionary.", 'green')
        elif int(selected_dict_num) == 2:
            selected_dict = enchant.Dict("en_GB")
            print_delay("Selected UK English Dictionary.", 'green')
        else:
            print_delay("Wrong input.", 'red')
            self.dict_select()


class Game:
    def __init__(self):
        self.score = 0
        self.string_list = list(string.ascii_lowercase)

    def game_method(self):
        counter = 10
        i = 0
        while i < counter:
            global rand_num
            global rand_alphabet
            rand_num = random.randint(3, 9)
            rand_alphabet = random.choice(self.string_list)
            print_delay(f"The alphabet is {rand_alphabet} and the number is {rand_num}.\n", 'white')
            user_ans = input()
            self.score_method(selected_dict.check(user_ans))
            i += 1

        self.check_score()

    def score_method(self, check):
        if len(rand_alphabet) == rand_num:
            if check:
                print_delay("Correct! 1 point added!", 'green')
                self.score += 1
            else:
                print_delay("Uh oh! Your word wasn't in the dictionary...", 'red')
        else:
            print_delay("Uh oh! The number of characters in your word wasn't matching the number provided!\n", 'red')

    def upload_score(self):
        # with open("score.json")
        pass

    def check_score(self):
        with open("score.json", "r") as f:
            file = json.load(f)
        if 'high_score' in file['users'][username.lower()]:
            if file['users'][username.lower()]['high_score'] < self.score:
                file['users'][username.lower()]['high_score'] = self.score
            else:
                file['users'][username.lower()]['latest_score'] = self.score
        else:
            file['users'][username.lower()]['high_score'] = self.score

        with open("score.json", "w") as y:
            json.dump(file, y, indent=4)

        print_delay(f"Your score was {self.score}. End of Game.", 'green')


def print_opts():
    global output_opt
    opt = input(colored("Enter 1 for delayed output (looks like it is being typed) and 2 for normal output.\n", 'cyan'))
    if int(opt) == 1:
        output_opt = False
        print_delay("Selected delayed output.", 'green')
    elif int(opt) == 2:
        output_opt = True
        print(colored("Selected normal output.", 'green'))
    else:
        print(colored("Invalid. please select either 1 or 2.", 'red'))
        print_opts()


def print_delay(inpt_string, color):
    if output_opt:
        print(colored(inpt_string, color))
    else:
        for i in range(len(inpt_string)):
            print(colored(inpt_string[i], color), sep='', end='', flush=True)
            sleep(0.15)
