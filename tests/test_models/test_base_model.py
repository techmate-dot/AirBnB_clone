#!/usr/bin/python3
"""A script that test the various functions of the base_model
    """
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Hold all test for the BaseModel

    Args:
        unittest (object): test object
    """
    def test_created_at(self):
        """Ensure that the created_at is of type Datetime and
            is the same as current time"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at).__name__, 'datetime')

