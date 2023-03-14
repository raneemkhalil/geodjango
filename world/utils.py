from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, WorldBorderJson
from osgeo import gdal
from django.contrib.gis.db import models


world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}

worldborder_mapping = {
    'objectid': 'OBJECTID',
    'diameter': 'DIAMETER',
    'label': 'LABEL',
    'l_scaled': 'L_SCALED',
    'v': 'V',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING',
}

leakhotspot_mapping = {
    'elevation': 'ELEVATION',
    'emitter_k': 'EMITTER_K',
    'label': 'LABEL',
    'p': 'P',
    'runid': 'RunID',
    'leak': 'Leak',
    'color': 'color',
    'geom': 'MULTIPOINT',
}


def convert(name: str):
    json_path = name + '.json'
    world_jsn = Path(__file__).resolve().parent / 'data' / json_path
    srcDS = gdal.OpenEx(str(world_jsn))
    shp_path = name + '.shp'
    world_shp = Path(__file__).resolve().parent / 'data' / shp_path
    ds = gdal.VectorTranslate(str(world_shp), srcDS, format='ESRI Shapefile') # convert to shp file
    return str(world_shp)


def run(verbose=True, **kwargs):
    lm = LayerMapping(kwargs['model'], kwargs['path'], kwargs['layer_mapping'], transform=False) # insert into database
    lm.save(strict=True, verbose=verbose)
