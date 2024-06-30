import unittest

from bootloader_flashing.files.hex import Hex


class TestHex(unittest.TestCase):
    def test_reading(self):
        hex = Hex("demo.hex")
        print(hex)


if __name__ == "__main__":
    unittest.main()
