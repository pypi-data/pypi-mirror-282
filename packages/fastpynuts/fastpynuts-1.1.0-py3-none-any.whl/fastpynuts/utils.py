"""
Contains miscellaneous utilities.
"""

import shapely
from shapely.geometry import shape, Polygon, MultiPolygon
from shapely.errors import GeometryTypeError


def geometry2shapely(geometry):
    """
    Convert the geometry given by dictionary `geometry` to a `shapely` geometry using
    [shapely's `shape`](https://shapely.readthedocs.io/en/stable/manual.html#shapely.geometry.shape).
    Additionally allows to pass a GeoJSON feature containing

    Supported geometry types:
    - Polygon
    - MultiPolygon
    - MultiPoint
    - a GeoJSON feature containing one of the above valid geometries
    """
    try:
        poly = shape(geometry)
    except GeometryTypeError:
        poly = shape(geometry["geometry"])

    return poly



# def get_polygon_bounds(poly):
#     if shapely.is_geometry(poly):
#         return poly.bounds
#         # if isinstance(poly, Polygon):
#         #     coords = poly.exterior.coords
#         # elif isinstance(poly, MultiPolygon):
#         #     coords = poly.geoms[0].exterior.coords
#         # elif hasattr(poly, "coords"):
#         #     coords = poly.coords
#         # else:
#         #     raise ValueError(f"Unsupported type {type(poly)}")

#         # x = [c[0] for c in coords]
#         # y = [c[1] for c in coords]
#         # minx, miny, maxx, maxy = min(x), min(y), max(x), max(y)
#     elif isinstance(poly, dict):
#         # TODO: validate these formats
#         geom_type = poly["type"]
#         if geom_type == "Polygon":
#             coords = poly["coords"]
#         elif geom_type == "MultiPolygon":
#             coords = []


#         x = [c[0] for c in coords]
#         y = [c[1] for c in coords]
#         minx, miny, maxx, maxy = min(x), min(y), max(x), max(y)
#         return minx, miny, maxx, maxy
