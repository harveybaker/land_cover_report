import os
from typing import Dict
import ee
import streamlit as st
from .info import globcover_2009, copernicus_2015, copernicus_2019, esaworldcover_2021

st.cache_data()
def list_of_klms():
    return os.listdir('ui/kml/')

st.cache_data
def dataset_dict():
    print(":in dataset_dict")
    output_dict = {}
    # functions

    def mask_s2_clouds(image):
        """Masks clouds in a Sentinel-2 image using the QA band.

        Args:
            image (ee.Image): A Sentinel-2 image.

        Returns:
            ee.Image: A cloud-masked Sentinel-2 image.
        """
        qa = image.select('QA60')

        # Bits 10 and 11 are clouds and cirrus, respectively.
        cloud_bit_mask = 1 << 10
        cirrus_bit_mask = 1 << 11

        # Both flags should be set to zero, indicating clear conditions.
        mask = (
            qa.bitwiseAnd(cloud_bit_mask)
            .eq(0)
            .And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
        )
        return image.updateMask(mask).divide(10000)
    
    # Update output dict with required layers
    output_dict['landcover_2009']={
        "dataset": ee.Image('ESA/GLOBCOVER_L4_200901_200912_V2_3').select('landcover'),
        "visualization": {'bands': ['landcover'],},
        "class_dict": globcover_2009,
        "builtin_legend": 'GLOBCOVER',
        "name":'2009_landcover',
    }
    output_dict['landcover_2015']={
        "dataset":ee.Image('COPERNICUS/Landcover/100m/Proba-V-C3/Global/2015').select('discrete_classification'),
        "visualization": {'bands': ['discrete_classification'],},
        "class_dict": copernicus_2015,
        "builtin_legend": 'COPERNICUS/Landcover/100m/Proba-V/Global',
        "name":'2015_landcover',
    }
    output_dict['landcover_2019']={
        "dataset":ee.Image('COPERNICUS/Landcover/100m/Proba-V-C3/Global/2019').select('discrete_classification'),
        "visualization": {'bands': ['discrete_classification'],},
        "class_dict": copernicus_2019,
        "builtin_legend": 'COPERNICUS/Landcover/100m/Proba-V/Global',
        "name":'2019_landcover',
    }
    output_dict['landcover_2021']={
        "dataset":ee.ImageCollection('ESA/WorldCover/v200').first().select('Map'),
        "visualization": {'bands': ['Map'],},
        "class_dict": esaworldcover_2021,
        "builtin_legend": 'ESA_WorldCover',
        "name":'2021_landcover',
    }
    
    for yr in ['2015','2017','2019', '2021', '2023']:
        output_dict[f"satellite_{yr}"] = {
            "dataset":ee.ImageCollection('COPERNICUS/S2_HARMONIZED').filterDate(f'{yr}-01-01', f'{yr}-12-31').filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)).map(mask_s2_clouds).median(),
            "visualization":{
                'min': 0.0,
                'max': 0.3,
                'bands': ['B4', 'B3', 'B2'],
            },
            "class_dict": None, 
            "builtin_legend": None,
            "name":f"{yr}_satellite",
        }
    return output_dict