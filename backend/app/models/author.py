###############################################################################
## author.py for sous-chef backend models package                           ##
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
## Author model for sous-chef backend models package
##
## }}}

### author ## {{{
from .dbbase import DBBase, db

class Author(DBBase):
    __tablename__ = "author"
    firstname = db.Column(db.String(40),  nullable=False)
    lastname  = db.Column(db.String(40),  nullable=False)
    fullname  = db.Column(db.String(100), nullable=False)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname
        self.fullname  = firstname + " " + lastname

    def serialize(self):
        return { "firstname": self.firstname,
                 "lastname":  self.firstname,
                 "fullname":  self.fullname }
    
## }}}
