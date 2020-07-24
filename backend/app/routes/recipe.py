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
from flask import Blueprint, request
from ..models import Recipe, db

recipe_bp = Blueprint('recipe', __name__, url_prefix='/recipe')

@recipe_bp.route('', methods=['POST'])
def addRecipe():
    recipe = Recipe(request.json['name'],
                    request.json['author'],
                    request.json['totaltime'],
                    request.json['preptime'],
                    request.json['cooktime'],
                    request.json['difficulty'])
    db.session.add(recipe)
    db.session.commit()
    ##return jsonify({"recipe", recipe.serialize()})
    return ""
## }}}
