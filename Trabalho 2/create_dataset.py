import json
import csv
import copy
import os
import requests

import steam_games 
import steam_reviews 


# Python program to print 
# colored text and background 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

def update_result(results):

    # Update the dict with the info from author
    author = copy.deepcopy(results['author'])
    results.pop('author')
    results.update(author)

    # Update the review
    review = results['review']
    review = review.replace("\t", " ").replace("\n", " ")
    results['review'] = review

def create_csv(game_id, results):

    filename = 'dataset/' + game_id + ".tsv"
    with open(filename, 'w+') as f:

        # create the csv writer object
        writer = csv.writer(f, delimiter='\t')

        # Iterate from every review
        head = True
        for r in results:

            # update the results dict
            update_result(r)

            # If is head, write the header
            if head:
                writer.writerow(r.keys())
                head = False

            # write values
            writer.writerow(r.values())
    
    prGreen("TSV File created!")

def check_dataset(game_id):
    filename = 'dataset/' + game_id + ".tsv"
    return not os.path.exists(filename) 


# games = steam_games.get_most_reviewed_games()

# total = len(games)
# for i, game in enumerate(games):
#     print("[%d/%d]Downloading reviews from the game with id:" % (i, total), game)

#     if check_dataset(game):
#         results = steam_reviews.get(game, printProgress=True)
#         if results is not None:
#             create_csv(game, results)
#         else:
#             prRed("This ID don't exist!")
#     else:
#         prCyan("This dataset already exists!")

req = requests.get(url="http://api.steampowered.com/ISteamApps/GetAppList/v2", params={'json': 1})
games = req.json()

for i, game in enumerate(games['applist']['apps']):
    game_id = str(game['appid'])

    print("[%d/%d]Downloading reviews from the game with id:" % (i, len(games['applist']['apps'])), game_id)

    if check_dataset(game_id):
        results = steam_reviews.get(game_id, printProgress=True)
        if results is not None:
            if len(results) > 0:
                create_csv(game_id, results)
            else:
                prYellow("Don't have reviews!")
        else:
            prRed("This ID don't exist!")
    else:
        prCyan("This dataset already exists!")









# with open("id_games.txt", "r+") as f:
#     string = f.read()
#     id_games = json.loads(string)

# for a in id_games:
#     # now song is a dictionary
#     for attribute, value in a.items():
#         print(attribute, value) # example usage


# for i, game in enumerate(games):
#     print("[%d/%d]Downloading reviews from the game with id:" % (i, total), game)
#     if check_dataset(game):
#         results = steam_reviews.get(game, printProgress=True)
#         create_csv(game, results)
#     else:
#         print("This dataset already exists!")

