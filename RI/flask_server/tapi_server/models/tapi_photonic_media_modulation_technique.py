# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiPhotonicMediaModulationTechnique(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    RZ = "RZ"
    NRZ = "NRZ"
    BPSK = "BPSK"
    DPSK = "DPSK"
    QPSK = "QPSK"
    _8QAM = "8QAM"
    _16QAM = "16QAM"
    PAM4 = "PAM4"
    PAM8 = "PAM8"
    UNDEFINED = "UNDEFINED"

    def __init__(self):  # noqa: E501
        """TapiPhotonicMediaModulationTechnique - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaModulationTechnique':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.ModulationTechnique of this TapiPhotonicMediaModulationTechnique.  # noqa: E501
        :rtype: TapiPhotonicMediaModulationTechnique
        """
        return util.deserialize_model(dikt, cls)