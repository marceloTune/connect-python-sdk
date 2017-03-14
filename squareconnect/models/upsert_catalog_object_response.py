# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class UpsertCatalogObjectResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, catalog_object=None):
        """
        UpsertCatalogObjectResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[Error]',
            'catalog_object': 'CatalogObject'
        }

        self.attribute_map = {
            'errors': 'errors',
            'catalog_object': 'catalog_object'
        }

        self._errors = errors
        self._catalog_object = catalog_object

    @property
    def errors(self):
        """
        Gets the errors of this UpsertCatalogObjectResponse.
        The set of [Error](#type-error)s encountered.

        :return: The errors of this UpsertCatalogObjectResponse.
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this UpsertCatalogObjectResponse.
        The set of [Error](#type-error)s encountered.

        :param errors: The errors of this UpsertCatalogObjectResponse.
        :type: list[Error]
        """

        self._errors = errors

    @property
    def catalog_object(self):
        """
        Gets the catalog_object of this UpsertCatalogObjectResponse.
        The created [CatalogObject](#type-catalogobject).

        :return: The catalog_object of this UpsertCatalogObjectResponse.
        :rtype: CatalogObject
        """
        return self._catalog_object

    @catalog_object.setter
    def catalog_object(self, catalog_object):
        """
        Sets the catalog_object of this UpsertCatalogObjectResponse.
        The created [CatalogObject](#type-catalogobject).

        :param catalog_object: The catalog_object of this UpsertCatalogObjectResponse.
        :type: CatalogObject
        """

        self._catalog_object = catalog_object

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other