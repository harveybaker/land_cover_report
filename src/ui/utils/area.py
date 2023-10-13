import pandas as pd
import ee
import streamlit as st

def class_val_dict(val_list, class_name_list):
    output_dict = {}
    if len(val_list)==len(class_name_list):
        for i in range(len(val_list)):
            output_dict[f"{val_list[i]}"]=class_name_list[i]
    return output_dict

def area_sum_by_class_func(item):
    areaDict = ee.Dictionary(item)
    classNumber = ee.Number(areaDict.get('class')).format()
    area = ee.Number(areaDict.get('sum')).round()
    return ee.List([classNumber, area])

st.cache_data
def area_by_class(dataset, poly_clip, class_name_dict = {}):
    # print(class_name_dict)
    data=pd.DataFrame()
    areaImage = ee.Image.pixelArea().addBands(dataset.clip(poly_clip))
    areas = areaImage.reduceRegion(
        reducer = ee.Reducer.sum().group(
            groupField= 1,
            groupName= 'class',
        ),
        geometry= poly_clip,
        scale= 1,
        maxPixels= 1e10
        )
    classAreas = ee.List(areas.get('groups'))
    classAreaLists = classAreas.map(area_sum_by_class_func)
    result = ee.Dictionary(classAreaLists.flatten())
    tot_forrest_perc = 0
    forrest_flag = 0
    for val, area in result.getInfo().items():
        perc =  area/poly_clip.area().getInfo()*100
        try:
            # print(class_name_dict)
            class_name = class_name_dict[f"{val}"]['name']
            forrest_flag = class_name_dict[f"{val}"]['forrest_flag']
            if forrest_flag:
                tot_forrest_perc += perc
        except:
            class_name = "NA"
            forrest_flag = 0
        new_row=pd.DataFrame({
            'class_name': [class_name], 
            'class_val': [val], 
            'area': [round(area, 2)],
            'perc': [round(perc, 2)], 
            'forrest_flag': forrest_flag,
            'forrest_cum_perc': [round(tot_forrest_perc,2)],
        })
        data = pd.concat([data,new_row])
            # print('class Val:', val, 'Area:', round(area, 2), 'Perc:', round(perc, 2), 'total_forrest_Perc:', round(tot_perc,2))
    if result.getInfo():
        return data.reset_index(drop=True)

st.cache_resource
def display_all_area_by_class(poly, layers_dict):
    tab_list = sorted(list(layers_dict.keys()))
    tabs = st.tabs(tab_list)
    for i in range(len(tabs)):
        tabs[i].write(tab_list[i])
        tabs[i].write(area_by_class(layers_dict[tab_list[i]]["dataset"], poly, layers_dict[tab_list[i]]["class_dict"]))
