#https://www.reddit.com/r/XboxGamePass/comments/jt214y/public_api_for_fetching_the_list_of_game_pass/
#https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=9ND0CG3LM22K,9NJWTJSVGVLJ&market=TR&languages=tr&MS-CV=DGU1mcuYo0WMMp+F.1
import json
import requests
ids = []
games = []
req = "https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds="
games_res = requests.get("https://catalog.gamepass.com/sigls/v2?id=fdd9e2a7-0fee-49f6-ad69-4354098401ff&language=tr&market=TR")
games_list = json.loads(games_res.text)
for i in range (1, len(games_list)):
    ids.append(games_list[i]["id"])
for j in range(len(ids)):
    if(j != 0):
        req += ","
    req += ids[j]
req += "&market=TR&languages=tr&MS-CV=DGU1mcuYo0WMMp"
main_res = requests.get(req)
main_data = json.loads(main_res.text)
for k in range(len(ids)):
    games.append([])
    games[k].append(main_data["Products"][k]["LocalizedProperties"][0]["ProductTitle"])
    games[k].append(main_data["Products"][k]["LocalizedProperties"][0]["ShortDescription"])
    #print(main_data["Products"][k]["LocalizedProperties"][0]["ProductTitle"])
    for l in range(len(main_data["Products"][k]["LocalizedProperties"][0]["Images"])):
        if(main_data["Products"][k]["LocalizedProperties"][0]["Images"][l]["ImagePurpose"] == "Poster"):
            games[k].append("https:" + main_data["Products"][k]["LocalizedProperties"][0]["Images"][l]["Uri"])
            #print("https:" + main_data["Products"][k]["LocalizedProperties"][0]["Images"][l]["Uri"])
print(games)