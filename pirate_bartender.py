
import random

ADJECTIVES = {
  "strong": ["iron", "steel", "lead", "brobdingnagian", "stalwart",
             "strapping", "hale", "staunch", "stout"],
  "salty": ["salty", "briny", "salted", "alkaline", "brackish"],
  "bitter": ["sour", "puckered", "acrid", "pungent"],
  "sweet": ["sugared", "candied", "sachariferous", "cloying", "rotting"],
  "fruity": ["flowered", "plummed", "south american", "island", "tiki"]
}

NOUNS = {
  "strong": ["fist", "hammer", "cannonball"],
  "salty": ["gunwhale", "mainstay", "spanker"],
  "bitter": ["bitter", "pucker", "whiplash"],
  "sweet": ["port-o-call", "shore-leave", "tradewind"],
  "fruity": ["daiquiri", "fruitfly"]
}
    
INGREDIENTS = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
  "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
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
  
  for k in questions:
    answers[k] = input(questions[k])
    if answers[k].lower() == 'y' or answers[k].lower() == 'yes':
      answers[k] = True
    else:
      answers[k] = False
    
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
  
  possible_adjectives = []
  possible_nouns = []
  for k in answers:
    if answers[k]:
      possible_adjectives.append(random.choice(adjectives[k]))
      possible_nouns.append(random.choice(nouns[k]))
  
  print(possible_adjectives)
  print(possible_nouns)
  
  adjective = random.choice(possible_adjectives)
  noun = random.choice(possible_nouns)
  drink_name = adjective, ' ', noun
  
  return drink_name
  

def getPatronName():
  patron_name = input('What be yer name, matey? ')
  
  return patron_name
  

if __name__ == '__main__':
  
  patron = getPatronName()
  answers = askQuestions(QUESTIONS)
  drink = constructDrink(answers, INGREDIENTS)
  drink_name = generateDrinkName(answers, ADJECTIVES, NOUNS)
  print(drink_name)
  print(drink)