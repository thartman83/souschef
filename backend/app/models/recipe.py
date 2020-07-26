###############################################################################
## recipe.py for sous-chef backend                                           ##
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
## recipe model
##
## }}}

### libraries ## {{{
from .dbbase import DBBase, db
from .ingredientList import IngredientList
## }}}

### recipe ## {{{
class Recipe(DBBase):
    __tablename__ = "recipe"
    name = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    totaltime = db.Column(db.Float, nullable=False)
    preptime = db.Column(db.Float)
    cooktime = db.Column(db.Float)
    difficulty = db.Column(db.Integer)
    ingredientLists = db.relationship('IngredientList')

    def __init__(self, name, author, totaltime, preptime, cooktime, difficulty):
        self.name = name
        self.author = totaltime
        self.totaltime = totaltime
        self.preptime = preptime
        self.cooktime = cooktime
        self.difficulty = difficulty

    def serialize(self):
        return { "name": self.name,
                 "author": self.author,
                 "totaltime": self.totaltime,
                 "preptime": self.preptime,
                 "cooktime": self.cooktime,
                 "difficulty": self.difficulty,
                 "ingredientLists": list(map(IngredientList.serialize,
                                             self.ingredientLists))
        }

## }}}
