import streamlit as st
from web_function import load_data
from Tabs import home, predict, visualize

# Mendefinisikan tabs
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualization": visualize
}

# Membuat sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Halaman", list(Tabs.keys()))

# Memuat data
df, x, y = load_data()

# Menampilkan subheader berdasarkan halaman yang dipilih jika diperlukan
if page in ["Prediction", "Visualization"]:
    st.sidebar.subheader(page)
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()
    # Tabs[page].app()