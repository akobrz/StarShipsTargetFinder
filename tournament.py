import json
import math
from datetime import datetime, timedelta
from os import system, listdir
from os.path import isfile, join

from prettytable.colortable import ColorTable, Themes

from common import id_player_id, id_player_name, id_fleet_id, id_fleet_name, battle_directory, battle_log, \
    id_player_fleet, id_log_player, my_user_id, id_log_result, pretty_label, id_player_stars, empty, players_in_list, \
    tournament_log, id_log_date, filter_top_players, id_player_trophy, color, YELLOW
from register import data_directory


def tournament():
    data_file = load_last_file()
    data_json = json.load(data_file)
    players = get_players(data_json)
    angrey_fleet_id = find_angrey(players)[id_player_fleet]
    fleets = [fleet for fleet in get_fleets(data_json)[:8] if fleet[id_fleet_id] != angrey_fleet_id]
    players = filter_top_players(fleets, players)
    log = read_from_file()
    tournament_log = read_from_tournament_log()
    log = filter_log(log, tournament_log)
    s = build_statistics(log, players, fleets)

    while True:
        system('cls')
        print('\nPixel Starships Tournament Targets\n')
        display_event(s, fleets)
        if (return_menu() == -1):
            break

def filter_log(log, tournament_log):
    event_delta = timedelta(days=8)
    tournament_log = [entry for entry in tournament_log if entry[id_log_date] > (datetime.today() - event_delta).strftime('%Y-%m-%d')]
    return [entry for entry in log if entry[id_log_player] not in [entry[id_log_player] for entry in tournament_log]]

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
    fleet_names = [fleet[id_fleet_name] for fleet in fleets]
    table = ColorTable(fleet_names, theme=Themes.OCEAN)
    table.right_padding_width = 0
    table.left_padding_width = 0
    table.align = "l"
    statistics.sort(key=lambda element: element[3])
    statistics.sort(key=lambda element: element[5])

    col0 = build_column(statistics, fleets[0][id_fleet_id])
    col1 = build_column(statistics, fleets[1][id_fleet_id])
    col2 = build_column(statistics, fleets[2][id_fleet_id])
    col3 = build_column(statistics, fleets[3][id_fleet_id])
    col4 = build_column(statistics, fleets[4][id_fleet_id])
    col5 = build_column(statistics, fleets[5][id_fleet_id])
    col6 = build_column(statistics, fleets[6][id_fleet_id])

    for i in range(0, players_in_list):
        table.add_row([col0[i], col1[i], col2[i], col3[i], col4[i], col5[i], col6[i]])

    print(table)


def build_column(statistics, fleet_id):
    result = []
    players = [s for s in statistics if s[4] == fleet_id and s[2] > 0 and s[1] / s[2] == 1][:players_in_list]
    for player in players:
        result.append(player[3] + ' ' + str(player[6]))
    while len(result) < players_in_list:
        result.append('')
    return result


def build_statistics(log, players, fleets):
    ids = get_log_players(log)
    statistics = []

    for user in players:
        user[id_player_stars] = math.floor(max(user[id_player_trophy] / 1000, user[id_player_stars] * 0.15))

    for id in ids:
        result = count_wins(id, log)
        player_name = get_player_name(id, players)
        player_fleet_id = get_fleet_id(id, players)
        player_fleet_name = get_fleet_name(player_fleet_id, fleets)
        player_stars = get_player_stars(id, players)
        if is_fleet_in_event(player_fleet_id, fleets):
            player_name = pretty_label(player_name)
            # player id, win battles, all battles, player name, player fleet id, player fleet name, player stars
            statistics.append([result[0], result[1], result[2], player_name, player_fleet_id, player_fleet_name, player_stars])
    return statistics

def count_wins(player_id, log):
    wins = 0
    battles = 0
    last_battles = [entry for entry in log if entry[id_log_player] == player_id][-3:]
    last_battles.sort(key=lambda element: element[0])

    for entry in last_battles:
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
            return color(p[id_player_stars], YELLOW)
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

def read_from_tournament_log():
    with open(battle_directory + tournament_log) as f:
        lines = [line.strip().split('|') for line in f]
    return lines

def load_last_file():
    files = [f for f in listdir(data_directory) if isfile(join(data_directory, f))]
    files.sort(reverse=True)
    return open('data\\' + files[0])


if __name__ == '__main__':
    tournament()