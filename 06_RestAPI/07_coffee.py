# conda install -c anaconda flask
from flask import Flask
import folium
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (37.55617096413908, 126.83839509599032)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/marker')
def marker():
    df = pd.read_csv('../input/coffee2.csv')
    mapping = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=13)

    for i in df.index:
        folium.Marker(
            location=[df['위도'][i], df['경도'][i]],
            popup=df['도로명주소'][i], 
            tooltip=f"{df['상호명'][i]}, {df['지점명'][i]}"
        ).add_to(mapping)
    mapping
    return mapping._repr_html_()

@app.route('/sb')
def starbucks():
    df = pd.read_csv('../input/starbucks.csv')
    mapping = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=13)

    for i in df.index:
        folium.Marker(
            location=[df['위도'][i], df['경도'][i]],
            popup=df['도로명주소'][i], 
            tooltip=f"{df['상호명'][i]}, {df['지점명'][i]}",
            icon=folium.Icon(color='cadetblue', icon='usd')
        ).add_to(mapping)
    mapping
    return mapping._repr_html_()

@app.route('/ed')
def ediya():
    df = pd.read_csv('../input/ediya.csv')
    mapping = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=13)

    for i in df.index:
        folium.Marker(
            location=[df['위도'][i], df['경도'][i]],
            popup=df['도로명주소'][i], 
            tooltip=f"{df['상호명'][i]}, {df['지점명'][i]}",
            icon=folium.Icon(color='red', icon='tag')
        ).add_to(mapping)
    mapping
    return mapping._repr_html_()

@app.route('/pd')
def paikdabang():
    df = pd.read_csv('../input/paikdabang.csv')
    mapping = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=13)

    for i in df.index:
        folium.Marker(
            location=[df['위도'][i], df['경도'][i]],
            popup=df['도로명주소'][i], 
            tooltip=f"{df['상호명'][i]}, {df['지점명'][i]}",
            icon=folium.Icon(color='purple', icon='map-marker')
        ).add_to(mapping)
    mapping
    return mapping._repr_html_()

@app.route('/ts')
def twosome():
    df = pd.read_csv('../input/twosome.csv')
    mapping = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=13)

    for i in df.index:
        folium.Marker(
            location=[df['위도'][i], df['경도'][i]],
            popup=df['도로명주소'][i], 
            tooltip=f"{df['상호명'][i]}, {df['지점명'][i]}",
            icon=folium.Icon(color='orange', icon='certificate')
        ).add_to(mapping)
    mapping
    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)