import os
import unittest
from config import get_api_key, get_request_timeout


class TestConfig(unittest.TestCase):
    def test_default_timeout(self):
        if "REQUEST_TIMEOUT" in os.environ:
            del os.environ["REQUEST_TIMEOUT"]
        self.assertEqual(get_request_timeout(), 5)


if __name__ == "__main__":
    unittest.main()