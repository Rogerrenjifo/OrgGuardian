"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: feature_recognizer.py                                                  #
# Project: OrgGuardian                                                         #
# Last Modified: Thursday, 19th October 2023 7:32:54 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


import os
from deepface import DeepFace


responce_path = os.getenv("RESPONSES_PATH")


class FeatureRecognizer:
    @classmethod
    def recognize(self, image, options) -> list[dict]:
        """Detects features on faces in the image"""
        result = DeepFace.analyze(
            img_path=image,
            actions=options,
            enforce_detection=False,
        )
        return result

    @classmethod
    def verification(self, image_1, image_2) -> dict:
        result = DeepFace.verify(
            img1_path=image_1, img2_path=image_2, enforce_detection=False
        )
        return result

    @classmethod
    def find(self, image_1, db) -> list:
        result = DeepFace.find(image_1, db, enforce_detection=True)
        return result
