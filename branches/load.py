import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

counties_mapping = {
    'objectid': 'OBJECTID',
    'id_field': 'ID_',
    'county_nam': 'COUNTY_NAM',
    'const_code': 'CONST_CODE',
    'constituen': 'CONSTITUEN',
    'county_cod': 'COUNTY_COD',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/counties.shp'))

def run(verbose=True):
	lm = LayerMapping(Counties, county_shp, counties_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=False,verbose=verbose)