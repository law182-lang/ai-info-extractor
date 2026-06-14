Python  
markdown\_content \= """\# AI Info Extractor Pro

Aplikasi berbasis web untuk mengekstrak informasi dari teks tidak terstruktur menjadi format tabel terstruktur menggunakan AI.

\#\# Arsitektur Sistem

\* \*\*Frontend:\*\* Streamlit.  
\* \*\*Backend/AI:\*\* Google GenAI SDK dengan model \`gemini-3.5-flash\`.  
\* \*\*Pemrosesan Data:\*\* Instruksi sistem dikonfigurasi untuk mengembalikan JSON, dibersihkan menggunakan Regex, lalu dikonversi menjadi Pandas DataFrame.  
\* \*\*Output:\*\* Tabel interaktif, opsi unduh CSV dan JSON.

\#\# Kebutuhan Sistem

Library yang dibutuhkan:  
\* \`streamlit\`  
\* \`google-genai\`  
\* \`pandas\`  
\* \`python-dotenv\`

\#\# Struktur Repositori

Output kode

File README.md successfully created.

\`\`\`text  
.  
├── app.py              \# File skrip utama aplikasi   
├── .streamlit/  
│   └── secrets.toml    \# File untuk menyimpan API Key (lokal)  
├── .gitignore          \# File untuk mengabaikan kredensial  
├── requirements.txt    \# Daftar library yang dibutuhkan  
└── README.md           \# Dokumentasi repositori

## **Instruksi Instalasi & Penggunaan**

### **1\. Menjalankan di Komputer Lokal**

**Clone Repositori:**

Bash  
git clone \[https://github.com/law182-lang/ai-info-extractor.git\](https://github.com/law182-lang/ai-info-extractor.git)  
cd ai-info-extractor

**Konfigurasi API Key:**  
Buat folder .streamlit dan file secrets.toml di dalam folder root. Masukkan API Key Anda:

Ini, TOML  
GEMINI\_API\_KEY\="api\_key\_anda\_disini"

**Install Dependensi:**

Bash  
pip install \-r requirements.txt

**Jalankan Aplikasi:**

Bash  
streamlit run app.py

### **2\. Deploy ke Streamlit Community Cloud**

1. Pastikan folder .streamlit/ dan file .env sudah terdaftar di .gitignore agar tidak terunggah ke GitHub.  
2. Push kode terbaru ke GitHub repositori Anda.  
3. Login ke share.streamlit.io.  
4. Klik **New app**, lalu pilih repositori law182-lang/ai-info-extractor, branch main, dan Main file path app.py.  
5. Klik **Advanced settings...**, masuk ke bagian **Secrets**, dan tambahkan:  
   Ini, TOML  
   GEMINI\_API\_KEY\="api\_key\_anda\_disini"

6. Klik **Save**, lalu **Deploy\!**.  
   """

with open("README.md", "w", encoding="utf-8") as f:  
f.write(markdown\_content)  
print("File README.md successfully created.")

File MD Anda sudah siap  
\[file-tag: code-generated-file-0-1781420375909078282\]

Berikut adalah teks format Markdown jika Anda ingin langsung menyalinnya:

\`\`\`markdown  
\# AI Info Extractor Pro

Aplikasi berbasis web untuk mengekstrak informasi dari teks tidak terstruktur menjadi format tabel terstruktur menggunakan AI.

\#\# Arsitektur Sistem

\* \*\*Frontend:\*\* Streamlit.  
\* \*\*Backend/AI:\*\* Google GenAI SDK dengan model \`gemini-3.5-flash\`.  
\* \*\*Pemrosesan Data:\*\* Instruksi sistem dikonfigurasi untuk mengembalikan JSON, dibersihkan menggunakan Regex, lalu dikonversi menjadi Pandas DataFrame.  
\* \*\*Output:\*\* Tabel interaktif, opsi unduh CSV dan JSON.

\#\# Kebutuhan Sistem

Library yang dibutuhkan:  
\* \`streamlit\`  
\* \`google-genai\`  
\* \`pandas\`  
\* \`python-dotenv\`

\#\# Struktur Repositori

\`\`\`text  
.  
├── app.py              \# File skrip utama aplikasi   
├── .streamlit/  
│   └── secrets.toml    \# File untuk menyimpan API Key (lokal)  
├── .gitignore          \# File untuk mengabaikan kredensial  
├── requirements.txt    \# Daftar library yang dibutuhkan  
└── README.md           \# Dokumentasi repositori

## **Instruksi Instalasi & Penggunaan**

### **1\. Menjalankan di Komputer Lokal**

**Clone Repositori:**

Bash  
git clone \[https://github.com/law182-lang/ai-info-extractor.git\](https://github.com/law182-lang/ai-info-extractor.git)  
cd ai-info-extractor

**Konfigurasi API Key:**  
Buat folder .streamlit dan file secrets.toml di dalam folder root. Masukkan API Key Anda:

Ini, TOML  
GEMINI\_API\_KEY\="api\_key\_anda\_disini"

**Install Dependensi:**

Bash  
pip install \-r requirements.txt

**Jalankan Aplikasi:**

Bash  
streamlit run app.py

### **2\. Deploy ke Streamlit Community Cloud**

1. Pastikan folder .streamlit/ dan file .env sudah terdaftar di .gitignore agar tidak terunggah ke GitHub.  
2. Push kode terbaru ke GitHub repositori Anda.  
3. Login ke share.streamlit.io.  
4. Klik **New app**, lalu pilih repositori law182-lang/ai-info-extractor, branch main, dan Main file path app.py.  
5. Klik **Advanced settings...**, masuk ke bagian **Secrets**, dan tambahkan:  
   Ini, TOML  
   GEMINI\_API\_KEY\="api\_key\_anda\_disini"

6. Klik **Save**, lalu **Deploy\!**.