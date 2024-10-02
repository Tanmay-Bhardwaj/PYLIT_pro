import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.title("Home Page")
st.sidebar.success("developed by Team PYLIT colaboration with Tanmay Bhardwaj")

page_bg_img="""
<style>
    [data-testid="stAppViewContainer"] {
background:
      conic-gradient(at 10% 50%,#0000 75%,#000000 0),
      conic-gradient(at 10% 50%,#0000 75%,#000000 0) calc(1*32px) calc(3*32px),
      conic-gradient(at 10% 50%,#0000 75%,#000000 0) calc(2*32px) calc(1*32px),
      conic-gradient(at 10% 50%,#0000 75%,#000000 0) calc(3*32px) calc(4*32px),
      conic-gradient(at 10% 50%,#0000 75%,#000000 0) calc(4*32px) calc(2*32px),
      conic-gradient(at 50% 10%,#0000 75%,#000000 0) 0 calc(4*32px),
      conic-gradient(at 50% 10%,#0000 75%,#000000 0) calc(1*32px) calc(2*32px),
      conic-gradient(at 50% 10%,#0000 75%,#000000 0) calc(2*32px) 0,
      conic-gradient(at 50% 10%,#0000 75%,#000000 0) calc(3*32px) calc(3*32px),
      conic-gradient(at 50% 10%,#0000 75%,#000000 0) calc(4*32px) calc(1*32px),
      #000000;
background-size: 160px 160px;


}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.subheader("Pylit is an Open source initiative by all the members of the project. With the Valuable guidance of  Samudra sir, team PYLIT was able to successfully create a language translator in Python. The future version of PYLIT looks forward to adding features like computer vision translation and expanding the number of languages to which the language can be translated.")
with st.sidebar:
    selected = option_menu(
        menu_title="Contact US", 
        options=["pylit.usr@gmail.com"], 
        icons=['envelope-at-fill'], 
        menu_icon="cast", default_index=0)