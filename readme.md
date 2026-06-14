# AI Info Extractor Pro

Aplikasi berbasis web untuk mengekstrak informasi dari teks tidak terstruktur menjadi format tabel terstruktur menggunakan AI.

## Arsitektur Sistem

* **Frontend:** Streamlit.
* **Backend/AI:** Google GenAI SDK dengan model `gemini-3.5-flash`.
* **Pemrosesan Data:** Instruksi sistem dikonfigurasi untuk mengembalikan JSON, dibersihkan menggunakan Regex, lalu dikonversi menjadi Pandas DataFrame.
* **Output:** Tabel interaktif, opsi unduh CSV dan JSON.

## Kebutuhan Sistem

Library yang dibutuhkan:
* `streamlit`
* `google-genai`
* `pandas`
* `python-dotenv`

## Struktur Repositori

```text
.
├── app.py              # File skrip utama aplikasi
├── .streamlit/
│   └── secrets.toml    # File untuk menyimpan API Key (lokal)
├── .gitignore          # File untuk mengabaikan kredensial
├── requirements.txt    # Daftar library yang dibutuhkan
└── readme.md           # Dokumentasi repositori
```

## Instruksi Instalasi & Penggunaan
### Menjalankan di Komputer Lokal
1.  **Clone Repositori:**

    ```bash
    git clone [https://github.com/law182-lang/ai-info-extractor.git](https://github.com/law182-lang/ai-info-extractor.git)cd ai-info-extractor 
    ```

2.  **Konfigurasi API Key:**

    Buat folder .streamlit dan file secrets.toml di dalam folder root. Masukkan API Key Anda:

    ```bash
    GEMINI_API_KEY="api_key_anda_disini"
    ```

3.  **Install Dependensi:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi:**

    ```bash
    streamlit run app.py
    ```

### Deploy ke Streamlit Community Cloud

1. **Pastikan folder .streamlit/ dan file .env sudah terdaftar di .gitignore agar tidak terunggah ke GitHub.**

2. **Push kode terbaru ke GitHub repositori Anda.**

3. **Login ke share.streamlit.io.**

4. **Klik New app, lalu pilih repositori law182-lang/ai-info-extractor,branch main, dan Main file path app.py.**

5. **Klik Advanced settings..., masuk ke bagian Secrets, dan tambahkan:**

```bash
GEMINI_API_KEY="api_key_anda_disini"
```

6. **Klik Save, lalu Deploy!.**

