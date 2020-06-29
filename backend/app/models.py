###############################################################################
## models.py for sous-chef backend                                          ##
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
## DB models for the sous-chef backend
##
## }}}

### models ## {{{

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

## Base ## {{{
class DBBase(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.Text)
    datecreated = db.Column(db.DateTime, default=datetime.utcnow)
    datemodified = db.Column(db.DateTime, onupdate=datetime.utcnow)

## }}}

## Recipe ## {{{
class Recipe(DBBase):
    __tablename__ = "recipe"
    name = db.Column(db.String(80), unique=True, nullable=False)
    ingredientLists = db.relationship('IngredientList', backref='recipe',
                                       lazy=True)
## }}}

## IngredientList ## {{{
class IngredientList(DBBase):
    __tablename__ = "ingredientlist"
    name = db.Column(db.String(80))
    order = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                          nullable=False)
    ingredients = db.relationship('Ingredient', backref='recipe',
                                   lazy=True)
## }}}

## Ingredient ## {{{
class Ingredient(DBBase):
    __tablename__ = "ingredient"
    name = db.Column(db.String(80))
    unit = db.Column(db.String(25), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    ingredientList_id = db.Column(db.Integer,
                                  db.ForeignKey('ingredientlist.id'),
                                  nullable=False)
## }}}

## }}}
