import streamlit as st
import pandas as pd

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
display_year, era = reverse_internal_year(selected_year)
st.write("Selected year: ",display_year, era)

start_year,end_year=get_time_window(selected_year)

start_display,start_era= reverse_internal_year(start_year)
end_display,end_era=reverse_internal_year(end_year)

st.write("Historical context: ",start_display,start_era, " to ",end_display,end_era) 
