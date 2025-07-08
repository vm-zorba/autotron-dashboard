import streamlit as st
import pandas as pd

SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/110tuY8QOQTj4H_J0QB5gtovHGUlRSSg3A38dluB3eUI/edit?usp=sharing"

st.set_page_config(page_title="AutoTron Dashboard", layout="wide")
st.title("🚦 AutoTron Live Trade Dashboard")

# Load signals
@st.cache_data(ttl=120)
def load_signals():
    return pd.read_csv(https://docs.google.com/spreadsheets/d/110tuY8QOQTj4H_J0QB5gtovHGUlRSSg3A38dluB3eUI/edit?usp=sharing)

signals = load_signals()
st.dataframe(signals)

# You can add more widgets: charts, stats, filters, etc.
