from pyproj import Transformer, CRS
from proj_strings import WGS84, P42


def do_transform(from_crs, to_crs, x, y):
    transformer = Transformer.from_crs(crs_from=from_crs, crs_to=to_crs)
    print(transformer)
    return transformer.transform(x, y)


class TransformFacade:
    wgs84_crs = CRS.from_proj4(WGS84)
    p42_crs = CRS.from_proj4(P42)

    def wgs84_to_p42(self, point_xy_tuple):
        return do_transform(self.wgs84_crs, self.p42_crs, point_xy_tuple[0], point_xy_tuple[1])

    def p42_to_wgs84(self, point_xy_tuple):
        return do_transform(self.p42_crs, self.wgs84_crs, point_xy_tuple[0], point_xy_tuple[1])
