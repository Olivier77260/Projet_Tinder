import streamlit as st

st.set_page_config(page_title="Tinder", page_icon=":couple:", layout="centered", initial_sidebar_state="auto")

dashboard = st.Page("pages/page1.py", title="Dashboard", icon=None, default=True)
bugs = st.Page("pages/page2.py", title="Bug reports", icon=None)
alerts = st.Page("pages/page1.py", title="System alerts", icon=None)

search = st.Page("pages/page1.py", title="Search", icon="🔥")
history = st.Page("pages/page2.py", title="History", icon=":material/star:")

pages = {
    "🏠 Your account": [search, history,],
    "Resources": [],
}

pg = st.navigation(pages)
pg.run()