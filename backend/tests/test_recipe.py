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

def test_createRecipe(client, app, db):
    data = {
        "name" : "Test Recipe5",
        "author": { "firstname": "Ema",
                    "lastname": "Nymton" },
        "totaltime" : 1,
        "preptime" : 5,
        "cooktime" : 5,
        "difficulty" : 1,
        "ingredientLists": [
            {
                "name": "Ingredient list1",
                "displayorder": 1,
                "ingredients": [
                    {
                        "name": "Onion",
                        "unit": "medium",
                        "amount": 1.0,
                        "displayorder": 1,
                    },
                    {
                        "name": "Garlic",
                        "unit": "cloves",
                        "amount": 4.0,
                        "displayorder": 2,
                    }
                ]
            },
            {
                "name": "Ingredient list2",
                "displayorder": 2
            }            
        ]
    }
    
    response = client.post('/recipe', data = json.dumps(data),
                           headers = headers)

    assert response.status_code == 200

    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT COUNT(ID) as c FROM recipe')
    assert cursor.fetchone()['c'] == 1

    cursor.execute('SELECT id from recipe')
    recipe_id = cursor.fetchone()['id']

    cursor.execute('SELECT COUNT(ID) as c FROM author')
    assert cursor.fetchone()['c'] == 1

    cursor.execute('SELECT * FROM ingredientlist ORDER BY displayorder')
    row = cursor.fetchone()
    assert 'name' in row
    assert 'displayorder' in row
    assert 'recipe_id' in row

    assert row['name'] == "Ingredient list1"
    assert row['displayorder'] == 1
    assert row['recipe_id'] == recipe_id

    row = cursor.fetchone()
    assert row['name'] == "Ingredient list2"
    assert row['displayorder'] == 2
    assert row['recipe_id'] == recipe_id

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
## }}}
