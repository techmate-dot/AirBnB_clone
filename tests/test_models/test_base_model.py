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

    def test_updated_at(self):
        """Ensure that the updated_at is of type Datetime and is
            not equals created_at
        """
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(type(my_model.updated_at).__name__, 'datetime')
        self.assertFalse(my_model.created_at is my_model.updated_at)
