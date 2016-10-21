# Recipe Converter
---
#### **recipes_files/ contains:** 
- a flat text file with sample recipes **recipes.txt**
- Also present in the json file being written to after each program execution recipes.json
- 
#### **recipe.py**
- Class definition of a *Recipe*

#### **recipes.py**
- parses commandline arguments to scale surving size and filter for ingredients
- instantiates Recipe objects 
  + massages these instances to Python dictionaies
  + wraps these together
  + encodes the python dict to JSON and writes to file

#### **To execute**
    usage: recipes.py [-h] [-s SERVING_SIZE] [-f FILTER_ITEMS]

    A vanilla program to convert flat text recipes to json

    optional arguments:
      -h, --help            show this help message and exit
      -s SERVING_SIZE, --serving-size SERVING_SIZE
                           The number of servings you'd like to make.
     -f FILTER_ITEMS, --filter-items FILTER_ITEMS
                          A comma delimited string of ingredients to filter
                          recipes by. Multi-word ingredients must be quoted.
    Certainly this isn't how Food Network does it

#### Example
	./recipes.py -s 4 -f "cheese,milk"

