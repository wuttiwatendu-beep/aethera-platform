import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="RMUTI Energy Network", layout="wide")

# CSS สำหรับปรับแต่งโทนสีสว่างและ Card สไตล์พรีเมียม
st.markdown("""
    <style>
    .main { background-color: #f8fafc; color: #1e293b; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        border: 1px solid #e2e8f0;
    }
    div[data-testid="stMetricValue"] { color: #E85D04; font-weight: bold; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f5f9;
        border-radius: 5px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ข้อมูลอาคาร (Master Data ตามที่คุณนุระบุ)
data = [
    {"Bldg": "อาคาร G (หนองระเวียง)", "kW": 354.56, "Lat": 14.9435, "Lon": 102.2140, "Type": "Source"},
    {"Bldg": "อาคาร 35 (ทะเบียน)", "kW": 485.76, "Lat": 14.9922, "Lon": 102.1162, "Type": "Source"},
    {"Bldg": "อาคาร 32 (บริหาร)", "kW": 400.00, "Lat": 14.9925, "Lon": 102.1155, "Type": "P2P"},
    {"Bldg": "อาคาร 4 (วิทยบริการ)", "kW": 280.00, "Lat": 14.9910, "Lon": 102.1165, "Type": "P2P"},
    {"Bldg": "อาคาร 2 (หอประชุม)", "kW": 250.00, "Lat": 14.9905, "Lon": 102.1158, "Type": "P2P"},
    {"Bldg": "อาคาร 1 (อธิการบดี)", "kW": 220.00, "Lat": 14.9915, "Lon": 102.1160, "Type": "P2P"},
    {"Bldg": "Sports Complex", "kW": 150.00, "Lat": 14.9940, "Lon": 102.1140, "Type": "P2P"},
    {"Bldg": "อาคาร A", "kW": 314.24, "Lat": 14.9935, "Lon": 102.1168, "Type": "P2P"},
    {"Bldg": "อาคาร B", "kW": 300.00, "Lat": 14.9900, "Lon": 102.1170, "Type
