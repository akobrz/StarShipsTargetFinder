from os import system

from prettytable.colortable import ColorTable, Themes

from event import event
from log import log
from register import register

menus = ['log', 'register', 'event', 'exit']

def menu():
    while True:
        system('cls')
        choice = resolve_menu()
        if (choice == -1):
            break
        if (choice == 'q'):
            exit(0)
        if(choice == 0):
            log()
        if (choice == 1):
            register()
        if (choice == 2):
            event()
        if (choice == 3):
            exit(0)

def resolve_menu():
    table = ColorTable(["ID", "MENU"], theme=Themes.OCEAN)
    table.right_padding_width = 5
    table.left_padding_width = 2
    table.align = "l"

    print('\nPixel Starships Register\n')
    for id, item in enumerate(menus):
        table.add_row([str(id), menus[id]])
    print(table)
    return input_menu()

def input_menu():
    choice = input('\nEnter option from the menu (q to quit): ')
    if (choice == ''):
        return -1
    if (choice == 'q'):
        exit(0)
    return int(choice)

if __name__ == '__main__':
    menu()