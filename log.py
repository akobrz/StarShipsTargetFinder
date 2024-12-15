import json
from os import system, listdir
from os.path import isfile, join

from prettytable.colortable import ColorTable, Themes

from common import G, R, Y, id_player_id, id_player_name, id_fleet_id, id_fleet_name, battle_directory, battle_log
from register import data_directory


def log():
    data_file = load_last_file()
    data_json = json.load(data_file)
    fleets = get_fleets(data_json)
    players = get_players(data_json)
    log = read_from_file()
    while True:
        system('cls')
        print('\nPixel Starships Log\n')
        display_log(log, fleets, players)
        if (return_menu() == -1):
            break

def get_fleets(data_json):
    return data_json['fleets']

def get_players(data_json):
    return data_json['users']

def return_menu():
    choice = input('\nPress Enter to return (q to quit): ')
    if (choice == ''):
        return -1
    if (choice == 'q'):
        exit(0)
    return int(choice)

def display_log(log, fleets, players):
    table = ColorTable(["DATE", "FLEET", "PLAYER", "RESULT"], theme=Themes.OCEAN)
    table.right_padding_width = 5
    table.left_padding_width = 2
    table.align = "l"
    for entry in log[-50:]:
        entry_date = str(entry[0])
        entry_fleet = get_fleet_name(int(entry[1]), fleets)
        entry_player = get_player_name(int(entry[2]), players)
        entry_result = entry[3]
        if entry_result == "win":
            table.add_row([entry_date, entry_fleet, entry_player, G + entry_result])
        elif entry_result == "lose":
            table.add_row([entry_date, entry_fleet, entry_player, R + entry_result])
        else:
            table.add_row([entry_date, entry_fleet, entry_player, Y + entry_result])
    print(table)

def get_player_name(id, players):
    for p in players:
        if (id == p[id_player_id]):
            return p[id_player_name]

def get_fleet_name(id, fleets):
    for f in fleets:
        if (id == f[id_fleet_id]):
            return f[id_fleet_name]

def read_from_file():
    with open(battle_directory + battle_log) as f:
        lines = [line.strip().split('|') for line in f]
    return lines

def load_last_file():
    files = [f for f in listdir(data_directory) if isfile(join(data_directory, f))]
    files.sort(reverse=True)
    return open('data\\' + files[0])


if __name__ == '__main__':
    log()