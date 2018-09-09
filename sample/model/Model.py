import sqlite3
import unittest


class Model(object):
    _conn = None

    @staticmethod
    def connect(db):
        if not Model._conn:
            Model._conn = sqlite3.connect(db)
        else:
            Model._conn.close()
            _conn = sqlite3.connect(db)
        return Model._conn

    @staticmethod
    def get_connect():
        if Model._conn:
            return Model._conn
        else:
            raise ConnectionError('database connect not found! please connect database use Model.connect(db) method.')


class TestModel(unittest.TestCase):
    def test_get_connect(self):
        with self.assertRaises(ConnectionError, msg='connect not initial test failed!'):
            Model.get_connect()
        conn = Model.connect('person.db')
        self.assertNotEqual(conn, None, msg='connect failed!')
        self.assertEqual(Model.get_connect(), conn, msg='get_connect() test failed!')
        conn.close()


if __name__ == '__main__':
    unittest.main()
