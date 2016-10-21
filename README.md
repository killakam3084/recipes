# recipes
===
The *recipes_files*/ dir contains a flat text file with sample recipes
Also present in the json file being written to after each program execution
===
*recipe.py* 
- Class definition of a *Recipe*
*recipes.py* 
- parses commandline arguments to scale surving size and filter for ingredients
- instantiates Recipe objects 
  + massages these instances to Python dictionaies
  + wraps these together
  + encodes the python dict to JSON and writes to file
===
