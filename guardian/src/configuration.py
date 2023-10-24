"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: configuration.py                                                       #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 1:36:46 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from os import getenv
from dotenv import load_dotenv
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

port = int(getenv("PORT_ML", 80))
host = str(getenv("HOST_ML", "0.0.0.0"))

api = Api()
database = SQLAlchemy()
