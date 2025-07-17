
import datetime
class cricketplayer:
    team_size = 11
    def __init__(self,fname,lname,birth_year,team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self,score):
        self.scores.append(score)

    def avg_score(self):
        return sum(self.scores)/len(self.scores)

    def age_of_player(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year

virat= cricketplayer('virat' , 'kohli' , 1988 , 'india' )

virat.add_score(25)
virat.add_score(89)
virat.add_score(125)
virat.add_score(83)

print(virat.first_name)
print(virat.last_name)
print(virat.avg_score())
print(f"age of this player is {virat.age_of_player()}")

