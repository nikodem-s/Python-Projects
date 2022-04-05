from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"
printer = PrettyPrinter()


def getlinks():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def getScoreboard():
    scoreboard = getlinks()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        v_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        print("---------------------------------------------------------------------")
        print(f"{home_team['triCode']} vs {v_team['triCode']}")
        print(f"{home_team['score']} - {v_team['score']}")
        print(f"{clock}, {period['current']}")


def get_stats():
    stats = getlinks()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team",
                        teams))  # funkcja anonimowa, jesli warunek jest spelniony to zostaje element w liscie
    teams.sort(key=lambda x: int(x['ppg']['rank']))
    i = 0

    for team in teams:
        i += 1
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i}. {name} - {nickname}: {ppg}")


getScoreboard()
get_stats()

