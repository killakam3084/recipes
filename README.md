ecipe Converter
---
#### **recipes_files/ contains:** 
- a flat text file with sample recipes **recipes.txt**
- the json file being written to after each program execution **recipes.json**

#### **recipes/ contains:** 

- **recipe.py**
    - Class definition of a *Recipe*
- **recipes.py**
    - parses commandline arguments to scale surving size and filter for ingredients
    - instantiates Recipe objects 
      + massages these instances to Python dictionaies
      + wraps these together
      + encodes the python dict to JSON and writes to file

#### _To execute_
**Clone repository:** 
`git clone https://github.com/killakam3084/recipes_repo`

**Run the script:**

    usage: recipes.py [-h] [-s SERVING_SIZE] [-f FILTER_ITEMS] input_file out_file

    Certainly this isn't how Food Network does it

    positional arguments:
      input_file            An input text file to read in recipes from. Must
                        adhere certain structure.**
      out_file              File to write json recipe data to.

    optional arguments:
      -h, --help            show this help message and exit
      -s SERVING_SIZE, --serving-size SERVING_SIZE
                        The number of servings you'd like to make.
      -f FILTER_ITEMS, --filter-items FILTER_ITEMS
                            A comma delimited string of ingredients to filter                        recipes by. Multi-word ingredients must be quoted.

    Recipe List must appear as follows. **
    =======
    recipe_name
    serveing_size
    ingredient 0
    ingredient 1
    ingredient 2
    ...
    ...
    ...
    ingredient n


#### _Example_
    ./recipes.py -s 4 -f "cheese,milk"

#### *Assumptions*
- The user only wants to scale up the recipe up by a multiple of original serving size
- The input flat text adheres to the sample txt structure:
    recipe name
    serving size
    ingredient 1
    ingredient 2
    ...
- Also chose to represent ingredients who don't have a defined quantity value
   as empty "" in the json representation...seemed reasonable.
- And per the problem formulation just filtering exact string matches..."cheese" won't find "cheddar cheese" and vice versa.


