import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Text Translate",
    page_icon="🎙️",
)

st.title("Text transalte")

page_bg_img="""
<style>
    [data-testid="stAppViewContainer"] {
    background-color: #e5e5f7;
    opacity: 0.8;
    background-image: radial-gradient(circle at center center, #a66c00, #e5e5f7), repeating-radial-gradient(circle at center center, #a66c00, #a66c00, 15px, transparent 30px, transparent 15px);
    background-blend-mode: multiply;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

text=st.text_area("Text to translate")

if st.button("translate"):
    translated_hi = GoogleTranslator(source='auto', target='hi').translate(text)
    translated_mr = GoogleTranslator(source='auto', target='mr').translate(text)
    
    st.text_area(label="Hindi:", value=translated_hi, height=100)
    st.text_area(label="Marathi:", value=translated_mr, height=100)
else:
    st.write("Click the button to translate")