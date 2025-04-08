import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Generador de títulos virales", layout="centered")

st.title("🔥 Generador de Títulos Virales (Español & English)")
st.write("Escribe un tema y genera ideas virales para TikTok, YouTube, Instagram...")

tema = st.text_input("🎯 Tema o palabra clave", placeholder="Ej: cómo ganar dinero desde casa")

idiomas = st.multiselect("🌐 Selecciona los idiomas", ["Español", "English"], default=["Español", "English"])

if st.button("Generar títulos"):
    if not tema:
        st.warning("Por favor, escribe un tema.")
    else:
        with st.spinner("Generando ideas virales..."):

            # Carga el generador de texto (modelo pequeño y gratuito)
            generator = pipeline("text-generation", model="DeepESP/gpt2-spanish", max_length=60)

            def generar_titulos(texto, n=5):
                return [generator(f"Título viral: {texto}", max_length=50, do_sample=True)[0]['generated_text'].replace("Título viral: ", "") for _ in range(n)]

            if "Español" in idiomas:
                st.subheader("🇪🇸 Títulos en Español")
                titulos_es = generar_titulos(tema)
                for i, t in enumerate(titulos_es, 1):
                    st.markdown(f"{i}. {t}")

            if "English" in idiomas:
                st.subheader("🇬🇧 Titles in English")
                gen_en = pipeline("text-generation", model="gpt2", max_length=60)
                titles_en = [gen_en(f"Viral title: {tema}", max_length=50, do_sample=True)[0]['generated_text'].replace("Viral title: ", "") for _ in range(5)]
                for i, t in enumerate(titles_en, 1):
                    st.markdown(f"{i}. {t}")
