import folium

def add_civilization_polygons(historical_map, selected_year):

    # Mesopotamia
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

    # Indus Valley
    indus_region = [
        [30.5, 66.5],
        [33.0, 68.0],
        [32.5, 71.5],
        [29.0, 73.0],
        [25.0, 69.5],
        [26.0, 66.5]
    ]

    # Egypt
    egypt_region = [
        [31.5, 30.0],
        [31.0, 32.0],
        [27.0, 33.0],
        [22.0, 32.5],
        [22.0, 30.0],
        [26.0, 29.5]
    ]

    # Roman Empire
    roman_region = [
        [45.0, -5.0],
        [50.0, 10.0],
        [45.0, 25.0],
        [35.0, 35.0],
        [30.0, 20.0],
        [36.0, 0.0]
    ]

    # Han Dynasty
    han_region = [
        [38.0, 105.0],
        [40.0, 110.0],
        [37.0, 117.0],
        [32.0, 118.0],
        [28.0, 112.0],
        [31.0, 105.0]
    ]

    # Shang Dynasty
    shang_region = [
        [38.5, 108.0],
        [39.5, 112.0],
        [37.5, 117.0],
        [34.0, 118.0],
        [32.0, 114.0],
        [34.0, 109.0]
    ]

    # Mauryan Empire
    mauryan_region = [
        [30.0, 74.0],
        [29.0, 82.0],
        [25.0, 88.0],
        [20.0, 86.0],
        [16.0, 78.0],
        [22.0, 72.0]
    ]

    # Akkadian Empire
    akkadian_region = [
        [36.0, 40.5],
        [37.0, 43.0],
        [36.0, 46.5],
        [33.0, 48.0],
        [30.0, 46.0],
        [32.0, 42.0]
    ]

    # Common polygon styling
    polygon_style = {
        "color": "#B8A27A",
        "fill_color": "#C2A878",
        "fill_opacity": 0.65,
        "weight": 2
    }

    # Add civilizations according to the selected year

    if -3499 <= selected_year <= -2999:
        folium.Polygon(
            locations=mesopotamia_region,
            tooltip="Mesopotamia",
            **polygon_style
        ).add_to(historical_map)

    if -2600 <= selected_year <= -1900:
        folium.Polygon(
            locations=indus_region,
            tooltip="Indus valley",
            **polygon_style
        ).add_to(historical_map)

    if -3100 <= selected_year <= -2686:
        folium.Polygon(
            locations=egypt_region,
            tooltip="Egypt",
            **polygon_style
        ).add_to(historical_map)

    if -26 <= selected_year <= 476:
        folium.Polygon(
            locations=roman_region,
            tooltip="Roman",
            **polygon_style
        ).add_to(historical_map)

    if 206 <= selected_year <= 220:
        folium.Polygon(
            locations=han_region,
            tooltip="Han",
            **polygon_style
        ).add_to(historical_map)

    if -1600 <= selected_year <= -1046:
        folium.Polygon(
            locations=shang_region,
            tooltip="Shang",
            **polygon_style
        ).add_to(historical_map)

    if -321 <= selected_year <= -184:
        folium.Polygon(
            locations=mauryan_region,
            tooltip="Mauryan",
            **polygon_style
        ).add_to(historical_map)

    if -2333 <= selected_year <= -2153:
        folium.Polygon(
            locations=akkadian_region,
            tooltip="Akkadian",
            **polygon_style
        ).add_to(historical_map)
