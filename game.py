from time import sleep
from termcolor import colored
import random
import enchant
import string

output_opt = True


class Start:

    def intro(self):
        start_string = "Hello there! Welcome to the Word Game. Here, you will be given a letter and a single digit " \
                       "number.\nYou have to input a word from the selected English Dictionary with the number of " \
                       "characters being the digit given.\n"

        # print(start_string)
        print_(start_string, 'yellow')

    def dict_select(self):
        global selected_dict
        english_dictionary = "Enter 1 for US dictionary and 2 for UK dictionary."

        # print(english_dictionary)
        print_(english_dictionary, 'blue')

        selected_dict_num = input()

        if int(selected_dict_num) == 1:
            selected_dict = enchant.Dict("en_US")
            print_("Selected US English Dictionary.\n", 'green')
        elif int(selected_dict_num) == 2:
            selected_dict = enchant.Dict("en_GB")
            print_("Selected UK English Dictionary.\n", 'green')
        else:
            print_("Wrong input.", 'red')
            self.dict_select()


class Game:
    def __init__(self):
        self.score = 0
        self.string_list = list(string.ascii_lowercase)

    def game_method(self):
        counter = 20
        i = 0
        while i < counter:
            global rand_num
            global user_ans
            global rand_alphabet
            rand_num = random.randint(3, 9)
            rand_alphabet = random.choice(self.string_list)
            print_(f"The alphabet is {rand_alphabet} and the number is {rand_num}.", 'white')
            user_ans = input()
            self.score_method(selected_dict.check(user_ans))
            i += 1

        self.check_score()

    def score_method(self, check):
        if user_ans.startswith(rand_alphabet):
            if len(user_ans) == rand_num:
                if check:
                    print_("Correct! 1 point added!\n", 'green')
                    self.score += 1
                else:
                    print_("Uh oh! Your word wasn't in the dictionary...\n", 'red')
            else:
                print_(f"Uh oh! The number of characters in your word wasn't {rand_num}!\n",
                            'red')
        else:
            print_(f"Uh oh! Your word did not start with {rand_alphabet}\n", 'red')

    def check_score(self):
        print_(f"Your score was {self.score}. End of Game.", 'green')


def print_(inpt_string, color):
    if output_opt:
        print(colored(inpt_string, color))
