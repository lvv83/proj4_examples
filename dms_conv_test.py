import unittest
import dms_conv


class DMSConverterTest(unittest.TestCase):

    def test_dms_1(self):
        coord = dms_conv.from_dms_string('56° 17\' 30,494"')  # '56° 17' 30,494" N'
        self.assertAlmostEqual(coord, 56.29180389, places=6)


if __name__ == "__main__":
    unittest.main()
