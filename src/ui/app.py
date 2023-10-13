import os
from typing import Dict
import ee
import streamlit as st
import geemap.foliumap as geemap
from utils.layers import dataset_dict, list_of_klms
from utils.map import map_gen, map_poly_gen, map_add_layer_gen
from utils.area import display_all_area_by_class
st.set_page_config(layout="wide")



ee.Initialize()

def app():
    st.title("Earth Engine Landcover Analysis")
    layers_dict = dataset_dict()
    # print(layer_dict)
    # print(list(layer_dict.keys()))
    files = list_of_klms()
    selected_file = st.selectbox("Select an kml fil", files)
    row1_col1, row1_col2 = st.columns([3, 1])
    with row1_col2:
        select_layer_choice = st.selectbox("Select a view", sorted(list(layers_dict.keys())), index=3)
    with row1_col1:
        map_streamlit_var = map_gen()
        kml_feat_collection = map_poly_gen(f"ui/kml/{selected_file}")
        map_streamlit_var = map_add_layer_gen(map_streamlit_var,kml_feat_collection, layers_dict[select_layer_choice])
        # width = 950
        # height = 600
        map_streamlit_var.to_streamlit(
            # width=width, 
            # height=height
        )
        keys_to_extract = ["landcover_2009", "landcover_2015","landcover_2019", "landcover_2021"]
        layers_dict_subset = {key: layers_dict[key] for key in keys_to_extract}
        if st.button("Calculate Forrest Coverage"):
            if map_streamlit_var.draw_features:
                new_drawn_fc = ee.FeatureCollection(map_streamlit_var.draw_features)
                new_poly = new_drawn_fc.geometry()
                display_all_area_by_class(kml_feat_collection.geometry(), layers_dict_subset)
            else:
                display_all_area_by_class(kml_feat_collection.geometry(), layers_dict_subset)
app()