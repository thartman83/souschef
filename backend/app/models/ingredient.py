###############################################################################
## ingredient.py for sous-chef backend models package                        ##
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
## Ingredient model for the sous-chef backend models package 
##
## }}}

### ingredient ## {{{
from .dbbase import DBBase, db

class Ingredient(DBBase):
    __tablename__ = "ingredient"
    name = db.Column(db.String(80), nullable=False)
    unit = db.Column(db.String(25), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    displayorder = db.Column(db.Integer, nullable=False)
    ingredientList_id = db.Column(db.Integer,
                                  db.ForeignKey('ingredientlist.id'),
                                  nullable=False)

    def __init__(self, name, unit, amount, displayorder, ingredientList_id):
        self.name = name
        self.unit = unit
        self.amount = amount
        self.displayorder = displayorder
        self.ingredientList_id = ingredientList_id

    def serialize(self):
        return { "name": self.name,
                 "unit": self.unit,
                 "amount": self.amount,
                 "displayorder": self.displayorder,
                 "ingredientList_id": self.ingredientList_id
                 }
                 
        
## }}}
