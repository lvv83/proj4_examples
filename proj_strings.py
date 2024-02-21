# Идентификаторы строк построенты по принципу
# <ЭЛЛИПСОИД>
# или
# <ЭЛЛИПСОИД>_<ПРОЕКЦИЯ>_<ЗОНА>

WGS84 = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'

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

# Проекция Гаусса-Крюгера (9-зона)
GSK11_GK_Q9 = ('+proj=tmerc +lat_0=0 +lon_0=51 +k=1 +x_0=9500000 +y_0=0 +ellps=GSK2011 +towgs84=0.013,-0.092,-0.03,'
               '-0.001738,0.003559,-0.004263,0.0074 +units=m +no_defs')

# Местные системы координат Республики Коми (шестиградусные)

P42_MSK11_Q4 = ('+proj=tmerc +lat_0=0 +lon_0=50.03333333333 +k=1 +x_0=4400000.0 +y_0=-6211057.63 +ellps=krass '
                '+towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs')

P42_MSK11_Q5 = ('+proj=tmerc +lat_0=0 +lon_0=56.03333333333 +k=1 +x_0=5400000.0 +y_0=-6211057.63 +ellps=krass '
                '+towgs84=23.57,-140.95,-79.8,0,0.35,0.79,-0.22 +units=m +no_defs')
