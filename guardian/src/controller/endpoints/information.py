"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: information.py                                                         #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 1:38:49 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import Resource, Namespace
from guardian.src.model.personal_information.roger import Roger
from guardian.src.controller.output_models import information_model


ns = Namespace("roger_information", description="This endpoint returns my information")


@ns.route("/")
class FacialAttributes(Resource):
    @ns.marshal_list_with(information_model)
    def get(self):
        return Roger()
