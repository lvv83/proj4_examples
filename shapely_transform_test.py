import unittest
from shapely import Point
from shapely.ops import transform
from pyproj import CRS, Transformer

from proj_strings import WGS84, P42


def create_wgs84_p42_pyproj_transform():
    # https://shapely.readthedocs.io/en/stable/manual.html#other-transformations
    wgs84_crs = CRS.from_proj4(WGS84)
    p42_crs = CRS.from_proj4(P42)
    transformer = Transformer.from_crs(crs_from=wgs84_crs, crs_to=p42_crs)
    return transformer.transform


class ShapelyTransformTest(unittest.TestCase):

    # Контрольные точки СТО Роскартография 3.5-2020 (Приложение Ж)

    wgs84_x = 44.03420944  # 44° 02' 03,154"
    wgs84_y = 56.29180389  # 56° 17' 30,494"

    p42_x = 44.03599139  # 44° 02' 09,569"
    p42_y = 56.29164361  # 56° 17' 29,917"

    def test_geometry_transform(self):
        # Проверка трансформации геометрических объектов (здесь точка)

        wgs84_point = Point(self.wgs84_x, self.wgs84_y)

        pyproj_transform = create_wgs84_p42_pyproj_transform()
        p42_point = transform(pyproj_transform, wgs84_point)

        self.assertAlmostEqual(p42_point.x, self.p42_x, places=6)
        self.assertAlmostEqual(p42_point.y, self.p42_y, places=6)
