Recipe Converter
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

#### _**To execute**_
 
1. **Clone repository:** `git clone https://github.com/killakam3084/recipes_repo`
2. **Install recipes package** `cd recipes/  && pip install`

3. **Run the script:**
		
		usage: recipes-to-json [-h] [-s SERVING_SIZE] [-f FILTER_ITEMS]
                       input_file out_file

		Certainly this isn't how Food Network does it

		positional arguments:
		  input_file            An input text file to read in recipes from. Must
                        adhere certain structure.**
		  out_file              File to write json recipe data to.

		optional arguments:
		  -h, --help            show this help message and exit
		  -s SERVING_SIZE, --serving-size SERVING_SIZE
4. _**Example**_
    `recipes-to-json -s 4 -f "cheese,milk" recipes.json recipes.txt`

#### _**Assumptions**_
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
