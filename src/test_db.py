import unittest
import tempfile
from database import Database

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.database_file = tempfile.NamedTemporaryFile(delete=False)

    def setUp(self):
        self.db = Database(self.database_file.name)

    def test_db_connects(self):
        self.assertTrue(self.db.conn is not None)

    def xtest_insert(self):
        pass

    def xtest_delete(self):
        pass

    def xtest_update(self):
        pass



if __name__ == '__main__':
    unittest.main()