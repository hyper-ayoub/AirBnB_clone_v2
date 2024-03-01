#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """this will test the User class"""

    @classmethod
    def setUpClass(c):
        """set up for test"""
        c.user = User()
        c.user.first_name = "Kevin"
        c.user.last_name = "Yook"
        c.user.email = "yook00627@gmamil.com"
        c.user.password = "secret"

    @classmethod
    def teardown(c):
        """at the end of the test this will tear it down"""
        del c.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_user(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_user(self):
        """chekcing if User have attributes"""
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("id" in self.user.__dict__)
        self.assertTrue("created_at" in self.user.__dict__)
        self.assertTrue("updated_at" in self.user.__dict__)
        self.assertTrue("password" in self.user.__dict__)
        self.assertTrue("first_name" in self.user.__dict__)
        self.assertTrue("last_name" in self.user.__dict__)

    def test_is_subclass_user(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_user(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Not file engine")
    def test_save_user(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_user(self):
        """test if dictionary works"""
        self.assertEqual("to_dict" in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
