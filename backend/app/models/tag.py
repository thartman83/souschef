###############################################################################
## tag.py for sous-chef backend models package                           ##
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
## Tag model for sous-chef models package 
##
## }}}

### tag ## {{{
from .dbbase import DBBase, db

class Tag(DBBase):
    __tablename__ = "tag"
    name = db.Column(db.String(20), nullable=False)
    recipes = db.relationship('Tag', secondary='tagxrecipe')

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            "name": self.name
        }

class TagXRecipe(db.Model):
    __tablename__ = 'tagxrecipe'
    __table_args__ = {'mysql_engine':'InnoDB'}
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                          primary_key=True)
## }}}
