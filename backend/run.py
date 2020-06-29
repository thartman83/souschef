###############################################################################
## app.py for sous chef backend                                              ##
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
## 
##
## }}}

### app ## {{{
import os
from flask import Flask
from app.models import db
import config

class App:
    def __init__(self):
        self.db = db
        self.app = Flask(__name__, instance_relative_config=True)
        self.app.config.from_object('config.dev.Config')        
        self.db.init_app(self.app)

    def createTables(self):
        with self.app.app_context():
            self.db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0:5000')
## }}}
