try:
    # only after py3.4
    import collections.abc as abc
except ImportError:
    import collections as abc

import geojson
import shapely.geometry
import six


def shapely_to_geojson(geometry):
    """Converts a Shapely Shape geometry to a GeoJSON geometry"""
    if hasattr(geometry, "__geo_interface__"):
        geometry = shapely.geometry.mapping(geometry)
    return geometry


def geometry_like_to_shapely(geometry):
    """
    Convert a GeoJSON dict, or __geo_interface__ object, to a Shapely geometry.

    Handles Features and FeatureCollections (FeatureCollections become GeometryCollections).
    """
    if isinstance(geometry, shapely.geometry.base.BaseGeometry):
        return geometry

    if not isinstance(geometry, abc.Mapping):
        try:
            geometry = geometry.__geo_interface__
        except AttributeError:
            six.raise_from(
                TypeError(
                    "geometry object is not a GeoJSON dict, nor has a `__geo_interface__`: {}".format(
                        geometry
                    )
                ),
                None,
            )

    geoj = as_geojson_geometry(geometry)
    try:
        shape = shapely.geometry.shape(geoj)
    except Exception:
        raise ValueError(
            "Could not interpret this geometry as a Shapely shape: {}".format(geometry)
        )

    # test that geometry is in WGS84
    check_valid_bounds(shape.bounds)
    return shape


def as_geojson_geometry(geojson_dict):
    """
    Return a mapping as a GeoJSON instance, converting Feature types to Geometry types.
    """
    try:
        geoj = geojson.GeoJSON.to_instance(geojson_dict, strict=True)
    except (TypeError, KeyError, UnicodeEncodeError) as ex:
        raise ValueError(
            "geometry not recognized as valid GeoJSON ({}): {}".format(
                str(ex), geojson_dict
            )
        )
    # Shapely cannot handle GeoJSON Features or FeatureCollections
    if isinstance(geoj, geojson.Feature):
        geoj = geoj.geometry
    elif isinstance(geoj, geojson.FeatureCollection):
        features = []
        for feature in geoj.features:
            try:
                features.append(
                    geojson.GeoJSON.to_instance(feature, strict=True).geometry
                )
            except (TypeError, KeyError, UnicodeEncodeError) as ex:
                raise ValueError(
                    "feature in FeatureCollection not recognized as valid ({}): {}".format(
                        str(ex), feature
                    )
                )
        geoj = geojson.GeometryCollection(features)
    return geoj


def check_valid_bounds(bounds):
    """
    Test given bounds are correct type and in correct order.

    Raises TypeError or ValueError if bounds are invalid, otherwise returns None
    """
    try:
        if not isinstance(bounds, (list, tuple)):
            raise TypeError(
                "Bounds must be a list or tuple, instead got type {}".format(
                    type(bounds)
                )
            )

        if len(bounds) != 4:
            raise ValueError(
                "Bounds must a sequence of (minx, miny, maxx, maxy), "
                "got sequence of length {}".format(len(bounds))
            )
    except TypeError:
        six.raise_from(
            TypeError(
                "Bounds must a sequence of (minx, miny, maxx, maxy), got {}".format(
                    type(bounds)
                )
            ),
            None,
        )

    if bounds[0] >= bounds[2]:
        raise ValueError(
            "minx >= maxx in given bounds, should be (minx, miny, maxx, maxy)"
        )
    if bounds[1] >= bounds[3]:
        raise ValueError(
            "miny >= maxy in given bounds, should be (minx, miny, maxx, maxy)"
        )
