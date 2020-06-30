###############################################################################
## schemas.py for sous-chef backend                                          ##
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
## db schemas
##
## }}}

### schemas ## {{{
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import models

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

### RecipeSchema ## {{{
class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Recipe
        include_fk = True

    name = ma.auto_field()
    totaltime = ma.auto_field()
    preptime = ma.auto_field()
    cooktime = ma.auto_field()
    difficulty = ma.auto_field()        
## }}}

### IngredientListSchema ## {{{
class IngredientListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.IngredientList
        include_fk = True
    
## }}}

### IngredientSchema ## {{{
class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Ingredient
        include_fk = True
        
## }}}

### StepListSchema ## {{{
class StepListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Ingredient
        include_fk = True
## }}}

### StepSchema ## {{{
class StepSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Ingredient
        include_fk = True
## }}}

## }}}
