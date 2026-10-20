import streamlit as st
from timeline import to_internal_year, reverse_internal_year, get_time_window 

st.title("ChronoAtlas: The World Through Time")
st.write("Explore world history through time. Discover historical events from different regions and civilizations that were happening around the same year.")

selected_year=st.slider(
    "Select the historical year",
    min_value=-3000,
    max_value=2026,
    value=500
)

display_year, era = reverse_internal_year(selected_year)
st.write("Selected year: ",display_year, era)

start_year,end_year=get_time_window(selected_year)
st.write("Historical context: ",reverse_internal_year(start_year), " to ",reverse_internal_year(end_year)) 