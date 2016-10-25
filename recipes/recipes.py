#!/usr/bin/env python
import json
import argparse
import textwrap

import recipe


def split_cmdline_filter_items(string):
    """
        Helper function to handle filtered items comma delimited string

        :param string: the comma delimited string to split
        :return: the list of tokens after string split
    """
    filter_items = string.split(',')
    return filter_items


def parse_arguments():
    """
        Method to parse commandline arguments of serving size and filter items

        :return: return nothing
    """
    global parser
    parser = argparse.ArgumentParser(
        description='Certainly this isn\'t how Food Network does it',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
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
    '''))
    parser.add_argument('input_file',
                        help="An input text file to read in recipes from. "
                             "Must adhere certain structure.**")
    parser.add_argument('out_file', help="File to write json recipe data to.")
    parser.add_argument('-s', '--serving-size', type=str,
                        help='The number of servings you\'d like to make.',
                        dest='serving_size', default=4)
    parser.add_argument('-f', '--filter-items', type=split_cmdline_filter_items,
                        dest='filter_items',
                        help='A comma delimited string of ingredients to filter recipes by. '
                             'Multi-word ingredients must be quoted.')
    global args
    args = parser.parse_args()

    global serving_size_override
    serving_size_override = args.serving_size
    global filter_ingredients
    filter_ingredients = args.filter_items


def construct_list_of_recipes():
    """
        Function to parse txt file of recipes and construct 2-D list tokenizing
        each of the recipes metadata and ingredient content

        :return: returns the 2-D list of lists of recipe(s) tokens
    """
    sub_list = []
    with open(args.input_file, 'r') as f:
        lines = [line if line == '\n' else line.rstrip('\n') for line in f]

    recipes_list = []
    for element in lines:
        if element == '\n':
            recipes_list.append(sub_list)
            sub_list = []
        else:
            sub_list.append(element)
    recipes_list.append(sub_list)
    return recipes_list


def construct_recipe_object(recipes_list):
    """
        Digs the relevant information from the list of list or recipe tokens:
        name, serving size, ingredient list.

        :param recipes_list: The list of list of recipes tokens
        :return: An instance of a Recipe
    """
    recipe_name = recipes_list[0]
    serving_number_string = recipes_list[1].split(' ')
    recipe_serving_size = serving_number_string[1]
    recipe_ingredients_list = [recipes_list[i] for i in
                               range(2, len(recipes_list))]
    if serving_size_override:
        recipe_obj = recipe.Recipe(recipe_name, recipe_serving_size,
                                   serving_size_override,
                                   recipe_ingredients_list)
    else:
        recipe_obj = recipe.Recipe(recipe_name, recipe_serving_size,
                                   recipe_serving_size,
                                   recipe_ingredients_list)
    return recipe_obj


def filter_output_dict(output_dict):
    """
    Function to construct a new output_dict excluding recipes with
    filter_ingredients

    :param output_dict: the filtered list if there exists items to filter by
    :return: the filtered list
    """
    global filter_ingredients
    if filter_ingredients:
        filtered_dict = {k: v for k, v in
                         output_dict.iteritems() if
                         all(filter_item in v['ingredients']
                             for filter_item in filter_ingredients)}
        return filtered_dict
    else:
        return output_dict


def construct_output_dict():
    """
    Iterate over the recipes and wrap them into a output dict

    :return: the output dictionary
    """
    list_of_recipes = construct_list_of_recipes()
    output_dict = {}
    for recipe_list in list_of_recipes:
        recipe_instance = construct_recipe_object(recipe_list)
        recipe_dict = recipe_instance.construct_json_rep_obj()
        for k, v in recipe_dict.iteritems():
            output_dict[k] = v
    output_dict = filter_output_dict(output_dict)
    return {'recipes': output_dict}


def dump_output_object(output_obj):
    """
    Encodes to json and dumps

    :param output_obj: the python of recipes to be encoded to json
    :return: return nothing
    """
    with open(args.out_file, 'w') as outfile:
        json.dump(obj=output_obj, fp=outfile, indent=4)


parse_arguments()
output_obj = construct_output_dict()
dump_output_object(output_obj)
