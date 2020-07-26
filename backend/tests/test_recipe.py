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
        "difficulty" : 1
    }
    
    response = client.post('/recipe', data = json.dumps(data),
                           headers = headers)

    assert response.status_code == 200

    cursor = db.cursor()
    cursor.execute('SELECT COUNT(ID) FROM recipe')
    assert cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(ID) FROM author')
    assert cursor.fetchone()[0]
## }}}
