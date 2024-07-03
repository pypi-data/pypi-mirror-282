import unittest
from rabbitstore import RabbitStore

class TestRabbitStore(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.username = 'guest'
        self.password = 'guest'
        self.key = 'test_key'
        self.value = {'data': 'value'}

    def test_set_get(self):
        RabbitStore.set(self.key, self.value, host=self.host, username=self.username, password=self.password)
        result = RabbitStore.get(self.key, host=self.host, username=self.username, password=self.password)
        self.assertEqual(result, self.value)

    def test_remove(self):
        RabbitStore.set(self.key, self.value, host=self.host, username=self.username, password=self.password)
        RabbitStore.set(self.key, None, host=self.host, username=self.username, password=self.password)
        result = RabbitStore.get(self.key, host=self.host, username=self.username, password=self.password)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
