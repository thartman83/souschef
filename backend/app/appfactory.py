###############################################################################
## appfactory.py for sous-chef backend                                          ##
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
## Factory functions for creating applications
##
## }}}

### appfactory ## {{{
from flask import Flask, g
from .models import db
from .routes import bp, recipe_bp

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from app.models import db
    from app.routes import recipe_bp

    db.init_app(app)
    app.register_blueprint(recipe_bp)

    @app.before_first_request
    def setup():
        with app.app_context():
            db.drop_all()
            db.create_all()

    return app

## }}}
