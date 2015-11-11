
import random

ADJECTIVES = {
  "strong": ["Iron", "Steel", "Lead", "Brobdingnagian", "Stalwart",
             "Strapping", "Hale", "Staunch", "Stout"],
  "salty": ["Salty", "Briny", "Salted", "Alkaline", "Brackish"],
  "bitter": ["Sour", "Puckered", "Acrid", "Pungent"],
  "sweet": ["Sugared", "Candied", "Sacharriferous", "Cloying", "Rotting"],
  "fruity": ["Flowered", "Plummed", "South American", "Island", "Tiki", 
             "Carribean"]
}

GREETINGS = [
  "And a good day to ye, <<<patron>>>",
  "<<<patron>>>, pleasure to be makin\' yer acquaintance",
  "Avast ye, <<<patron>>>, what can I do ye fore?"
]
    
INGREDIENTS = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
  "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

NOUNS = {
  "strong": ["Fist", "Hammer", "Cannonball"],
  "salty": ["Gunwhale", "Mainstay", "Barnacle"],
  "bitter": ["Bitter", "Pucker", "Whiplash"],
  "sweet": ["Port-o-Call", "Shore-Leave", "Tradewind"],
  "fruity": ["Daiquiri", "Fruitfly"]
}

QUESTIONS = {
  "strong": "Do ye like yer drinks strong?",
  "salty": "Do ye like it with a salty tang?",
  "bitter": "Are ye a lubber who likes it bitter?",
  "sweet": "Would ye like a bit of sweetness with yer poison?",
  "fruity": "Are ye one for a fruity finish?"
}


def askQuestions(questions):
  """ Get answers to descriptive questions
  
      Args:
        questions: dict, key = varname
                         value = question text
                        
      Returns:
        answers: dict, key = varname
                       value = user input
  """
  
  answers = {}
  at_least_one_preference = False
  
  for k in questions:
    answers[k] = input(questions[k])
    if answers[k].lower() == 'y' or answers[k].lower() == 'yes':
      answers[k] = True
      at_least_one_preference = True
    else:
      answers[k] = False
    
  # if no yes answers, bail.
  if not at_least_one_preference:
    exit('Have some bilgewater and be on ye merry way.')
      
  return answers
  

def constructDrink(answers, ingredients):
  """ Generate drink ingredients from ingredients based on answers.
  
    Args:
      answers: dict, key = varname
                     value = boolean 
                     
      ingredients: dict, key = varname (corresponding to answers keys)
                         value = list of possible ingredients
                        
    Returns:
      drink: list of drink ingredients
  """
  
  drink = []
  
  for k in answers:
    if answers[k]:
      drink.append(random.choice(ingredients[k]))
  
  return drink


def generateDrinkName(answers, adjectives, nouns):
  """ Generate a two word drink name based on user preferences.
  
  Args:
    answers: dict, key = varname
                   value = boolean
                   
    adjectives: dict, key = varname
                      value = (somewhat) appropriate list of adjectives for key
                    
    nouns: dict, key = varname
                 value = list of nouns appropriate for key
                 
  Returns:
    drink_name: str, name of the drink.
  """
  
  possible_adjectives = []
  possible_nouns = []
  
  for k in answers:
    if answers[k]:
      possible_adjectives.append(random.choice(adjectives[k]))
      possible_nouns.append(random.choice(nouns[k]))
  
  adjective = random.choice(possible_adjectives)
  noun = random.choice(possible_nouns)
  drink_name = adjective + ' ' + noun
  
  return drink_name
  

def getPatronName():
  """ Get user name from user.
  
    Args:
      none.
    
    Returns:
      patron_name: str, name of user
  """
  
  patron_name = input('What be yer name, matey? ')
  
  return patron_name
  

def greeting(patron_name, greetings):
  generic_greeting = random.choice(greetings)
  specific_greeting = generic_greeting.replace("<<<patron>>>", patron_name)
  
  return specific_greeting
  
  
def keepDrinking(patron_name):
  keep_drinking = input("Another round, " + patron_name + "? ")
  if keep_drinking.lower() == 'y' or keep_drinking.lower() == 'yes':
    drinking = True
  else:
    drinking = False
    
  return drinking
  
  
if __name__ == '__main__':
  drinking = True
  
  while drinking:
    patron = getPatronName()
    print(greeting(patron, GREETINGS))
    answers = askQuestions(QUESTIONS)
    drink = constructDrink(answers, INGREDIENTS)
    drink_name = generateDrinkName(answers, ADJECTIVES, NOUNS)
    print("Have a {}".format(drink_name))
    print("Here\'s what\'s in it: ")
    for ingredient in drink:
      print(ingredient)
      
    drinking = keepDrinking(patron)
    