import datetime
class player:
    def __init__(self,fname,lname,birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    def get_age(self):
        now = datetime.datetime.now().year
        return now - self.birth_year

class tennis_player(player):
    def __init__(self,fname,lname,birth_year,team):
        super().__init__(fname,lname,birth_year)
        self.aces = []
        self.team = team

    def add_ace(self,aces):
        self.aces.append(aces)

    def get_avg_aces(self):
        return sum(self.aces)/len(self.aces)

class circket_player(player):
    def __init__(self,fname,lname,birth_year,team):
        super().__init__(fname,lname,birth_year)
        self.team = team
        self.scores = []

    def avg_score(self):
        return sum(self.scores)/len(self.scores)

    def add_score(self,score):
        self.scores.append(score)


virat: circket_player = circket_player('virat' , 'kohli' , 1988 , 'india')

virat.add_score(25)
virat.add_score(89)
virat.add_score(125)
virat.add_score(83)

print(virat.first_name)
print(virat.last_name)
print(virat.avg_score())
print(virat.team)
print(f"age of this player is {virat.get_age()}")

roger: tennis_player = tennis_player('Roger','feder',1981,'Swiss')
roger.add_ace(10)
roger.add_ace(15)
roger.add_ace(20)
print(roger.first_name)
print(roger.last_name)
print(roger.get_avg_aces())
print(roger.team)
print("age of roger feder",roger.get_age())