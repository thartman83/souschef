###############################################################################
## routes.py for sous-chef backend                                          ##
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
## crud routes
##
## }}}

### routes ## {{{

from app import schemas
from app import models

def init_app(app):
    ### main ## {{{
    @app.route('/', methods = ['GET'])
    def main():
        return "Hello, Recipe"
    ## }}}

    ### Post a recipe ## {{{
    @app.route('/recipe', methods = ['POST'])
    def createRecipe():
        data = request.get_json()
        recipe_schema = schemas.RecipeSchema()
        recipe = recipe_schema.load(data)
        res = recipe_schema.dump(recipe.create())
        return make_response(jsonify({"recipe": res }), 200)
    ## }}}

## }}}
