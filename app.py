import streamlit as st
from google import genai
from google.genai import types
import pandas as pd
import json
import os
import re
from dotenv import load_dotenv

load_dotenv("env")
API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="AI Info Extractor Pro", layout="wide")

if not API_KEY:
    st.error("Error: GEMINI_API_KEY tidak ditemukan.")
    st.stop()

# Inisialisasi client baru
client = genai.Client(api_key=API_KEY)

st.title("AI Information Extractor Pro")

if "extracted_df" not in st.session_state:
    st.session_state.extracted_df = None

with st.form("extraction_form"):
    input_text = st.text_area("Masukkan teks:", height=200)
    submitted = st.form_submit_button("Ekstrak ke Tabel")

if submitted:
    if not input_text.strip():
        st.warning("Teks tidak boleh kosong.")
    elif len(input_text) > 50000:
        st.error("Teks terlalu panjang.")
    else:
        with st.spinner("Memproses data..."):
            try:
                system_instruction = (
                    "Kamu adalah asisten ekstraksi data. Ekstrak informasi dari teks "
                    "dan kembalikan HANYA dalam format JSON array of objects."
                )
                
                # Menggunakan library google-genai terbaru
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=input_text,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        response_mime_type="application/json"
                    )
                )
                
                raw_text = response.text.strip()
                clean_json = re.sub(r"^```json\s*|\s*```$", "", raw_text, flags=re.MULTILINE).strip()
                
                data = json.loads(clean_json)
                
                if isinstance(data, dict):
                    list_keys = [k for k, v in data.items() if isinstance(v, list)]
                    data = data[list_keys[0]] if list_keys else [data]
                
                df = pd.json_normalize(data)
                st.session_state.extracted_df = df
                st.success("Berhasil!")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

if st.session_state.extracted_df is not None:
    st.dataframe(st.session_state.extracted_df, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="Unduh CSV",
            data=st.session_state.extracted_df.to_csv(index=False),
            file_name="data.csv",
            mime="text/csv"
        )
        
    with col2:
        st.download_button(
            label="Unduh JSON",
            data=st.session_state.extracted_df.to_json(orient="records"),
            file_name="data.json",
            mime="application/json"
        )