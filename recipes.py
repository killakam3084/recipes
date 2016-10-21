#!/usr/bin/env python

import os
import json
from recipe import Recipe
import argparse

'''Globals'''
serving_size_override = ''
filter_ingredients = []


def split_cmdline_filter_items(string):
    filter_items = string.split(',')
    return filter_items


def parse_arguments():
    global parser
    parser = argparse.ArgumentParser(
        description='A vanilla program to convert flat text recipes to json',
        epilog='Certainly this isn\'t how Food Network does it')
    parser.add_argument('-s', '--serving-size', type=str,
                        help='The number of servings you\'d like to make.',
                        dest='serving_size')
    parser.add_argument('-f', '--filter-items', type=split_cmdline_filter_items,
                        dest='filter_items',
                        help='Enter a comma delimited string of ingredients to filter recipes by.')
    global args
    args = parser.parse_args()

    global serving_size_override
    serving_size_override = args.serving_size
    global filter_ingredients
    filter_ingredients = args.filter_items


def construct_list_of_recipes():
    fn = os.path.join(os.path.dirname(__file__), './recipe_files/recipe_0.txt')
    sub_list = []
    with open(fn, 'r') as f:
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


def construct_recipe_object(recipe):
    recipe_name = recipe[0]
    serving_number_string = recipe[1].split(' ')
    recipe_serving_size = serving_number_string[1]
    recipe_ingredients_list = [recipe[i] for i in range(2, len(recipe))]
    if serving_size_override:
        recipe_obj = Recipe(recipe_name, recipe_serving_size,
                            serving_size_override,
                            recipe_ingredients_list)
    else:
        recipe_obj = Recipe(recipe_name, recipe_serving_size,
                            recipe_serving_size,
                            recipe_ingredients_list)
    return recipe_obj


def construct_json_object(recipe_obj):
    return recipe_obj.construct_json_rep_obj()


def construct_output_dict():
    list_of_recipes = construct_list_of_recipes()
    output_dict = {}
    for recipe_list in list_of_recipes:
        recipe_obj = construct_recipe_object(recipe_list)
        recipe_json_obj = construct_json_object(recipe_obj)
        for k, v in recipe_json_obj.iteritems():
            output_dict[k] = v
    output_dict = filter_output_dict(output_dict)
    return {'recipes': output_dict}


def filter_output_dict(output_dict):
    global filter_ingredients
    if filter_ingredients:
        filtered_dict = {k: v for k, v in
                         output_dict.iteritems() if
                         all(ingredient in v['ingredients'] for ingredient in
                             filter_ingredients)}
        return filtered_dict
    else:
        return output_dict


def dump_output_object(output_obj):
    fn = os.path.join(os.path.dirname(__file__), './recipe_files/recipes.json')
    with open(fn, 'w') as outfile:
        json.dump(obj=output_obj, fp=outfile, indent=4)


parse_arguments()
output_obj = construct_output_dict()
dump_output_object(output_obj)
