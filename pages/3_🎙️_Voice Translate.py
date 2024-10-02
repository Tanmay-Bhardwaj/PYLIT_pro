import streamlit as st
from deep_translator import GoogleTranslator
import speech_recognition as sr


st.set_page_config(
    page_title="Voice Translate",
    page_icon="🎙️",
)

st.title("Voice Translate")


page_bg_img="""
<style>
    [data-testid="stAppViewContainer"] {
	background: radial-gradient(at bottom right, #E5A82F 0, #E5A82F 8.75px, #E5A82F33 8.75px, #E5A82F33 17.5px, #E5A82FBF 17.5px, #E5A82FBF 26.25px, #E5A82F40 26.25px, #E5A82F40 35px, #E5A82F4D 35px, #E5A82F4D 43.75px, #E5A82FBF 43.75px, #E5A82FBF 52.5px, #E5A82F33 52.5px, #E5A82F33 61.25px, transparent 61.25px, transparent 70px), radial-gradient(at top left, transparent 0, transparent 8.75px, #E5A82F33 8.75px, #E5A82F33 17.5px, #E5A82FBF 17.5px, #E5A82FBF 26.25px, #E5A82F4D 26.25px, #E5A82F4D 35px, #E5A82F40 35px, #E5A82F40 43.75px, #E5A82FBF 43.75px, #E5A82FBF 52.5px, #E5A82F33 52.5px, #E5A82F33 61.25px, #E5A82F 61.25px, #E5A82F 70px, transparent 70px, transparent 175px);
	background-blend-mode: multiply;
	background-size: 70px 70px, 70px 70px;
	background-color: #B2A461;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


if st.button("Click to record audio 🎙️"):
    st.write("recording..")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        text=recognizer.recognize_google(audio)
    st.write(text)
    translated_hi = GoogleTranslator(source='auto', target='hi').translate(text)
    translated_mr = GoogleTranslator(source='auto', target='mr').translate(text)
    st.text_area(label="Hindi:", value=translated_hi, height=100)
    st.text_area(label="Marathi:", value=translated_mr, height=100)
    