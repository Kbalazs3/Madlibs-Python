# It is a Madlibs game written inPython.


def to_middle():
    return "\t" * 6


def stat_menu():
    print(to_middle() + "START MENU\n\n" + (to_middle() + "New Game\n") + to_middle() + "Quit Game")
    start_menu_command = input(to_middle() + "Enter 'n' to start new game, and 'q' to quit game\n:").upper()
    while start_menu_command != 'N' or start_menu_command != 'Q':
        start_menu_command = input(to_middle() + "Enter 'n' to start new game, and 'q' to quit game\n:").upper()
    if start_menu_command == 'N':
        game_logic()
    elif start_menu_command == 'Q':
        quit(0)


def game_modes():
    return "\tAnimals\n\tFamous People\n\tStar Wars"


def ask_game_mode():
    game_mode = input(to_middle() + "Choose the type of Madlibs Game, You want to play: \n")




def game_logic():
    pass


if __name__ == '__main__':
    stat_menu()