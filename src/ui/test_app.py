import streamlit as st
from streamlit_folium import st_folium
import geemap.foliumap as geemap
import ee
from dataclasses import dataclass
from typing import Dict, List, Optional

# os.environ["EARTHENGINE_TOKEN"] == st.secrets["EARTHENGINE_TOKEN"]

ee.Initialize()

@dataclass
class Point:
    lat: float
    lon: float

    @classmethod
    def from_dict(cls, data: Dict) -> "Point":
        if "lat" in data:
            return cls(float(data["lat"]), float(data["lng"]))
        elif "latitude" in data:
            return cls(float(data["latitude"]), float(data["longitude"]))
        else:
            raise NotImplementedError(data.keys())

    def is_close_to(self, other: "Point") -> bool:
        close_lat = self.lat - 0.0001 <= other.lat <= self.lat + 0.0001
        close_lon = self.lon - 0.0001 <= other.lon <= self.lon + 0.0001
        return close_lat and close_lon


@dataclass
class Bounds:
    south_west: Point
    north_east: Point

    def contains_point(self, point: Point) -> bool:
        in_lon = self.south_west.lon <= point.lon <= self.north_east.lon
        in_lat = self.south_west.lat <= point.lat <= self.north_east.lat

        return in_lon and in_lat

    @classmethod
    def from_dict(cls, data: Dict) -> "Bounds":
        return cls(
            Point.from_dict(data["_southWest"]), Point.from_dict(data["_northEast"])
        )


"# streamlit geemap demo"
st.markdown('Source code: <https://github.com/giswqs/geemap-streamlit/blob/main/geemap_app.py>')


with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import ee

    m = geemap.Map()
    dem = ee.Image('USGS/SRTMGL1_003')

    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

    m.addLayer(dem, vis_params, 'SRTM DEM', True, 1)
    m.addLayerControl()

    # call to render Folium map in Streamlit
    map_data = st_folium(m)

    # get data from map for further processing
    map_bounds = Bounds.from_dict(map_data["bounds"])

    st.write(map_bounds)