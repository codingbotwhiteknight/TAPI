# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_createnotificationsubscriptionservice_output import TapiNotificationCreatenotificationsubscriptionserviceOutput  # noqa: F401,E501
from tapi_server import util


class TapiNotificationCreateNotificationSubscriptionService(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiNotificationCreateNotificationSubscriptionService - a model defined in OpenAPI

        :param output: The output of this TapiNotificationCreateNotificationSubscriptionService.  # noqa: E501
        :type output: TapiNotificationCreatenotificationsubscriptionserviceOutput
        """
        self.openapi_types = {
            'output': TapiNotificationCreatenotificationsubscriptionserviceOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationCreateNotificationSubscriptionService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.CreateNotificationSubscriptionService of this TapiNotificationCreateNotificationSubscriptionService.  # noqa: E501
        :rtype: TapiNotificationCreateNotificationSubscriptionService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiNotificationCreateNotificationSubscriptionService.


        :return: The output of this TapiNotificationCreateNotificationSubscriptionService.
        :rtype: TapiNotificationCreatenotificationsubscriptionserviceOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiNotificationCreateNotificationSubscriptionService.


        :param output: The output of this TapiNotificationCreateNotificationSubscriptionService.
        :type output: TapiNotificationCreatenotificationsubscriptionserviceOutput
        """

        self._output = output