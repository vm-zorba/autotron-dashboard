import streamlit as st
import pandas as pd

# === Replace XXX and the GIDs with your real values ===
SIGNALS_URL = "https://docs.google.com/spreadsheets/d/110tuY8QOQTj4H_J0QB5gtovHGUlRSSg3A38dluB3eUI/edit?gid=0#gid=0"
TRADES_URL  = "https://docs.google.com/spreadsheets/d/110tuY8QOQTj4H_J0QB5gtovHGUlRSSg3A38dluB3eUI/edit?gid=55150987#gid=55150987"  # <- Put your trades tab GID here

st.set_page_config(page_title="AutoTron Dashboard", layout="wide")
st.title("🚦 AutoTron Live Trade Dashboard")

# --- Use tabs for pro vibes ---
tab1, tab2 = st.tabs(["📊 Signals", "💼 Trades"])

with tab1:
    st.header("Signals")
    signals = pd.read_csv(SIGNALS_URL)
    st.dataframe(signals)

with tab2:
    st.header("Trades")
    trades = pd.read_csv(TRADES_URL)
    st.dataframe(trades)
