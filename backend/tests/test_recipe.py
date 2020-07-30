###############################################################################
## test_recipe.py for sous-chef backend testing                                  ##
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
## test methods for the recipe routes and models in the sous-chef backend
##
## }}}

### test_recipe ## {{{
from app.appfactory import create_app
import json

headers = { "Content-Type": "application/json" }

def test_createRecipe(client, app, db, gooddata):    
    response = client.post('/recipe', data = json.dumps(gooddata),
                           headers = headers)

    assert response.status_code == 200

    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT COUNT(ID) as c FROM recipe')
    assert cursor.fetchone()['c'] == 1

    cursor.execute('SELECT id from recipe')
    recipe_id = cursor.fetchone()['id']

    cursor.execute('SELECT COUNT(ID) as c FROM author')
    assert cursor.fetchone()['c'] == 1

    validateIngredientLists(cursor, recipe_id)
    validateStepList(cursor, recipe_id)
    validateTags(cursor, recipe_id)

def validateIngredientLists(cursor, recipe_id):
    cursor.execute('SELECT * FROM ingredientlist ORDER BY displayorder')
    row = cursor.fetchone()
    assert 'name' in row
    assert 'displayorder' in row
    assert 'recipe_id' in row

    assert row['name'] == "Ingredient list1"
    assert row['displayorder'] == 1
    assert row['recipe_id'] == recipe_id

    ingredientlist_id = row['id']

    row = cursor.fetchone()
    assert row['name'] == "Ingredient list2"
    assert row['displayorder'] == 2
    assert row['recipe_id'] == recipe_id
    validateIngredients(cursor, ingredientlist_id)

def validateIngredients(cursor, ingredientlist_id):
    cursor.execute('SELECT * FROM ingredient ORDER BY displayorder')
    row = cursor.fetchone()
        
    assert row['name'] == "Onion"
    assert row['unit'] == "medium"
    assert row['amount'] == 1.0
    assert row['displayorder'] == 1


    row = cursor.fetchone()
    assert row['name'] == "Garlic"
    assert row['unit'] == "cloves"
    assert row['amount'] == 4
    assert row['displayorder'] == 2

def validateStepList(cursor, recipe_id):
    cursor.execute("""SELECT * FROM steplist where recipe_id = %i ORDER BY 
displayorder""" % recipe_id)
    row = cursor.fetchone()

    assert row['name'] == 'Step 1 Title'
    assert row['totaltime'] == 1
    assert row['preptime'] == 1
    assert row['cooktime'] == 1
    assert row['displayorder'] == 1
    assert row['recipe_id'] == recipe_id

    steplist_id = row['id']

    row = cursor.fetchone()
    assert row['name'] == 'Step 2 Title'
    assert row['totaltime'] == 2
    assert row['preptime'] == 2
    assert row['cooktime'] == 2
    assert row['displayorder'] == 2
    assert row['recipe_id'] == recipe_id
    validateSteps(cursor, steplist_id)

def validateSteps(cursor, steplist_id):
    cursor.execute("""SELECT * FROM step where steplist_id = %i ORDER BY
displayorder""" % steplist_id)

    row = cursor.fetchone()
    assert row['text'] == 'This is the first step'
    assert row['displayorder'] == 1
    assert row['steplist_id'] == steplist_id

    row = cursor.fetchone()
    assert row['text'] == 'This is the second step'
    assert row['displayorder'] == 2
    assert row['steplist_id'] == steplist_id

    row = cursor.fetchone()
    assert row['text'] == 'This is the third step'
    assert row['displayorder'] == 3
    assert row['steplist_id'] == steplist_id

def validateTags(cursor, recipe_id):
    cursor.execute("""SELECT name, tag_id, recipe_id FROM tag 
inner join tagxrecipe on tag.id = tagxrecipe.tag_id 
WHERE recipe_id = %i""" % recipe_id)

    row = cursor.fetchone()
    assert row['name'] in ['tag1', 'tag2']
    assert row['tag_id'] in [1, 2]

    row = cursor.fetchone()
    assert row['name'] in ['tag1', 'tag2']
    assert row['tag_id'] in [1,2]
## }}}
