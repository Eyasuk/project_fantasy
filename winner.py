import requests
r=requests.get("https://fantasy.premierleague.com/api/leagues-classic/142197/standings/")
data=r.json()
max=0
p_name=""
for i in data["standings"]["results"]:
    if i["total"]>max:
        max=i["total"]
        p_name=i["player_name"]
print(p_name)

