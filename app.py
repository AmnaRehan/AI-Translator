import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

st.title("AI Translator")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ8NDQ0NFREWFhURFRUYHSggGBolGxUVITEhJSkrLi46Fx8zOD84NygtOjcBCgoKDQ0NDw0NDysZFRkrLS0tNysrNzctKystKysrKzcrKy0rKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAMIBAwMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAAAAQIDB//EABkQAQEBAQEBAAAAAAAAAAAAAAABEQISA//EABkBAQEBAQEBAAAAAAAAAAAAAAABAgMFBP/EABgRAQEBAQEAAAAAAAAAAAAAAAARARIC/9oADAMBAAIRAxEAPwDyH5x35ceXXl6fl8Hp25bcua3K6OO46RuOcalVjcdpWnKVqVque46RqMSrK1jO42JqtMgAAABgmgYlhamo0YmGpayqWJYtrNqNYiUtZqNYlSqzajWJWatrNRvErNW1m1GsZARpzjpzXLl05rPlrXSVuVzlalbxz3HWVqOcrUrTG46StyuUalVjcdZWpXKVqVaxuOkq65yrq1mOno9OemrSN6ax6TSkdNTWNNSrGtTWdTUpGrU1LUtK1FtS1m1NRYtqIlqNZhazaWpUazErNq2s0bzEtZq1m1ndazDRkZrUZjUc43GM1dx0lalc5WpXTNY3HWNSucblbY3HSVdYlWVWNx0la1z1dGY3q65mrUjpprGmlI3prGmlI3qaxppSNaWs6mosa1NRNFi6Ws2posXUtTRFhrNpWbRrMLWbS1KzreJazatZZ3WsUZ1WarnGo5xuMZrWujUrnK1HTNY10lblc41K3jG46StOcrUrTG43q6wokb01jTRI2M6apGjWdNCNGs6gRrTWdNRYupqGhFTU1LRYupampo1C1m0tRlYJalqM1rMKzatrNZ3WsBNGVc43HONRjNb10jUYlaldM1jcbjUYjUrpmsbjpKrEXWmY3q6xq6rMb0Z00I1ozq6JFE1NCNGpqaEa1NS1LRY0ms6mosa1NTU0qxdZ01NRYtZtLUtZqwqWms1ndaKlpazWN1rMBBKrEajEalYxrW41GI1K3ms7jpKsYlaldM1jcblXWNXW6zG9XWNXVqRrV1jTSpG9NZ00pGtNZ01aRrTWNNSka01nU0qxrU1NTUqxrU1nU1KRrUTUTdaipqams1YqWpalrO6uYVKWs2s7rWYujOqzVjMWMxWcVqVpiVqVvNTcblajm1K3msbjcqs6a1msxvTWdNWkb01nTVqRrTWdNKRrTWdNKRrU1m01Ksa1NZ1NOiN6axpqVY1qazqalI3qazqalWNWozprNWLqalqJutRdREtZqqrAlWCxnVQaWMyqqNStSsaa1UjpKuuerrVSN6usaatSN6uuerq1I3qazqaUjemsaanSxrTWNNTojWprOpqVY3qazpqVY16T0ialIums6alWNaM6aUijJpVi6gms1VE1Chq6yqK0us6atRrVZNWpGlZ01ajQmppSNaus6atI1qammlIumpppSKIiUU1DSkBBKq6hqalVRNNBRkKLoggCAoABoysSrGhBUVdZUF1WQqNDK6tFE1CjQhpRdE00pFNTTSi6moJRdEBQAAEBRAANRKKJU0qtaMqlIgCKumoLUaGVWkUQ0pGhNFRRAFEAUQBRDUANQFECrFNQCKIFF1NBAEBQAABAAAAAAAVBRRAFEBFNQKLogCiAqiAioAoAgAAAAAAAAAAAAAAAAAAAAAAAAAAAKACAAAAAAAAAAAAAAD//2Q==");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color: gray; font-size: 18px;'>Instantly translate text into multiple languages with AI-powered accuracy and speed.</p>",
    unsafe_allow_html=True
)

st.divider()
st.markdown("## Translate text to any language.")

language_to_translate = st.selectbox(
    label="Language to translate to:",
    options=["English", "Urdu", "Arabic", "Chinese","Spanish", "French", "Japanese"]
)

text_to_translate = st.text_area("Paste text here:")
translate_btn = st.button("Translate")

groq_llm = ChatGroq(model="gemma2-9b-it")
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You're a professional translator. Your task is to translate the following text to {language}"),
        ("user", "{text}")
    ]
)

prompt = chat_prompt_template.invoke({
    "language": language_to_translate,
    "text": text_to_translate
})

if translate_btn and text_to_translate.strip() != "":
    with st.spinner("Translating..."):
        placeholder = st.empty()
        full_translation = ""

        for chunk in groq_llm.stream(prompt):
            full_translation += chunk.content
            placeholder.markdown(full_translation)
  

    st.success("Translation complete!")
    st.snow()

elif translate_btn:
    st.error("Please provide the text to translate.")
