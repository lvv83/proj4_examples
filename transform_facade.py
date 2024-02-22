from pyproj import Transformer, CRS
from proj_strings import WGS84, P42, GSK11, P42_MSK11_Q4, P42_MSK11_Q5, GSK11_GK_Q9


def do_transform(from_crs, to_crs, x, y):
    transformer = Transformer.from_crs(crs_from=from_crs, crs_to=to_crs)
    print('TRANSFORM:', transformer)
    return transformer.transform(x, y)


def do_pipeline_transform(pipeline, x, y):
    transformer = Transformer.from_pipeline(pipeline)
    print('TRANSFORM:', transformer)
    return transformer.transform(x, y)


class TransformFacade:
    wgs84_crs = CRS.from_proj4(WGS84)
    p42_crs = CRS.from_proj4(P42)
    gsk11_crs = CRS.from_proj4(GSK11)
    msk11q4_crs = CRS.from_proj4(P42_MSK11_Q4)
    msk11q5_crs = CRS.from_proj4(P42_MSK11_Q5)
    gsk11_gk_q9_crs = CRS.from_proj4(GSK11_GK_Q9)

    def wgs84_to_p42(self, point_xy_tuple):
        return do_transform(self.wgs84_crs, self.p42_crs, point_xy_tuple[0], point_xy_tuple[1])

    def p42_to_wgs84(self, point_xy_tuple):
        return do_transform(self.p42_crs, self.wgs84_crs, point_xy_tuple[0], point_xy_tuple[1])

    def gsk11_to_wgs84(self, point_xy_tuple):
        return do_transform(self.gsk11_crs, self.wgs84_crs, point_xy_tuple[0], point_xy_tuple[1])

    def wgs84_to_gsk11(self, point_xy_tuple):
        return do_transform(self.wgs84_crs, self.gsk11_crs, point_xy_tuple[0], point_xy_tuple[1])

    def p42_to_gsk11(self, point_xy_tuple):
        return do_transform(self.p42_crs, self.gsk11_crs, point_xy_tuple[0], point_xy_tuple[1])

    def gsk11_to_p42(self, point_xy_tuple):
        return do_transform(self.gsk11_crs, self.p42_crs, point_xy_tuple[0], point_xy_tuple[1])

    def gsk11_to_gsk11gkq4(self, point_xy_tuple):
        return do_transform(self.gsk11_crs, self.gsk11_gk_q9_crs, point_xy_tuple[0], point_xy_tuple[1])

    def msk11q4_to_p42(self, point_xy_tuple):
        return do_transform(self.msk11q4_crs, self.p42_crs, point_xy_tuple[0], point_xy_tuple[1])

    def msk11q5_to_p42(self, point_xy_tuple):
        return do_transform(self.msk11q5_crs, self.p42_crs, point_xy_tuple[0], point_xy_tuple[1])

    def msk11q4_to_gsk11gkq9(self, point_xy_tuple):
        p42 = self.msk11q4_to_p42(point_xy_tuple)
        gsk11 = self.p42_to_gsk11(p42)
        return self.gsk11_to_gsk11gkq4(gsk11)

    def msk11q4_to_wgs84(self, point_xy_tuple):
        return do_transform(self.msk11q4_crs, self.wgs84_crs, point_xy_tuple[0], point_xy_tuple[1])

    def wgs84_to_msk11q4(self, point_xy_tuple):
        return do_transform(self.wgs84_crs, self.msk11q4_crs, point_xy_tuple[0], point_xy_tuple[1])

    def msk11q5_to_wgs84(self, point_xy_tuple):
        return do_transform(self.msk11q5_crs, self.wgs84_crs, point_xy_tuple[0], point_xy_tuple[1])

        # Рабочий вариант
        # p42 = self.msk11q5_to_p42(point_xy_tuple)
        # return self.p42_to_wgs84(p42)

