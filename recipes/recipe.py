from sets import Set


class Recipe:
    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    measurement_set = Set(
        ['bbl', 'cu', 'doz', 'F', 'fl', 'ft', 'gal', 'gr', 'gross',
         'in', 'lb', 'oz', 'pt', 'qt', 'sq', 'T', 't', 'tbsp',
         'tsp', 'tbs'])

    def __init__(self, name, serving_size, serving_size_override,
                 ingredients_list):
        self.name = name
        self.serving_size = int(serving_size)
        self.ingredients_list = ingredients_list
        self.serving_size_override = int(serving_size_override)

    def construct_ingredient_dict(self, scale_factor):
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
        scale_factor = self.calculate_scale_factor(self.serving_size_override)
        return {self.name: {
            'number_of_servings': self.serving_size * scale_factor,
            'ingredients': self.construct_ingredient_dict(scale_factor)}}

    def calculate_scale_factor(self, serving_size_override):
        # Assuming the servings_number will multiple of self.servings_number
        scale_factor = 1
        if int(serving_size_override) % self.serving_size == 0:
            scale_factor = serving_size_override / self.serving_size
        else:
            print 'The requested serving size must be a multiple of the original serving size.'
            print 'Writing the original recipe for ' + self.name + ' as is....'

        return scale_factor
