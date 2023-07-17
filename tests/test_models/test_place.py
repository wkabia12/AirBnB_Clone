#!/usr/bin/python3


"""
Tests for the Base Model
"""

import unittest
from models.place import Place
from models.engine import file_storage


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.model = Place()

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'city_id'))
        self.assertTrue(hasattr(self.model, 'user_id'))
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'descriptions'))
        self.assertTrue(hasattr(self.model, 'number_rooms'))
        self.assertTrue(hasattr(self.model, 'number_bathrooms'))
        self.assertTrue(hasattr(self.model, 'max_guest'))
        self.assertTrue(hasattr(self.model, 'price_by_night'))
        self.assertTrue(hasattr(self.model, 'latitude'))
        self.assertTrue(hasattr(self.model, 'longitude'))
        self.assertTrue(hasattr(self.model, 'amenity_ids'))
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
        self.assertEqual(obj_dict['__class__'], 'Place')
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(obj_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str_method(self):
        model_str = str(self.model)
        self.assertIn("[Place]", model_str)
        self.assertIn("({})".format(self.model.id), model_str)


if __name__ == '__main__':
    unittest.main()
