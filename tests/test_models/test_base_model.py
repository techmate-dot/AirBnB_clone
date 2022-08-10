#!/usr/bin/python3
"""A script that test the various functions of the base_model
    """
import unittest
from models.base_model import BaseModel
import time

my_model = BaseModel()


class TestBaseModel(unittest.TestCase):
    """ Hold all test for the BaseModel

    Args:
        unittest (object): test object
    """
    def test_created_at(self):
        """Ensure that the created_at is of type Datetime and
            is the same as current time"""
        self.assertEqual(type(my_model.created_at).__name__, 'datetime')

    def test_updated_at(self):
        """Ensure that the updated_at is of type Datetime and is
            not equals created_at
        """
        my_model.save()
        self.assertEqual(type(my_model.updated_at).__name__, 'datetime')
        self.assertFalse(my_model.created_at is my_model.updated_at)

    def test_new_instance(self):
        """Check to see that a new instance has been made
        """
        my_new_model = BaseModel(my_model.to_dict)
        self.assertFalse(my_model is my_new_model)
        self.assertFalse(my_model.id is my_new_model.id)

    def test_to_dict(self):
        """check to_dic returns a type dict
        """
        new_dict = my_model.to_dict()
        self.assertTrue(new_dict['__class__'], 'BaseModel')
        self.assertTrue(new_dict['created_at'],
                               my_model.created_at.isoformat())
        self.assertTrue(new_dict['updated_at'],
                               my_model.updated_at.isoformat())

    def test_str(self):
        """checks if a string representation  of the class is returned"""
        my_model =  BaseModel()
        st = my_model.__str__()
        self.assertAlmostEqual(st, str(my_model))
        self.assertAlmostEqual(st[0:11], '[BaseModel]')
        self.assertIsInstance(st, str)

    def test_saves(self):
        old_time = my_model.updated_at
        my_model.save()
        new_time = my_model.updated_at
        self.assertFalse(old_time == new_time)
        self.assertNotEqual(old_time, new_time)
