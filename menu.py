from os import system

from prettytable.colortable import ColorTable, Themes

from event import event
from log import log
from register import register
from register_tournament import register_tournament
from tournament import tournament

menus = ['log', 'register battle', 'top fleets / win', 'top fleets / loss','tournament targets', 'tournament battle', 'exit']

def menu():
    while True:
        system('cls')
        choice = resolve_menu()
        if choice == -1:
            break
        if choice == 'q':
            exit(0)
        if choice == 0:
            log()
        if choice == 1:
            register()
        if choice == 2:
            event(True)
        if choice == 3:
            event(False)
        if choice == 4:
            tournament()
        if choice == 5:
            register_tournament()
        if choice == 6:
            exit(0)

def resolve_menu():
    print_menu()
    return input_menu()


def print_menu():
    table = ColorTable(["ID", "MENU"], theme=Themes.OCEAN)
    table.right_padding_width = 1
    table.left_padding_width = 1
    table.align = "l"
    print('\nPixel Starships Register\n')
    for id, item in enumerate(menus):
        table.add_row([str(id), menus[id]])
    print(table)


def input_menu():
    choice = input('\nEnter option from the menu (q to quit): ')
    if choice not in ('0', '1', '2', '3', '4', '5', '6', 'q'):
        exit(0)
    return int(choice)


if __name__ == '__main__':
    menu()