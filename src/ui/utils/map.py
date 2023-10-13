import os
from typing import Dict
import ee
import streamlit as st
import geemap.foliumap as geemap
import geopandas as gpd
from fiona.drvsupport import supported_drivers
import json


def ee_geo_compatible(geoJSON_input: Dict):
    geoJSON_output = dict(geoJSON_input)
    try:
        if geoJSON_input["type"]=="Polygon":
            check_coords = geoJSON_input["coordinates"][0][0]
            if len(check_coords)>2:
                print("Forcefully making coordinates compatible ee.Geometry as current len>2:", check_coords)
                new_coords = [[x[0:2] for x in y] for y in geoJSON_input["coordinates"]]
                geoJSON_output["coordinates"] = new_coords
        else:
            print("currently unknown handling for type:", geoJSON_input["type"])
        return geoJSON_output
    except:
        print("Dict passed does not follow geoJSON format")
        return None


st.cache_data
def map_gen():
    # st.header("National Land Cover Database (NLCD)")
    Map = geemap.Map(zoom=4)
    
    return Map

st.cache_data
def map_poly_gen(kml_file: str):
    # Read in KML file
    # Path to your KML file
    kml_file_path = kml_file
    # Read the KML file using geopandas
    supported_drivers['KML'] = 'rw'
    my_map = gpd.read_file(kml_file_path, driver='KML')
    kml_geo_json=json.loads(my_map.to_json())
    new_kml_geo_json = dict(kml_geo_json)
    # Initiate with no features
    new_kml_geo_json["features"] = []
    # display("original geojson")
    # display(kml_geo_json)
    for feat in kml_geo_json["features"]:
        new_feat = dict(feat)
        new_feat["geometry"] = ee_geo_compatible(feat["geometry"])
        if new_feat["geometry"]:
            try:
                ee.Geometry(new_feat["geometry"])
                print("succesfully passed to ee.Geometry")
                new_kml_geo_json["features"] += [new_feat]
            except:
                print("Unable to pass into ee.Geometry asses below feature")
                # print(new_feat)
                
    # display("updated geoJSON")
    # display(new_kml_geo_json)
    geojson_fc = ee.FeatureCollection(new_kml_geo_json)

    return geojson_fc

st.cache_data
def map_add_layer_gen(Map, feat_collections, layer_dict: Dict):
    poly = feat_collections.geometry()
    poly_area = poly.area().getInfo()
    Map.centerObject(poly, 12)

    dataset = layer_dict["dataset"]
    visualization = layer_dict["visualization"]
    name = layer_dict["name"]
    legend = layer_dict["builtin_legend"]

    Map.addLayer(dataset.clip(poly), visualization, name)

    if legend:
        Map.add_legend(
            name, builtin_legend=legend, 
        )
    return Map