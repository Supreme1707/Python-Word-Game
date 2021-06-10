from game import *
from gh import *

def main_method():
    getter()
    print_opts()
    start_obj = Start()
    start_obj.login()
    start_obj.intro()
    start_obj.dict_select()
    game_obj = Game()
    game_obj.game_method()
    setter()

main_method()