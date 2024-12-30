import json
import math
from os import listdir
from os.path import isfile, join

from common import data_directory

my_user_name = 'Angrey'
my_user_id = 2833456

division_a_fleets = 8

id_fleet_id = 0
id_fleet_name = 1
id_fleet_score = 2
id_fleet_division = 3

id_user_id = 0
id_user_name = 1
id_user_fleet = 2
id_user_trophy = 3
id_user_stars = 4
id_user_rank = 5
id_user_highest_trophy = 18
id_user_battles_today = 19
id_user_attack_wins = 11
id_user_attack_losses = 12
id_user_defence_wins = 14
id_user_defence_losses = 15

id_criteria_division = 0
id_criteria_min_trophy = 1
id_criteria_max_trophy = 2
id_criteria_highest_trophy = 3
id_criteria_stars = 4
id_criteria_my_fleet = 5
id_criteria_missing_player = 6
id_criteria_missing_feelt = 7

def position():
    # https://drive.google.com/drive/folders/10wOZgAQk_0St2Y_jC3UW497LVpBNxWmP
    f = load_last_file()
    data = json.load(f)
    fleets = data['fleets']
    fleets_names = []
    for f in fleets[0:8]:
        fleets_names.append(f[1])
    users = data['users']

    # fleet division, user_min_trophy, user_max_trophy, user_highest_trophy_ever, min_stars, my_fleet_id, user_min_trophy, user_highest_trophy_ever,
    # 5015
    criteria = [1, 4000, 5300, 5600, 11, 9343, 'abcde']
    display_my_fleet_position(users, criteria)

def display_my_fleet_position(users, criteria):
    fleet_users = [user for user in users if user[id_user_fleet] == criteria[id_criteria_my_fleet]]

    for user in fleet_users:
        user[id_user_stars] = math.floor(max(user[id_user_trophy] / 1000, user[id_user_stars] * 0.15))

    fleet_users = sorted(fleet_users, key=lambda user: user[id_user_stars], reverse=True)

    for (i, user) in enumerate(fleet_users):
        if (user[id_user_id] == my_user_id):
            print('\nAngrey is on the position', i, 'with', user[id_user_stars], 'stars\n')


def load_last_file():
    files = [f for f in listdir(data_directory) if isfile(join(data_directory, f))]
    files.sort(reverse=True)
    return open('data\\' + files[0])


if __name__ == '__main__':
    position()