import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

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

historical_map = folium.Map(location=[31.3, 45.6], zoom_start=4)

for index, row in active_events.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"{row['event_name'], row['description']}"
    ).add_to(historical_map)

st_folium(historical_map)                 #display map 

