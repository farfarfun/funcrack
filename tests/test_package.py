import unittest

import funcrack


class PackageTests(unittest.TestCase):
    def test_version_is_a_string(self) -> None:
        self.assertIsInstance(funcrack.__version__, str)
        self.assertEqual(funcrack.__version__, "0.0.1")


if __name__ == "__main__":
    unittest.main()
