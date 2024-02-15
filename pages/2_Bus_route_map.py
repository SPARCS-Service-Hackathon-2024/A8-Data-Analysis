import streamlit as st
import pandas as pd
import pydeck as pdk

# Streamlit 앱 제목
st.title('버스 정류장 노선 분석')

# CSV 파일 경로
FILE_PATH = 'concatenated_routes.csv'

# CSV 파일 읽기
df = pd.read_csv(FILE_PATH, encoding='cp949')

route_ids = df['route_id'].unique()
selected_route_id = st.selectbox('노선을 선택하세요.', route_ids)

filtered_data = df[df['route_id'] == selected_route_id]

st.map(filtered_data)
