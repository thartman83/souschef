###############################################################################
## recipe.py for sous-chef backend routes package                           ##
## Copyright (c) 2020 Tom Hartman (thomas.lees.hartman@gmail.com)            ##
##                                                                           ##
## This program is free software; you can redistribute it and/or             ##
## modify it under the terms of the GNU General Public License               ##
## as published by the Free Software Foundation; either version 2            ##
## of the License, or the License, or (at your option) any later             ##
## version.                                                                  ##
##                                                                           ##
## This program is distributed in the hope that it will be useful,           ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of            ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             ##
## GNU General Public License for more details.                              ##
###############################################################################

### Commentary ## {{{
##
## recipe routes for the sous-chef backend routes package
##
## }}}

### recipe ## {{{
from flask import Blueprint, request, jsonify
from ..models import (Recipe, Author, IngredientList, Ingredient, StepList,
                      Step, Tag, db)

recipe_bp = Blueprint('recipe', __name__, url_prefix='/recipe')

@recipe_bp.route('', methods=['POST'])
def createRecipe():
    author = getCreateAuthor(request.json['author'])    

    if author is None:
        return "Author information was malformed", 422
    
    recipe = Recipe(request.json['name'],
                    author,
                    request.json['totaltime'],
                    request.json['preptime'],
                    request.json['cooktime'],
                    request.json['difficulty'])
    db.session.add(recipe)
    db.session.flush()

    for i in request.json['ingredientLists']:
        ingredientList_id = createIngredientList(i, recipe.id)
        if ingredientList_id is None:
            return "IngredientList was malformed", 422

        if 'ingredients' in i:
            for j in i['ingredients']:
                ingredient_id = createIngredient(j, ingredientList_id)

                if ingredient_id is None:
                    return "Ingredient was malformed", 422

    for s in request.json['stepLists']:
        stepList_id = createStepList(s, recipe.id)
        if stepList_id is None:
            return "StepList was malformed", 422

        for t in s['steps']:
            step_id = createStep(t, stepList_id)

            if step_id is None:
                return "Step was malformed", 422

    if "tags" in request.json:
        for t in request.json['tags']:
            tag = getCreateTag(t, recipe)

            if tag is None:
                return "Tag data was malformed", 422        

    db.session.commit()
    return jsonify({"recipe": recipe.serialize()})

def getCreateAuthor(author):
    if type(author) is int:
        ret = Author.query.filter_by(id=author).first()
        if ret is None: #author id was not found in database
            return None 
        else:
            return ret.id
    elif type(author) is dict: 
        if 'firstname' in author and 'lastname' in author:
            id = authorExists(author['firstname'], author['lastname'])
            
            if id is None: # create a new author since it doesn't exist         
                author = Author(author['firstname'], author['lastname'])
                db.session.add(author)
                db.session.flush()
                return author.id
            else: # author already exists in the database return the id
                return id
        else: # No firstname or lastname
            return None
    else: # author information was not an integer or dict
        return None

def authorExists(firstname, lastname):
    return Author.query.filter_by(firstname=firstname, lastname=lastname).first()

def createIngredientList(ingredientList, recipe_id):
    if not 'name' in ingredientList or not 'displayorder' in ingredientList:
        return None

    ret = IngredientList(ingredientList['name'],
                         ingredientList['displayorder'],
                         recipe_id)
    db.session.add(ret)
    db.session.flush()
    return ret.id

def createIngredient(ingredient, ingredientList_id):
    if not 'name' in ingredient or not 'unit' in ingredient or \
       not 'amount' in ingredient or not 'displayorder' in ingredient:
        return None

    ret = Ingredient(ingredient['name'], ingredient['unit'], ingredient['amount'],
                     ingredient['displayorder'], ingredientList_id)
    db.session.add(ret)
    db.session.flush()
    return ret.id

def createStepList(steplist, recipe_id):
    if not 'displayorder' in steplist:
        return None

    ret = StepList(steplist.get('name'),
                   steplist.get('totaltime'),
                   steplist.get('preptime'),
                   steplist.get('cooktime'),
                   steplist.get('displayorder'),
                   recipe_id)
    db.session.add(ret)
    db.session.flush()
    return ret.id

def createStep(step, steplist_id):
    if not 'text' in step or not 'displayorder' in step:
        return None

    ret = Step(step['text'], step['displayorder'], steplist_id)
    db.session.add(ret)
    db.session.flush()
    return ret.id
        

def getCreateTag(tag, recipe):
    if not 'name' in tag:
        return None

    t = Tag(tag['name'])
    db.session.add(t)
    
    recipe.tags.append(t)
    return t


## }}}
