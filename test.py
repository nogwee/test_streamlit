import streamlit as st
#import tropycal.tracks as tracks
from streamlit_folium import st_folium
import folium
import pandas as pd

#basin = tracks.TrackDataset(basin="west_pacific", source="ibtracs")
#storm = basin.get_storm(("jebi", 2018))
#df = storm.to_dataframe()
#df.to_csv("test.csv")
df = pd.read_csv("test.csv")

m = folium.Map(location=[30, 145], zoom_start=4, tiles='cartodbpositron')

# for idx, row in df.iterrows():
#     folium.Marker([row["lat"], row["lon"]], popup=row["time"]).add_to(m)

folium.PolyLine(
    locations=[(row['lat'], row['lon']) for idx, row in df.iterrows()],
    color='blue',
    weight=2.5,
    opacity=1
).add_to(m)

st_folium(m)
