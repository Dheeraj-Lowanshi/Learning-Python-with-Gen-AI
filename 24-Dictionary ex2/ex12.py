


players={}

for i in range(5):
    name=input("Enter player name:")
    runs=int(input("Enter runs:"))
    players[name]=runs
print(players)
print("Highest scorer is",max(players.values()))
