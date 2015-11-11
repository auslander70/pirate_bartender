
import random

QUESTIONS = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

INGREDIENTS = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
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


if __name__ == '__main__':
  
  answers = askQuestions(QUESTIONS)
  drink = constructDrink(answers, INGREDIENTS)
  print(drink)