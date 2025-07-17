import datetime

def get_avg_score(player):
    return sum(player['score']) / len(player['score'])

def age_of_player(player):
    current_year = datetime.datetime.now().year
    return current_year - player['birth_year']

virat = {
    'first_name': 'Virat',
    'last_name': 'Kohli',
    'score': [],
    'birth_year': 1988,
}

virat['score'].append(80)
virat['score'].append(22)
virat['score'].append(0)

print(get_avg_score(virat))   
print(age_of_player(virat))
