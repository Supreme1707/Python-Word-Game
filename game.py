from time import sleep
from termcolor import colored
import random
import enchant
import string

output_opt = True


class Game:

    def __init__(self):
        self.difficulty_mode = 'medium'
        self.score = 0
        self.string_list = list(string.ascii_lowercase)

    def difficulty(self):
        print(colored("Please pick a difficulty with the number: ", "magenta"), end="")
        print(colored("1 easy, ", "green"), end="")
        print(colored("2 medium ", "blue"), end="")
        print(colored("or ", "magenta"), end="")
        print(colored("3 hard ", "red"))
        mode = input()
        try:
            if int(mode) == 1:
                self.difficulty_mode = 'easy'
                self.string_list.remove("q")
                self.string_list.remove("w")
                self.string_list.remove("x")
                self.string_list.remove("y")
                self.string_list.remove("z")
            elif int(mode) == 2:
                self.difficulty_mode = 'medium'
                self.string_list.remove("x")
                self.string_list.remove("y")
                self.string_list.remove("z")
            elif int(mode) == 3:
                self.difficulty_mode = 'hard'
        except:
            print("There was an error. It may be because you input a string instead of a number! Please input again.")
            self.difficulty()

    def intro(self):
        start_string = "Hello there! Welcome to the Word Game. Here, you will be given a letter and a single digit " \
                       "number.\nYou have to input a word from the selected English Dictionary with the number of " \
                       f"characters being the digit given.\n"

        # print(start_string)
        print_(start_string, 'yellow')

    def dict_select(self):
        global selected_dict
        english_dictionary = "Enter 1 for US dictionary and 2 for UK dictionary:"

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

    def game_method(self):
        if self.difficulty_mode == 'easy':
            counter = 10
        elif self.difficulty_mode == 'medium':
            counter = 15
        elif self.difficulty_mode == 'hard':
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
            print_("Next question coming in 5 seconds...\n", "blue")
            sleep(5)

        self.check_score()

    def score_method(self, check):
        if user_ans.startswith(rand_alphabet):
            if len(user_ans) == rand_num:
                if check:
                    print_("Correct! 1 point added!", 'green')
                    self.score += 1
                else:
                    print_("Uh oh! Your word wasn't in the dictionary!\n", 'red')
            else:
                print_(f"Uh oh! The number of characters in your word wasn't {rand_num}!\n",
                       'red')
        else:
            print_(f"Uh oh! Your word did not start with {rand_alphabet}!\n", 'red')

    def check_score(self):
        print_(f"Your score was {self.score}. End of Game.", 'green')


def print_(inpt_string, color):
    if output_opt:
        print(colored(inpt_string, color))
