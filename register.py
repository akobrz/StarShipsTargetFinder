import json
import math
from datetime import datetime
from os import listdir, system
from os.path import isfile, join

from prettytable.colortable import ColorTable, Themes

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

data_directory = 'data\\'
battle_directory = 'battles\\'
battle_log = 'log.txt'
results = ['win', 'lose', 'draw', 'escape', 'timeout']

player_min_trophy = 4800

def register():
    data_file = load_last_file()
    data_json = json.load(data_file)
    fleets = filter_fleets(data_json)
    users = filter_players(data_json)
    while True:
        system('cls')
        print('\nPixel Starships Register\n')
        result = registration(fleets, users)
        if (result == -1):
            break

def filter_fleets(data_json):
    all_fleets = data_json['fleets']
    all_players = data_json['users']
    fleets = []
    for f in all_fleets:
        is_any_player = False
        for p in all_players:
            if f[id_fleet_id] == p[id_player_fleet] and p[id_player_trophy] > player_min_trophy:
                is_any_player = True
                break
        if is_any_player:
            fleets.append(f)
    return fleets

def filter_players(data_json):
    all_players = data_json['users']
    return [p for p in all_players if p[id_player_trophy] > player_min_trophy]

def registration(fleets, players):
    fleet_id = resolve_fleet(fleets)
    if (fleet_id == -1):
        return -1
    player_id = resolve_player(fleet_id, players)
    if (player_id == -1):
        return -1
    selected_fleet = [fleet for fleet in fleets if fleet[id_fleet_id] == fleet_id]
    selected_player = [player for player in players if player[id_player_id] == player_id]
    return resolve_battle(selected_fleet, selected_player)

def resolve_battle(selected_fleet, selected_player):
    selected_result = results[resolve_result()]
    if (selected_result == -1):
        return -1
    current_date = datetime.today().strftime('%Y-%m-%d')
    write_to_file(selected_fleet, selected_player, selected_result, current_date)
    return 0

def write_to_file(selected_fleet, selected_player, selected_result, current_date):
    with open(battle_directory + battle_log, 'a+') as f:
        f.write(str(current_date) + "|" + str(selected_fleet[0][id_fleet_id]) + "|" + str(selected_player[0][id_player_id]) + "|" + selected_result + '\n')

def resolve_result():
    table = ColorTable(["ID", "RESULT"], theme=Themes.OCEAN)
    table.right_padding_width = 5
    table.left_padding_width = 2
    table.align = "l"

    for id, result in enumerate(results):
        table.add_row([str(id), results[id]])
    print(table)

    return input_result()

def resolve_player(fleet_id, players):
    players_names = []
    for p in [player for player in players if player[id_player_fleet] == fleet_id]:
        players_names.append(p[id_player_name])
    players_names.sort()
    display_names(players_names)
    player_2_select = input_player()
    if (player_2_select == -1):
        return -1
    selected = players_names[player_2_select]
    print("\nPlayer selected: " + selected)
    for p in players:
        if p[id_player_name].rstrip() == selected.rstrip():
            return p[id_player_id]
    print("\n Player not identified")
    return -1

def resolve_fleet(fleets):
    fleets_names = []
    for f in fleets:
        fleets_names.append(f[id_fleet_name])
    fleets_names.sort()
    display_names(fleets_names)
    fleet_2_select = input_fleet()
    if (fleet_2_select == -1):
        return -1
    selected = fleets_names[fleet_2_select]
    print("\nFleet selected: " + selected)
    for f in fleets:
        if f[id_fleet_name].rstrip() == selected.rstrip():
            return f[id_fleet_id]
    print("\n Fleet not identified")
    return -1

def input_result():
    choice = input('\nEnter result number: ')
    if (choice == ''):
        return -1
    if (choice == 'q'):
        exit(0)
    return int(choice)

def input_fleet():
    choice = input('\nEnter fleet number: ')
    if (choice == ''):
        return -1
    if (choice == 'q'):
        exit(0)
    return int(choice)

def input_player():
    choice = input('\nEnter player number: ')
    if (choice == ''):
        return -1
    if (choice == 'q'):
        exit(0)
    return int(choice)

def display_names(names):
    len_names = len(names)
    max_len = math.ceil(len_names / 4)
    max_len2 = 2 * max_len
    max_len3 = 3 * max_len
    if len_names > max_len:
        names_1 = create_column(0, names[:max_len])
    else:
        names_1 = create_column(0, names[:len_names])
    if len_names > max_len * 2:
        names_2 = create_column(max_len, names[max_len:max_len2])
    else:
        names_2 = create_column(max_len, names[max_len:len_names])
    if len_names > max_len3:
        names_3 = create_column(max_len2, names[max_len2 : max_len3])
    else:
        names_3 = create_column(max_len2, names[max_len2:len_names])
    if len_names > max_len3:
        names_4 = create_column(max_len3, names[max_len3:])
    else:
        names_4 = []

    display_columns(max_len, names_1, names_2, names_3, names_4)

def display_columns(max_len, column1, column2, column3, column4):
    table = ColorTable(["COL1", "COL2", "COL3", "COL4"], theme=Themes.OCEAN)
    table.right_padding_width = 5
    table.left_padding_width = 2
    table.align = "l"
    table.header = False

    for i in range(0, max_len):
        if i < len(column1):
            col1 = column1[i]
        else:
            col1 = ""
        if i < len(column2):
            col2 = column2[i]
        else:
            col2 = ""
        if i < len(column3):
            col3 = column3[i]
        else:
            col3 = ""
        if i < len(column4):
            col4 = column4[i]
        else:
            col4 = ""
        table.add_row([col1, col2, col3, col4])
    print(table)

def create_column(index, values):
    column = []
    for id, name in enumerate(values):
        to_append = (str(index + id).zfill(2) + " " + name)[:30]
        column.append(to_append)
    return column

def load_last_file():
    files = [f for f in listdir(data_directory) if isfile(join(data_directory, f))]
    files.sort(reverse=True)
    return open('data\\' + files[0])

if __name__ == '__main__':
    register()