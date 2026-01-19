import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("📚 Online Library System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["View Authors", "View Books", "View Borrow Records", "Download Excel"]
)

# ---------------- View Authors ----------------
if menu == "View Authors":
    st.header("All Authors")

    res = requests.get(f"{BASE_URL}/authors/")

    if res.status_code == 200:
        try:
            data = res.json()
            st.table(data)
        except:
            st.error("Backend did not return JSON data.")
    else:
        st.error("Backend API not working.")


elif menu == "View Books":
    st.header("All Books")

    res = requests.get(f"{BASE_URL}/books/")
    data = res.json()
    st.table(data)

# ---------------- View Borrow Records ----------------
elif menu == "View Borrow Records":
    st.header("Borrow Records")

    res = requests.get(f"{BASE_URL}/borrows/")
    data = res.json()
    st.table(data)

# ---------------- Download Excel ----------------
elif menu == "Download Excel":
    st.header("Download Library Data")

    st.markdown("Click the link below to download Excel file:")
    st.markdown(f"[Download Excel]({BASE_URL}/export/)")
