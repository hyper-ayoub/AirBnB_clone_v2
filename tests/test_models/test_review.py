from tests.test_models.test_base_model import TestBaseModel
from models.review import Review
import unittest


class TestReview(TestBaseModel):
    """ Test Review class """

    def setUp(self):
        """ Set up for the tests """
        self.model = Review
        self.name = "Review"
        self.value = Review(place_id="test_place_id", user_id="test_user_id", text="test_text")

    def test_place_id(self):
        """ Test place_id attribute """
        self.assertEqual(type(self.value.place_id), str)

    def test_user_id(self):
        """ Test user_id attribute """
        self.assertEqual(type(self.value.user_id), str)

    def test_text(self):
        """ Test text attribute """
        self.assertEqual(type(self.value.text), str)


if __name__ == '__main__':
    unittest.main()
