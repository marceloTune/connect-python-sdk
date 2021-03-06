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


class CatalogDiscount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, discount_type=None, percentage=None, amount_money=None, pin_required=None, label_color=None):
        """
        CatalogDiscount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'discount_type': 'str',
            'percentage': 'str',
            'amount_money': 'Money',
            'pin_required': 'bool',
            'label_color': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'discount_type': 'discount_type',
            'percentage': 'percentage',
            'amount_money': 'amount_money',
            'pin_required': 'pin_required',
            'label_color': 'label_color'
        }

        self._name = name
        self._discount_type = discount_type
        self._percentage = percentage
        self._amount_money = amount_money
        self._pin_required = pin_required
        self._label_color = label_color

    @property
    def name(self):
        """
        Gets the name of this CatalogDiscount.
        The discount's name. Searchable.

        :return: The name of this CatalogDiscount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogDiscount.
        The discount's name. Searchable.

        :param name: The name of this CatalogDiscount.
        :type: str
        """

        if not name:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def discount_type(self):
        """
        Gets the discount_type of this CatalogDiscount.
        Indicates whether the discount is a fixed amount or percentage, or entered at the time of sale. See [CatalogDiscountType](#type-catalogdiscounttype) for all possible values.

        :return: The discount_type of this CatalogDiscount.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """
        Sets the discount_type of this CatalogDiscount.
        Indicates whether the discount is a fixed amount or percentage, or entered at the time of sale. See [CatalogDiscountType](#type-catalogdiscounttype) for all possible values.

        :param discount_type: The discount_type of this CatalogDiscount.
        :type: str
        """

        self._discount_type = discount_type

    @property
    def percentage(self):
        """
        Gets the percentage of this CatalogDiscount.
        The percentage of the discount as a string representation of a decimal number, using a `.` as the decimal separator and without a `%` sign. A value of `7.5` corresponds to `7.5%`. Specify a percentage of `0` if `discount_type` is `VARIABLE_PERCENTAGE`.  Do not include this field for amount-based or variable discounts.

        :return: The percentage of this CatalogDiscount.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this CatalogDiscount.
        The percentage of the discount as a string representation of a decimal number, using a `.` as the decimal separator and without a `%` sign. A value of `7.5` corresponds to `7.5%`. Specify a percentage of `0` if `discount_type` is `VARIABLE_PERCENTAGE`.  Do not include this field for amount-based or variable discounts.

        :param percentage: The percentage of this CatalogDiscount.
        :type: str
        """

        self._percentage = percentage

    @property
    def amount_money(self):
        """
        Gets the amount_money of this CatalogDiscount.
        The amount of the discount. Specify an amount of `0` if `discount_type` is `VARIABLE_AMOUNT`.  Do not include this field for percentage-based or variable discounts.

        :return: The amount_money of this CatalogDiscount.
        :rtype: Money
        """
        return self._amount_money

    @amount_money.setter
    def amount_money(self, amount_money):
        """
        Sets the amount_money of this CatalogDiscount.
        The amount of the discount. Specify an amount of `0` if `discount_type` is `VARIABLE_AMOUNT`.  Do not include this field for percentage-based or variable discounts.

        :param amount_money: The amount_money of this CatalogDiscount.
        :type: Money
        """

        self._amount_money = amount_money

    @property
    def pin_required(self):
        """
        Gets the pin_required of this CatalogDiscount.
        Indicates whether a mobile staff member needs to enter their PIN to apply the discount to a payment in the Square Point of Sale app.

        :return: The pin_required of this CatalogDiscount.
        :rtype: bool
        """
        return self._pin_required

    @pin_required.setter
    def pin_required(self, pin_required):
        """
        Sets the pin_required of this CatalogDiscount.
        Indicates whether a mobile staff member needs to enter their PIN to apply the discount to a payment in the Square Point of Sale app.

        :param pin_required: The pin_required of this CatalogDiscount.
        :type: bool
        """

        self._pin_required = pin_required

    @property
    def label_color(self):
        """
        Gets the label_color of this CatalogDiscount.
        The color of the discount's display label in the Square Point of Sale app.

        :return: The label_color of this CatalogDiscount.
        :rtype: str
        """
        return self._label_color

    @label_color.setter
    def label_color(self, label_color):
        """
        Sets the label_color of this CatalogDiscount.
        The color of the discount's display label in the Square Point of Sale app.

        :param label_color: The label_color of this CatalogDiscount.
        :type: str
        """

        self._label_color = label_color

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
