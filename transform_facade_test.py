import unittest
from transform_facade import TransformFacade


class TransformTest(unittest.TestCase):
    # wgs84_x_dms = '44° 02\' 03,154"'
    # wgs84_y_dms = '56° 17\' 30,494"'

    wgs84_x = 44.03420944
    wgs84_y = 56.29180389

    # geoproj (P42 => WGS84)
    # 44.034209218
    # 56.291804030

    p42_x = 44.03599139  # 44° 02' 09,569"
    p42_y = 56.29164361  # 56° 17' 29,917"

    @classmethod
    def setUpClass(cls):
        cls._transformFacade = TransformFacade()

    def test_p42_wgs84(self):
        p42_point = (self.p42_x, self.p42_y)
        wgs84_point = self._transformFacade.p42_to_wgs84(p42_point)

        self.assertAlmostEqual(wgs84_point[0], self.wgs84_x, places=6)
        self.assertAlmostEqual(wgs84_point[1], self.wgs84_y, places=6)

    def test_wgs84_p42(self):
        wgs84_point = (self.wgs84_x, self.wgs84_y)
        p42_point = self._transformFacade.wgs84_to_p42(wgs84_point)
        self.assertAlmostEqual(p42_point[0], self.p42_x, places=6)
        self.assertAlmostEqual(p42_point[1], self.p42_y, places=6)
