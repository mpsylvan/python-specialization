- RECIPE STRUCTURE -- I would assign each recipe to a dictionary structure. This would allow us to nest the necessary
  attributes of each recipe as string keys that are paired with values that cater specifically to the 
  nature of each attribute, (recipe str name, a unit of time int, a list of ingredients, a difficulty score int)

- RECIPE ATTRIBUTES -- I would assign each recipe name to a str type, I'd assign cooking time to an int(understood as minutes) as this will be discrete non-decimal, I'd assign ingredients to 
  a list of tuples containing a str element that conveys the ingredient name, and slots for units of measure and/or notes about the ingredient.

- OUTER STRUCTURE  -- I would store every recipe within a general list. Sequenced list could be useful to understand the order of recipes entered. It could be easily manipulated and indexed  into when only looking at certain recipes via slicing, or when looking to drill down into something specific within a particular recipe dictionary. 