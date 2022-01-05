
import art
import random
from game_data import data
import replit


game_variables = {
  "a": 0,
  "b": 0,
  "current_score": 0
}
def randomize():
  game_variables["b"] = random.randint(0,len(data)-1)
  if game_variables["a"] == game_variables["b"]:
    randomize()
  else:
    return

def is_correct(a,b):

  if data[a]['follower_count'] > data[b]['follower_count']:
    return "a"
  else:
    return "b"

def game(a,b):
  print(art.logo)
  if(game_variables["current_score"] > 0):
    print(f"You're right! Current score : {game_variables['current_score']}")

  print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")

  print(art.vs)

  print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")

  answer = input("Who has more followers? Type 'A' or 'B':").lower()


  print(is_correct(a,b))
  if(answer == is_correct(a,b)):
    game_variables["current_score"] +=1
    game_variables["a"]=game_variables[answer]
    game_variables["b"] = random.randint(0,len(data)-1)
    if game_variables["a"] == game_variables["b"]:
      randomize()
    replit.clear()
    game(game_variables["a"],game_variables["b"])
  else:
    return

game_variables["a"] = random.randint(0,len(data)-1)
game_variables["b"] = random.randint(0,len(data)-1)

#super ugly but makes sure that the random choices are not the same

if game_variables["a"] == game_variables["b"]:
   randomize()

else:
  game(game_variables["a"],game_variables["b"])

print(f"You Lose! Final Score : {game_variables['current_score']}")
   
    

