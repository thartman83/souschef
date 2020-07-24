###############################################################################
## base.py for sous-chef backend                                             ##
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
## base model class
##
## }}}

### libraries ## {{{
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 
from datetime import datetime
## }}}

### db ## {{{
db = SQLAlchemy()
## }}}

### DBBase ## {{{
class DBBase(db.Model):
    __abstract__   = True
    __table_args__ = {'mysql_engine':'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.Text)
    datecreated = db.Column(db.DateTime, server_default=func.now())
    datemodified = db.Column(db.DateTime, server_default=func.now())    
## }}}
