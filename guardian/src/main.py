"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: main.py                                                                #
# Project: OrgGuardian                                                         #
# Last Modified: Thursday, 19th October 2023 3:01:44 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask import Flask
from guardian.src.configuration import api, database, port, host
from guardian.src.controller.endpoints.facial_attributes import ns as facial_attributes
from guardian.src.controller.endpoints.information import ns as information

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
api.init_app(app)
database.init_app(app)
api.add_namespace(information)
api.add_namespace(facial_attributes)

if __name__ == "__main__":
    app.run(host=host, port=port)
