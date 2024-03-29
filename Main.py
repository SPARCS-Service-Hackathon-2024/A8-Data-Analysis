import streamlit as st

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

st.write("# A8 데이터 분석 과제")

st.write('''
         이 Streamlit 앱은 대전광역시 대중교통 이용객들에게 버스 정류장 데이터 및 노선별 정류장 정보를 시각적으로 제공합니다.
         사용자는 대전광역시의 버스 정류장 분포를 볼 수 있고 시도, 시군구, 읍면동별 버스 정류장 개수를 확인할 수 있습니다.
         또한, 사용자는 드롭다운 메뉴를 통해 특정 버스 노선을 선택할 수 있으며, 선택된 노선에 해당하는 모든 버스 정류장이 지도 위에 표시됩니다.
         ''')