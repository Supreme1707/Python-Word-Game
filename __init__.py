from game import *


def main_method():
    start_obj = Start()
    start_obj.intro()
    start_obj.dict_select()
    game_obj = Game()
    game_obj.game_method()


main_method()
