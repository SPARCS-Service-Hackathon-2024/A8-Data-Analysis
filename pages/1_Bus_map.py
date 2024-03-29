import streamlit as st
import pandas as pd
import pydeck as pdk

# CSV 파일 경로
FILE_PATH = '대전광역시_시내버스 기반정보_20230329.csv'

# CSV 파일 읽기
df = pd.read_csv(FILE_PATH, encoding='cp949')

# 필요한 컬럼만 선택 (정류장명, 위도, 경도)
bus_stops = df[['정류장명', '와이좌표', '엑스좌표']].rename(columns={'와이좌표': 'latitude', '엑스좌표': 'longitude'})
bus_stops = bus_stops.dropna(subset=['latitude'])

# Streamlit 앱 제목
st.title('버스 정류장 데이터 분석')

# 지도에 표시
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=bus_stops['latitude'].mean(),
        longitude=bus_stops['longitude'].mean(),
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=bus_stops,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=100,
        ),
    ],
))

st.map(bus_stops)



bus_stop_counts = df.groupby(['시도명', '시군구명', '읍면동명']).size().reset_index(name='버스 정류장 개수')
bus_stop_counts_2 = df.groupby(['시도명', '시군구명']).size().reset_index(name='버스 정류장 개수')

# 결과 표시
st.write("## 버스 정류장 개수", bus_stop_counts)
st.write(bus_stop_counts_2)
st.bar_chart(bus_stop_counts_2.set_index('시군구명')['버스 정류장 개수'])

