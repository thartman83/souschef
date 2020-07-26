###############################################################################
## conftest.py for sous-chef backend testing                                  ##
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
## configuration testing
##
## }}}

### conftest ## {{{
import os
import tempfile

import pytest
import mysql.connector
from os import environ, path
from dotenv import load_dotenv
from app.appfactory import create_app

testdir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(testdir, '../config/.testenv'))

mysqlconfig = { 'user': environ.get('mysqluser'),
                'password': environ.get('mysqlpasswd'),
                'host': environ.get('mysqlhost'),
                'database': environ.get('mysqldb'),
}

@pytest.fixture
def app():
    app = create_app('config.test.Config')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def db():
    db = mysql.connector.MySQLConnection(**mysqlconfig)
    return db
## }}}
