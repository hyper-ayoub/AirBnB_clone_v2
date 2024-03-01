#!/usr/bin/python3
"""test for file storage"""
import unittest
from os import getenv
import MySQLdb
from models.state import State
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
class TestDBStorage(unittest.TestCase):
    """this will test the DBStorage"""

    @classmethod
    def setUpClass(self):
        """set up for test"""
        self.db = MySQLdb.connect(
            host=getenv("HBNB_MYSQL_HOST"),
            port=3306,
            user=getenv("HBNB_MYSQL_USER"),
            passwd=getenv("HBNB_MYSQL_PWD"),
            db=getenv("HBNB_MYSQL_DB"),
        )
        self.query = self.db.cursor()
        self.storage = DBStorage()

    @classmethod
    def teardown(self):
        """at the end of the test this will tear it down"""
        self.query.close()
        self.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
    def test_read_tables(self):
        """existing tables"""
        self.query.execute("SHOW TABLES")
        salida = self.query.fetchall()
        self.assertEqual(len(salida), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
    def test_no_element_user(self):
        """no elem in users"""
        self.query.execute("SELECT * FROM users")
        salida = self.query.fetchall()
        self.assertEqual(len(salida), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
    def test_no_element_cities(self):
        """no elem in cities"""
        self.query.execute("SELECT * FROM cities")
        salida = self.query.fetchall()
        self.assertEqual(len(salida), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
    def test_add(self):
        """Test same size between storage() and existing db"""
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), 0)
        state = State(name="Ebonyi")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), 1)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
    def test_all(self):
        """test if all works"""
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), len(self.storage.all(State)))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "Not db storage")
    def test_new(self):
        """test if new works"""
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), len(self.storage.all(State)))
        state = State(name="California")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        query_rows = self.query.fetchall()
        self.assertEqual(len(query_rows), len(self.storage.all(State)))


if __name__ == "__main__":
    unittest.main()
