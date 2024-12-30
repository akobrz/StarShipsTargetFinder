from rich.console import Console
from rich.text import Text
import rich

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

id_log_date = 0
id_log_fleet = 1
id_log_player = 2
id_log_result = 3

id_stat_player_id = 0
id_stat_wins = 1
id_stat_battles = 2
id_stat_player_name = 3
id_stat_fleet_id = 4
id_stat_fleet_name = 5
id_stat_stars = 6
id_stat_color = 7

player_min_trophy = 4800
player_max_trophy = 5800

players_in_list = 10

battle_directory = 'battles\\'
data_directory = 'data\\'
battle_log = 'log.txt'

empty = ""

#Colors
R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset

BLACK = '\033[30m'
RED = '\033[31m'
RED_BRIGHT = '\033[91m'
GREEN = '\033[32m'
GREEN_BRIGHT = '\033[92m'
YELLOW = '\033[33m'
YELLOW_BRIGHT = '\033[93m'
BLUE = '\033[34m'
BLUE_BRIGHT = '\033[94m'
MAGENTA = '\033[35m'
MAGENTA_BRIGHT = '\033[95m'
CYAN = '\033[36m'
CYAN_BRIGHT = '\033[96m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

tournament_log = 'tournament.txt'
results = ['win', 'lose', 'draw', 'escape', 'timeout']

def pretty_label(name):
    new_name = ''
    for c in name:
        if ord(c) < 55000:
            new_name += c
        else:
            new_name += '.'
    return new_name

def color(label, c):
    return c + str(label) + RESET

def find_angrey(players):
    for player in players:
        if player[id_player_id] == my_user_id:
            return player
    return None

def filter_top_players(fleets, players):
    return [user for user in players if user[id_player_trophy] in range(player_min_trophy, player_max_trophy) and user[id_player_fleet] in [fleet[id_fleet_id] for fleet in fleets]]

def tester():
    # print('\033[38;2;246;45;112mHello!\033[0m')
    print(RED + 'TEST\n' + RESET)
    print(MAGENTA + 'TEST\n' + RESET)
    print(GREEN + 'TEST\n' + RESET)
    print(GREEN_BRIGHT + 'TEST\n' + RESET)
    print(WHITE + 'TEST\n' + RESET)
    print(YELLOW + 'TEST\n' + RESET)
    print(WHITE + 'TEST\n' + RESET)
    print(BLUE_BRIGHT + 'TEST\n' + RESET)
    print(BLUE + 'TEST\n' + RESET)
    print(CYAN + 'TEST\n' + RESET)
    print(CYAN_BRIGHT + 'TEST\n' + RESET)
    print(WHITE + 'TEST\n' + RESET)

if __name__ == '__main__':
    tester()