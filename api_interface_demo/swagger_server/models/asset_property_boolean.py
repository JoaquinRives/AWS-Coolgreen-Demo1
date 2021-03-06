# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssetPropertyBoolean(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, property_name: str=None, asset_id: str=None, integer_value: bool=None):  # noqa: E501
        """AssetPropertyBoolean - a model defined in Swagger

        :param property_name: The property_name of this AssetPropertyBoolean.  # noqa: E501
        :type property_name: str
        :param asset_id: The asset_id of this AssetPropertyBoolean.  # noqa: E501
        :type asset_id: str
        :param integer_value: The integer_value of this AssetPropertyBoolean.  # noqa: E501
        :type integer_value: bool
        """
        self.swagger_types = {
            'property_name': str,
            'asset_id': str,
            'integer_value': bool
        }

        self.attribute_map = {
            'property_name': 'propertyName',
            'asset_id': 'assetId',
            'integer_value': 'integerValue'
        }
        self._property_name = property_name
        self._asset_id = asset_id
        self._integer_value = integer_value

    @classmethod
    def from_dict(cls, dikt) -> 'AssetPropertyBoolean':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssetPropertyBoolean of this AssetPropertyBoolean.  # noqa: E501
        :rtype: AssetPropertyBoolean
        """
        return util.deserialize_model(dikt, cls)

    @property
    def property_name(self) -> str:
        """Gets the property_name of this AssetPropertyBoolean.


        :return: The property_name of this AssetPropertyBoolean.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: str):
        """Sets the property_name of this AssetPropertyBoolean.


        :param property_name: The property_name of this AssetPropertyBoolean.
        :type property_name: str
        """

        self._property_name = property_name

    @property
    def asset_id(self) -> str:
        """Gets the asset_id of this AssetPropertyBoolean.


        :return: The asset_id of this AssetPropertyBoolean.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id: str):
        """Sets the asset_id of this AssetPropertyBoolean.


        :param asset_id: The asset_id of this AssetPropertyBoolean.
        :type asset_id: str
        """

        self._asset_id = asset_id

    @property
    def integer_value(self) -> bool:
        """Gets the integer_value of this AssetPropertyBoolean.


        :return: The integer_value of this AssetPropertyBoolean.
        :rtype: bool
        """
        return self._integer_value

    @integer_value.setter
    def integer_value(self, integer_value: bool):
        """Sets the integer_value of this AssetPropertyBoolean.


        :param integer_value: The integer_value of this AssetPropertyBoolean.
        :type integer_value: bool
        """

        self._integer_value = integer_value
