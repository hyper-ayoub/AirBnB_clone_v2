from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class TestReview(test_basemodel):
    """ Test Review class """

    def __init__(self, *args, **kwargs):
        """ Initialize test Review class """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test place_id attribute """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test user_id attribute """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test text attribute """
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()
