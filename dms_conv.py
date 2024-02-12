def from_dms_string(coord_string: str) -> float:
    """
    Возвращает значение координаты в числовом формате в виде десятичных градусов.

    :param coord_string
    Координата, представленная строкой формата dd° mm' ss.sss"
    """
    deg_pos = coord_string.index('°')
    min_pos = coord_string.index('\'')
    sec_pos = coord_string.index('"')

    degree = float(coord_string[0:deg_pos])
    minute = float(coord_string[deg_pos + 1: min_pos])
    second = float(coord_string[min_pos + 1: sec_pos].strip().replace(',', '.'))

    return degree + minute / 60.0 + second / 3600.0

