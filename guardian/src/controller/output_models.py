"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: output_models.py                                                       #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 1:38:26 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import fields
from guardian.src.configuration import api


information_model = api.model(
    "Roger", {"name": fields.String, "linkedin": fields.String, "email": fields.String}
)
