WGS84 = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'
# P42 = '+proj=longlat +ellps=krass +towgs84=25,-141,-78.5,0,0.35,0.736,0 +no_defs'
# 23.57, -140.95, -79.8, 0.0, -0.35, -0.79, -0.22

# Coordinate frame rotation
# P42 = '+proj=longlat +ellps=krass +towgs84=23.57,-140.95,-79.8,0,-0.35,-0.79,-0.22 +no_defs'

# Position vector
P42 = '+proj=longlat +ellps=krass +towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +no_defs'

# Внимание!!!
# Есть различие в параметрах методов "Coordinate frame rotation" и "Position vector"
# Параметры поворота берутся с противоположным знаком!!!

# В ArcGIS трансформация координат выполняется методом "Coordinate frame rotation"
# В библиотеке Proj трансформация выполняется методом "Position vector"

# В проекциях QGIS, в пересчёте параметров из ГОСТов, а также на некоторых сайтах
# (https://mapbasic.ru/msk11, https://gis-lab.info/forum/viewtopic.php?f=34&t=10551)
# указаны параметры перехода к WGS-84 для метода Coordinate frame rotation, видимо скопированные из WKT ArcGIS.
# Прямая подстановка таких параметров в Proj приводит к некорректной трансформации!!!

# При анализе pipeline-строки трансформации в Proj видим
# step proj=helmert x=23.57 y=-140.95 z=-79.8 rx=0 ry=0.35 rz=0.79 s=-0.22 convention=position_vector

# Возможно, что при переопределении метода трансформации в Proj можно будет указывать исходные параметры

# https://gis-lab.info/qa/datum-transform-methods.html
# https://github.com/OSGeo/PROJ/issues/1091
# https://gis.stackexchange.com/questions/112198/proj4-postgis-transformations-between-wgs84-and-nad83-transformations-in-alask


# Параметры перехода к WGS84 для эллипсоида ГСК-2011 рассчитаны на основе параметров в ГОСТ 32453-2017
# ГСК-2011 => ПЗ-90.11 (приложение А.5)
# WGS-84 => ПЗ-90.11 (приложение Г.1)
# с учётом замечания для "Position vector"
GSK11 = '+proj=longlat +ellps=GSK2011 +towgs84=0.013,-0.092,-0.03,-0.001738,0.003559,-0.004263,0.0074 +no_defs'
