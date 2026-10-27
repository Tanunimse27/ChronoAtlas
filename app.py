import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from branca.element import Element
from civilization_data import civilizations

st.set_page_config(layout="wide")
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

events=pd.read_csv("events.csv")

from timeline import to_internal_year, reverse_internal_year, get_time_window 

st.title("ChronoAtlas: The World Through Time")
st.write("Explore world history through time. Discover historical events from different regions and civilizations that were happening around the same year.")

selected_year=st.slider(
    "Select the historical year",
    min_value=-3999,
    max_value=2026,
    value=500
)
#filteration
active_events=events[
    (events["start_year"]<=selected_year)&
    (events["end_year"]>=selected_year)
]

st.dataframe(active_events)                       #display filtered data

st.map(active_events[["latitude","longitude"]])
display_year, era = reverse_internal_year(selected_year)
st.write("You are exploring events from : ",display_year, era)

start_year,end_year=get_time_window(selected_year)

start_display,start_era= reverse_internal_year(start_year)
end_display,end_era=reverse_internal_year(end_year)

st.write("Historical context: ",start_display,start_era, " to ",end_display,end_era) 

historical_map = folium.Map(
    location=[20, 0],
    zoom_start=2,
    min_zoom=2,
    max_zoom=8,
    tiles=None,
    max_bounds=True
)

folium.TileLayer(
    tiles="OpenStreetMap",
    no_wrap=True
).add_to(historical_map)

historical_map.options["maxBounds"] = [[-85, -180], [85, 180]]
historical_map.options["maxBoundsViscosity"] = 1.0

historical_map.options["maxBoundsViscosity"] = 1.0


zoom_script = f"""
(function() {{
    var map = {historical_map.get_name()};
    var worldBounds = L.latLngBounds(
        [[-85, -180], [85, 180]]
    );

    function adjustZoom() {{
        var minZoom = map.getBoundsZoom(worldBounds, true);
        map.setMinZoom(minZoom);

        if (map.getZoom() < minZoom) {{
            map.setZoom(minZoom);
        }}
    }}

    map.whenReady(function() {{
        adjustZoom();
        map.on("resize", adjustZoom);
    }});
}})();
"""

historical_map.get_root().script.add_child(Element(zoom_script))


#geographical points
mesopotamia_region = [
    [35.5, 41.0],
    [36.5, 42.5],
    [36.0, 44.5],
    [35.5, 46.5],
    [33.5, 48.0],
    [31.0, 47.5],
    [29.5, 46.0],
    [30.5, 43.5],
    [32.0, 41.5]
]
indus_region = [
    [30.5, 66.5],
    [33.0, 68.0],
    [32.5, 71.5],
    [29.0, 73.0],
    [25.0, 69.5],
    [26.0, 66.5]
]
egypt_region = [
    [31.5, 30.0],
    [31.0, 32.0],
    [27.0, 33.0],
    [22.0, 32.5],
    [22.0, 30.0],
    [26.0, 29.5]
]
roman_region = [
    [45.0, -5.0],
    [50.0, 10.0],
    [45.0, 25.0],
    [35.0, 35.0],
    [30.0, 20.0],
    [36.0, 0.0]
]
han_region = [
    [38.0, 105.0],
    [40.0, 110.0],
    [37.0, 117.0],
    [32.0, 118.0],
    [28.0, 112.0],
    [31.0, 105.0]
]
shang_region = [
    [38.5, 108.0],
    [39.5, 112.0],
    [37.5, 117.0],
    [34.0, 118.0],
    [32.0, 114.0],
    [34.0, 109.0]
]
mauryan_region = [
    [30.0, 74.0],
    [29.0, 82.0],
    [25.0, 88.0],
    [20.0, 86.0],
    [16.0, 78.0],
    [22.0, 72.0]
]
akkadian_region = [
    [36.0, 40.5],
    [37.0, 43.0],
    [36.0, 46.5],
    [33.0, 48.0],
    [30.0, 46.0],
    [32.0, 42.0]
]

if selected_year>=-3499 and selected_year<=-2999:
    folium.Polygon(locations=mesopotamia_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year >= -2600 and selected_year <= -1900:
    folium.Polygon(locations=indus_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year >= -3100 and selected_year <= -2686:
    folium.Polygon(locations=egypt_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year >= -26 and selected_year <= 476:
    folium.Polygon(locations=roman_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year >= 206 and selected_year <= 220:
    folium.Polygon(locations=han_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year >= -1600 and selected_year <= 1046:
    folium.Polygon(locations=shang_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year >=-321 and selected_year <= -184:
    folium.Polygon(locations=mauryan_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

if selected_year>=-2333 and selected_year<=-2153:
    folium.Polygon(locations=akkadian_region,
               color= "#B8A27A",
               fill_color="#C2A878",
               fill=True,
               fill_opacity=0.65
               ).add_to(historical_map)

for index, row in active_events.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"{row['event_name'], row['description']}"
    ).add_to(historical_map)

map_col,info_col=st.columns([2,1])

with map_col:
    st_folium(historical_map,
          use_container_width=True,
          height=850
          )              #display map 

with info_col:
    st.title("Civilization detail")
    st.write(civilizations["Mesopotamia"]["location"])
    st.write(civilizations["Mesopotamia"]["period"])