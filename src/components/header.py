import streamlit as st

def header_home():
    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(
        f"""
        <div style='display: flex; flex-direction: column; align-items: center;justify-content: center; margin-bottom:30px; margibn-top:30px;'>
        <img src="{logo_url}" alt="SnapClass Logo" style="height: 100px;" >
        <h1 style='text-align: center; color: #E0E3FF;'></h1>
        </div>
        <div class="snapclass-title">
            <span>Snap</span>
            <span>Class</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
   


def header_dashboard():
    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(
        f"""
        <div style='display: flex; align-items: center;justify-content: center; gap: 10px;'>
        <img src="{logo_url}" alt="SnapClass Logo" style="height: 85px;" >
        <h2 style='text-align-left: center; color: #5865F2;'></h2>
        <div class="snapclass-title-dashboard">
            <span>Snap</span>
            <span>Class</span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
   