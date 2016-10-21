from sets import Set


class Recipe:
    """
    A class representing a Recipe encapsulating name, serving size, and
    ingredient list
    """

    @staticmethod
    def is_int(s):
        """
        Helper function to return if integer
        :param s: a string to decipher
        :return: bool T/F
        """
        try:
            int(s)
            return True
        except ValueError:
            return False

    """
    Collection of measurement types to ignore for parzing ingredient
    tokens
    """
    measurement_set = Set(
        ['bbl', 'cu', 'doz', 'F', 'fl', 'ft', 'gal', 'gr', 'gross',
         'in', 'lb', 'oz', 'pt', 'qt', 'sq', 'T', 't', 'tbsp',
         'tsp', 'tbs'])

    def __init__(self, name, serving_size, serving_size_override,
                 ingredients_list):
        """
        Constructs an instance of a Recipe
        :param name: the name of the recipe
        :param serving_size: the number of servings a recipe makes
        :param serving_size_override: a multiple of the standard serving size
        :param ingredients_list: a list of ingredient tokens to coerce into dicts
        :return: nothing
        """
        self.name = name
        self.serving_size = int(serving_size)
        self.ingredients_list = ingredients_list
        self.serving_size_override = int(serving_size_override)

    def construct_ingredient_dict(self, scale_factor):
        """
        A method that massages a list of ingredient tokens for a recipe into a
        dictionary
        :param scale_factor: the multiplier by which to scale ingredient quantities
        :return: a dictionary of ingredient/quantity key/value pairs
        """
        ingredient_dict = {}
        for item in self.ingredients_list:
            quantity_string = ""
            item_name_string = ""
            for token in item.split(' '):
                if token in Recipe.measurement_set or Recipe.is_int(token):
                    if Recipe.is_int(token):
                        token = str(int(token) * scale_factor)
                    quantity_string += token + ' '
                else:
                    item_name_string += token + ' '
            ingredient_dict[item_name_string.strip()] = quantity_string.strip()
        return ingredient_dict

    def construct_json_rep_obj(self):
        """
        Creates a dictionary representation of the Recipe instance
        :return: the dictionary representation of the Recipe instance
        """
        scale_factor = self.calculate_scale_factor(self.serving_size_override)
        return {self.name: {
            'number_of_servings': self.serving_size * scale_factor,
            'ingredients': self.construct_ingredient_dict(scale_factor)}}

    def calculate_scale_factor(self, serving_size_override):
        """
        Calculates the multiplier by which to scale ingredients
        :param serving_size_override: a multiple of the standard serving size
        :return: the multiplier value
        """
        # Assuming the servings_number will multiple of self.servings_number
        scale_factor = 1
        if int(serving_size_override) % self.serving_size == 0:
            scale_factor = serving_size_override / self.serving_size
        else:
            print 'The requested serving size must be a multiple of the original serving size.'
            print 'Writing the original recipe for ' + self.name + ' as is....'

        return scale_factor
