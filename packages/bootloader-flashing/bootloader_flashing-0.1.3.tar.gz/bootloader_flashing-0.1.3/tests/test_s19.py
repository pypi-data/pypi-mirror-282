import unittest

from bootloader_flashing.files.s19 import S19


class TestHex(unittest.TestCase):
    def test_reading(self):
        s19 = S19("demo.s19")
        print(s19)


if __name__ == "__main__":
    unittest.main()
