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
from ..models import Recipe, Author, db

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
    
## }}}
