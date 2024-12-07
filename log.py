import json
from os import system, listdir
from os.path import isfile, join

from prettytable.colortable import ColorTable, Themes

from register import data_directory

my_user_name = 'Angrey'
my_user_id = 2833456

division_a_fleets = 8

id_fleet_id = 0
id_fleet_name = 1
id_fleet_score = 2
id_fleet_division = 3

id_player_id = 0
id_player_name = 1
id_player_fleet = 2
id_player_trophy = 3
id_player_stars = 4
id_player_rank = 5
id_player_highest_trophy = 18
id_player_battles_today = 19
id_player_attack_wins = 11
id_player_attack_losses = 12
id_player_defence_wins = 14
id_player_defence_losses = 15

id_criteria_division = 0
id_criteria_min_trophy = 1
id_criteria_max_trophy = 2
id_criteria_highest_trophy = 3
id_criteria_stars = 4
id_criteria_my_fleet = 5
id_criteria_missing_player = 6
id_criteria_missing_feelt = 7

player_min_trophy = 4800

battle_directory = 'battles\\'
battle_log = 'log.txt'

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

    for entry in log[-25:]:
        entry_date = str(entry[0])
        entry_fleet = get_fleet_name(int(entry[1]), fleets)
        entry_player = get_player_name(int(entry[2]), players)
        entry_result = entry[3]
        table.add_row([entry_date, entry_fleet, entry_player, entry_result])

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