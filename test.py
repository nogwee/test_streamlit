import streamlit as st
#import tropycal.tracks as tracks
from streamlit_folium import st_folium
import folium
import pandas as pd
from folium import FeatureGroup, LayerControl
import geopandas as gpd

st.set_page_config( 
    layout="wide"
)

placeholder = st.empty()
map_col, menu_col = placeholder.columns([4, 1])

#basin = tracks.TrackDataset(basin="west_pacific", source="ibtracs")
#storm = basin.get_storm(("jebi", 2018))
#df = storm.to_dataframe()
#df.to_csv("test.csv")
df = pd.read_csv("test.csv")
df = df.dropna(how="all", axis=1).drop(df.columns[0], axis=1)

# gdf = gpd.read_file("N02-23_GML/N02-23_RailroadSection.shp")
# gdf = gpd.read_file("N02-23_RailroadSection.geojson")

m = folium.Map(
    location=[30, 145], 
    zoom_start=4, 
    tiles='cartodbpositron'
)

minimap = folium.plugins.MiniMap(tile_layer='cartodbpositron',toggle_display=True)
m.add_child(minimap)


# with menu_col:
#     st.header("メニューとか")
#     on = st.toggle("経路図")

with map_col:

    keiro = FeatureGroup(name="経路図")
    # rosen = FeatureGroup(name="鉄道")

    # if on:
    folium.PolyLine(
        locations=[(row['lat'], row['lon']) for idx, row in df.iterrows()],
        color='blue',
        weight=2.5,
        opacity=1
    ).add_to(keiro)


    for idx, row in df.iterrows():
        jst = pd.to_datetime(row.time).tz_localize("utc").tz_convert("Asia/Tokyo")
        folium.Circle([row["lat"], row["lon"]], radius=20000, tooltip=f"{jst:%Y年%m月%d日%H時%M分}", fill=True
        ).add_to(keiro)

    # for idx, row in df.iterrows():
    #     folium.CircleMarker([row["lat"], row["lon"]], color="black", radius=4, fill_color="black", opacity=0, tooltip=f"{jst:%Y年%m月%d日%H時%M分}").add_to(m)

    # tooltip = folium.GeoJsonTooltip(fields=["N02_004", "N02_003"],aliases=["会社:", "路線名:"],)
    # folium.GeoJson(gdf, tooltip=tooltip).add_to(rosen)

    # rosen.add_to(m)
    keiro.add_to(m)

    LayerControl().add_to(m)

    st_folium(m, use_container_width=True, height=720, returned_objects=[])

    df
    gdf
