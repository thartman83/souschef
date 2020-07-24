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
from sqlalchemy.sql import func 
from datetime import datetime

db = SQLAlchemy()

## Base ## {{{
class DBBase(db.Model):
    __abstract__ = True
    __table_args__ = {'mysql_engine':'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.Text)
    datecreated = db.Column(db.DateTime, server_default=func.now())
    datemodified = db.Column(db.DateTime, onupdate=func.now())

## }}}

## Recipe ## {{{
class Recipe(DBBase):
    __tablename__ = "recipe"
    name = db.Column(db.String(80), unique=True, nullable=False)    
    totaltime = db.Column(db.Float, nullable=False)
    preptime = db.Column(db.Float)
    cooktime = db.Column(db.Float)
    difficulty = db.Column(db.Integer)

#    ingredientLists = db.relationship('IngredientList', backref='recipe',
#                                       lazy=True)
    steplists = db.relationship('StepList', backref='recipe')
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

### StepList ## {{{
class StepList(DBBase):
    __tablename__ = "steplist"
    name = db.Column(db.String(80))
    totaltime = db.Column(db.Float)
    preptime = db.Column(db.Float)
    cooktime = db.Column(db.Float)
    order = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                          nullable= False)
    steps = db.relationship('Step', backref='steplist',
                            lazy=True)
## }}}

### Step ## {{{
class Step(DBBase):
    __tablename__ = 'step'
    name = db.Column(db.String(80))
    text = db.Column(db.Text, nullable=False)
    steplist_id = db.Column(db.Integer, db.ForeignKey('steplist.id'),
                            nullable=False)
## }}}

## }}}
