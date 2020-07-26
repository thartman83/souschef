###############################################################################
## ingredientList.py for sous-chef backend models package                    ##
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
## IngredientList model for the sous-chef backend
##
## }}}

### ingredientList ## {{{
from .dbbase import DBBase, db
from .ingredient import Ingredient

class IngredientList(DBBase):
    __tablename__ = "ingredientlist"
    name      = db.Column(db.String(80))
    displayorder     = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                          nullable=False)
    ingredients = db.relationship('Ingredient')

    def __init__(self, name, order, recipe_id):
        self.name = name
        self.displayorder = order
        self.recipe_id = recipe_id

    def serialize(self):
        return { "name": self.name,
                 "displayorder": self.displayorder,
                 "recipe_id": self.recipe_id,
                 "ingredients": list(map(Ingredient.serialize, self.ingredients))
        }
    

## }}}
