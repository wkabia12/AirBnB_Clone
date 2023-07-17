#!/usr/bin/python3


"""
Tests for the Base Model
"""

import unittest
from models.user import User
from models.engine import file_storage


class TestUser(unittest.TestCase):

    def setUp(self):
        self.model = User()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'email'))
        self.assertTrue(hasattr(self.model, 'password'))
        self.assertTrue(hasattr(self.model, 'first_name'))
        self.assertTrue(hasattr(self.model, 'last_name'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        self.assertIsNotNone(self.model.id)
        self.assertEqual(len(self.model.id), 36)  # UUID has 36 characters

    def test_created_at(self):
        self.assertIsNotNone(self.model.created_at)

    def test_updated_at(self):
        self.assertIsNotNone(self.model.updated_at)

    def test_save_method(self):
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.model.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict['__class__'], 'User')
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(obj_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str_method(self):
        model_str = str(self.model)
        self.assertIn("[User]", model_str)
        self.assertIn("({})".format(self.model.id), model_str)


if __name__ == '__main__':
    unittest.main()
