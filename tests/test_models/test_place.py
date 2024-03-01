#!/usr/bin/python3
"""test for place"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(c):
        """set up for test"""
        c.place = Place()
        c.place.city_id = "1234-abcd"
        c.place.user_id = "4321-dcba"
        c.place.name = "Death Star"
        c.place.description = "UNLIMITED POWER!!!!!"
        c.place.number_rooms = 1000000
        c.place.number_bathrooms = 1
        c.place.max_guest = 607360
        c.place.price_by_night = 10
        c.place.latitude = 160.0
        c.place.longitude = 120.0
        c.place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def teardown(c):
        """at the end of the test this will tear it down"""
        del c.place

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_place(self):
        """checking for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue("id" in self.place.__dict__)
        self.assertTrue("created_at" in self.place.__dict__)
        self.assertTrue("updated_at" in self.place.__dict__)
        self.assertTrue("city_id" in self.place.__dict__)
        self.assertTrue("user_id" in self.place.__dict__)
        self.assertTrue("name" in self.place.__dict__)
        self.assertTrue("description" in self.place.__dict__)
        self.assertTrue("number_rooms" in self.place.__dict__)
        self.assertTrue("number_bathrooms" in self.place.__dict__)
        self.assertTrue("max_guest" in self.place.__dict__)
        self.assertTrue("price_by_night" in self.place.__dict__)
        self.assertTrue("latitude" in self.place.__dict__)
        self.assertTrue("longitude" in self.place.__dict__)
        self.assertTrue("amenity_ids" in self.place.__dict__)

    def test_is_subclass_place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types_place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Not file engine")
    def test_save_place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_place(self):
        """test if dictionary works"""
        self.assertEqual("to_dict" in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
