"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: facial_attributes.py                                                   #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 1:38:39 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import Resource, Namespace


ns = Namespace(
    "facial_attributes", description="the facial attributes will be implemented"
)


@ns.route("/facial_attributes")
class FacialAttributes(Resource):
    def post(self) -> dict:
        return "TO DO: in process to be implemented"

    def get(self):
        return "hello world"
