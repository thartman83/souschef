###############################################################################
## step.py for sous-chef backend models package                           ##
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
## Step model for the sous-chef model package 
##
## }}}

### step ## {{{
from .dbbase import DBBase, db

class Step(DBBase):
    __tablename__ = "step"
    text = db.Column(db.Text, nullable=False)
    displayorder = db.Column(db.Integer, nullable=False)
    steplist_id = db.Column(db.Integer, db.ForeignKey('steplist.id'))

    def __init__(self, text, displayorder, steplist_id):
        self.text = text
        self.displayorder = displayorder
        self.steplist_id = steplist_id

    def serialize(self):
        return { "text": self.text,
                 "displayorder": self.displayorder,
                 "steplist_id": self.steplist_id
        }
    
## }}}
