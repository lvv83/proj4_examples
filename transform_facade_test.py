import unittest
from transform_facade import TransformFacade


class TransformTest(unittest.TestCase):
    # Контрольные точки СТО Роскартография 3.5-2020 (Приложение Ж)

    wgs84_x = 44.03420944  # 44° 02' 03,154"
    wgs84_y = 56.29180389  # 56° 17' 30,494"

    p42_x = 44.03599139  # 44° 02' 09,569"
    p42_y = 56.29164361  # 56° 17' 29,917"

    gsk11_x = 44.03421222  # 44° 02' 03,164"
    gsk11_y = 56.291805  # 56° 17' 30.498"

    # Проверка через онлайн-конвертер https://geoproj.ru

    # geoproj.ru (P42 => WGS84)
    # 44.034209218
    # 56.291804030

    # geoproj.ru (GSK11 => WGS84)
    # 44.034209218
    # 56.291803746

    # geoproj.ru (P42 => GSK11)
    # 44.034212122
    # 56.291805285

    # Контрольные точки пункта ГГС "Язель"

    # МСК-11 Зона 4
    msk11_q4_x = 4433839.59
    msk11_q4_y = 658872.48

    # Гаусса-Крюгера 9 зона на эллипсоиде ГСК-2011 (рядом данные по выписке Росреестра, расхождение до 4.3 м)
    gsk11_gk_q9_x = 9482976.292  # 9482980.68
    gsk11_gk_q9_y = 6869725.201  # 6869722.24

    # geoproj.ru (MSK11Q4 => GSK11_GK_Q9)
    # 9482976.292
    # 6869725.201

    # Контрольная точка из 5-ой зоны МСК

    # МСК-11 Зона 5
    msk11_q5_x = 5289418.39
    msk11_q5_y = 848024.02

    wgs84_msk11_q5_x = 53.8017766
    wgs84_msk11_q5_y = 63.6162694

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

    def test_gsk11_wgs84(self):
        gsk11_point = (self.gsk11_x, self.gsk11_y)
        wgs84_point = self._transformFacade.gsk11_to_wgs84(gsk11_point)
        self.assertAlmostEqual(wgs84_point[0], self.wgs84_x, places=6)
        self.assertAlmostEqual(wgs84_point[1], self.wgs84_y, places=6)

    def test_wgs84_gsk11(self):
        wgs84_point = (self.wgs84_x, self.wgs84_y)
        gsk11_point = self._transformFacade.wgs84_to_gsk11(wgs84_point)
        self.assertAlmostEqual(gsk11_point[0], self.gsk11_x, places=6)
        self.assertAlmostEqual(gsk11_point[1], self.gsk11_y, places=6)

    def test_p42_gsk11(self):
        p42_point = (self.p42_x, self.p42_y)
        gsk11_point = self._transformFacade.p42_to_gsk11(p42_point)
        self.assertAlmostEqual(gsk11_point[0], self.gsk11_x, places=6)
        self.assertAlmostEqual(gsk11_point[1], self.gsk11_y, places=6)

    def test_gsk11_p42(self):
        gsk11_point = (self.gsk11_x, self.gsk11_y)
        p42_point = self._transformFacade.gsk11_to_p42(gsk11_point)
        self.assertAlmostEqual(p42_point[0], self.p42_x, places=6)
        self.assertAlmostEqual(p42_point[1], self.p42_y, places=6)

    def test_msk11q4_gsk11gkq9(self):
        msk_point = (self.msk11_q4_x, self.msk11_q4_y)
        gsk_point = self._transformFacade.msk11q4_to_gsk11gkq9(msk_point)
        # Прямоугольные координаты, точность - 2
        self.assertAlmostEqual(gsk_point[0], self.gsk11_gk_q9_x, places=2)
        self.assertAlmostEqual(gsk_point[1], self.gsk11_gk_q9_y, places=2)

    @unittest.skip  # Расхождение в 4 и 5 знаке после запятой
    def test_msk11q5_wgs84(self):
        msk_point = (self.msk11_q5_x, self.msk11_q5_y)
        wgs84_point = self._transformFacade.msk11q5_to_wgs84(msk_point)
        self.assertAlmostEqual(wgs84_point[0], self.wgs84_msk11_q5_x, places=6)
        self.assertAlmostEqual(wgs84_point[1], self.wgs84_msk11_q5_y, places=6)
