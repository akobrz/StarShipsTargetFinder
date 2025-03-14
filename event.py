import json
from os import system, listdir
from os.path import isfile, join

from prettytable.colortable import ColorTable, Themes
from common import G, R, Y, id_player_id, id_player_name, id_fleet_id, id_fleet_name, battle_directory, battle_log, \
    id_player_fleet, id_log_player, my_user_id, id_log_result, pretty_label, id_player_stars, empty
from register import data_directory

event_win = True

def event(win):
    global event_win
    event_win = win
    data_file = load_last_file()
    data_json = json.load(data_file)
    players = get_players(data_json)
    angrey_fleet_id = find_angrey(players)[id_player_fleet]
    fleets = [fleet for fleet in get_fleets(data_json)[:8] if fleet[id_fleet_id] != angrey_fleet_id]
    log = read_from_file()
    s = build_statistics(log, players, fleets)

    while True:
        system('cls')
        print('\nPixel Starships Top Fleets\n')
        display_event(s, fleets)
        if (return_menu() == -1):
            break

def find_angrey(players):
    for player in players:
        if player[id_player_id] == my_user_id:
            return player
    return None

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

def display_event(statistics, fleets):
    table = ColorTable(["Fleet", "*", "Player", "Score", "Battles"], theme=Themes.OCEAN)
    table.right_padding_width = 1
    table.left_padding_width = 1
    table.align = "l"
    statistics.sort(key=lambda element: element[3])
    statistics.sort(key=lambda element: element[5])
    for entry in statistics:
        if event_win and entry[1] / entry[2] == 1:
            table.add_row([entry[5], entry[6], entry[3], "%.0f" % (entry[1] * 100 / entry[2]) + "%", "(" + str(entry[1]) + "/" + str(entry[2]) + ")"])
        if not event_win and entry[1] / entry[2] < 1:
            table.add_row([entry[5], entry[6], entry[3], "%.0f" % (entry[1] * 100 / entry[2]) + "%", "(" + str(entry[1]) + "/" + str(entry[2]) + ")"])

    print(table)

def build_statistics(log, players, fleets):
    ids = get_log_players(log)
    statistics = []

    for id in ids:
        result = count_wins(id, log)
        player_name = get_player_name(id, players)
        player_fleet_id = get_fleet_id(id, players)
        player_fleet_name = get_fleet_name(player_fleet_id, fleets)
        player_stars = get_player_stars(id, players)
        if is_fleet_in_event(player_fleet_id, fleets):
            player_name = pretty_label(player_name)
            statistics.append([result[0], result[1], result[2], player_name, player_fleet_id, player_fleet_name, player_stars])
    return statistics

def count_wins(player_id, log):
    wins = 0
    battles = 0
    for entry in log:
        if entry[id_log_player] == player_id and entry[id_log_result] == 'win':
            wins += 1
        if entry[id_log_player] == player_id:
            battles += 1
    return (player_id, wins, battles)

def get_log_players(log):
    result = []
    for entry in log:
        if entry[id_log_player] not in result:
            result.append(entry[id_log_player])
    return result

def get_player_stars(id, players):
    for p in players:
        if (int(id)) == p[id_player_id]:
            return p[id_player_stars]
    return empty

def get_player_name(id, players):
    for p in players:
        if int(id) == p[id_player_id]:
            return p[id_player_name]
    return empty

def get_fleet_name(id, fleets):
    if id == None:
        return empty
    for f in fleets:
        if int(id) == f[id_fleet_id]:
            return f[id_fleet_name]
    return empty

def get_fleet_id(id, players):
    for p in players:
        if p[id_player_id] == int(id):
            return p[id_player_fleet]
    return None

def is_fleet_in_event(id, fleets):
    for f in fleets:
        if f[id_fleet_id] == id:
            return True
    return False

def read_from_file():
    with open(battle_directory + battle_log) as f:
        lines = [line.strip().split('|') for line in f]
    return lines

def load_last_file():
    files = [f for f in listdir(data_directory) if isfile(join(data_directory, f))]
    files.sort(reverse=True)
    return open('data\\' + files[0])


if __name__ == '__main__':
    event(True)