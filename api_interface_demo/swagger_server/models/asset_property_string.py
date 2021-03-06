# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssetPropertyString(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, property_name: str=None, asset_id: str=None, string_value: str=None):  # noqa: E501
        """AssetPropertyString - a model defined in Swagger

        :param property_name: The property_name of this AssetPropertyString.  # noqa: E501
        :type property_name: str
        :param asset_id: The asset_id of this AssetPropertyString.  # noqa: E501
        :type asset_id: str
        :param string_value: The string_value of this AssetPropertyString.  # noqa: E501
        :type string_value: str
        """
        self.swagger_types = {
            'property_name': str,
            'asset_id': str,
            'string_value': str
        }

        self.attribute_map = {
            'property_name': 'propertyName',
            'asset_id': 'assetId',
            'string_value': 'stringValue'
        }
        self._property_name = property_name
        self._asset_id = asset_id
        self._string_value = string_value

    @classmethod
    def from_dict(cls, dikt) -> 'AssetPropertyString':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssetPropertyString of this AssetPropertyString.  # noqa: E501
        :rtype: AssetPropertyString
        """
        return util.deserialize_model(dikt, cls)

    @property
    def property_name(self) -> str:
        """Gets the property_name of this AssetPropertyString.


        :return: The property_name of this AssetPropertyString.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: str):
        """Sets the property_name of this AssetPropertyString.


        :param property_name: The property_name of this AssetPropertyString.
        :type property_name: str
        """

        self._property_name = property_name

    @property
    def asset_id(self) -> str:
        """Gets the asset_id of this AssetPropertyString.


        :return: The asset_id of this AssetPropertyString.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id: str):
        """Sets the asset_id of this AssetPropertyString.


        :param asset_id: The asset_id of this AssetPropertyString.
        :type asset_id: str
        """

        self._asset_id = asset_id

    @property
    def string_value(self) -> str:
        """Gets the string_value of this AssetPropertyString.


        :return: The string_value of this AssetPropertyString.
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value: str):
        """Sets the string_value of this AssetPropertyString.


        :param string_value: The string_value of this AssetPropertyString.
        :type string_value: str
        """

        self._string_value = string_value
