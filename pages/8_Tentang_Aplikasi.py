"""
Page 8: Tentang Aplikasi - GULMAFY Application
"""
import streamlit as st
from utils.styling import apply_custom_css, create_footer

# Configure page
st.set_page_config(
    page_title="Tentang Aplikasi - GULMAFY",
    page_icon="ℹ️",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

st.title("ℹ️ Tentang Aplikasi GULMAFY")
st.markdown("Smart Weed Knowledge System Indonesia")
st.markdown("---")

# Main content tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Tentang GULMAFY",
    "Fitur & Fungsi",
    "Teknologi",
    "Panduan Penggunaan",
    "Kontak & Support"
])

with tab1:
    st.markdown("""
    ## 🌿 Tentang GULMAFY
    
    **GULMAFY** adalah sistem pengetahuan gulma cerdas yang dikembangkan khusus untuk Indonesia.
    Aplikasi ini merupakan hasil dari penelitian dan pengembangan untuk mendukung pertanian berkelanjutan
    dan meningkatkan kesadaran tentang pengelolaan gulma yang lebih baik.
    
    ### 🎯 Misi GULMAFY
    
    Memberikan akses mudah dan cepat kepada informasi ilmiah tentang gulma Indonesia
    sehingga petani, mahasiswa, dan peneliti dapat membuat keputusan yang lebih baik
    dalam pengendalian gulma.
    
    ### 👥 Target Pengguna
    
    - **Petani & Kelompok Tani**: Untuk identifikasi dan pengendalian gulma di lapangan
    - **Mahasiswa Pertanian**: Untuk pembelajaran dan penelitian akademik
    - **Peneliti & Akademisi**: Untuk pengembangan ilmu pengetahuan pertanian
    - **Penyuluh Pertanian**: Untuk edukasi dan pemberdayaan masyarakat
    
    ### 💡 Visi
    
    Menciptakan pertanian Indonesia yang lebih produktif dan berkelanjutan melalui
    manajemen gulma yang efektif, berbasis pengetahuan ilmiah, dan ramah lingkungan.
    
    ### 📈 Keunggulan GULMAFY
    
    ✅ **Berbasis Pengetahuan Lokal**: Database khusus gulma Indonesia
    
    ✅ **Sistem Expert**: Identifikasi berbasis ciri-ciri morfologi
    
    ✅ **Rekomendasi Terintegrasi**: Metode pengendalian multisarprasarana
    
    ✅ **Monitoring Real-time**: Tracking perkembangan gulma di lapangan
    
    ✅ **Interface User-Friendly**: Mudah digunakan oleh semua kalangan
    
    ✅ **Data Ilmiah**: Rujukan dari jurnal dan institusi terpercaya
    """)

with tab2:
    st.markdown("""
    ## 🎨 Fitur & Fungsi GULMAFY
    
    ### 1. 📊 Dashboard
    
    Tampilan ringkasan lengkap dengan:
    - Total database gulma, famili, habitat
    - Gulma paling berbahaya
    - Distribusi habitat dan famili
    - Statistik jurnal
    
    **Manfaat**: Mendapatkan gambaran cepat tentang data gulma Indonesia
    
    ### 2. 🔍 Identifikasi Gulma
    
    Sistem expert berbasis rule yang memungkinkan:
    - Input ciri-ciri gulma (bentuk batang, daun, habitat, dll)
    - Matching otomatis dengan database
    - Confidence score untuk akurasi
    - Informasi lengkap hasil identifikasi
    
    **Manfaat**: Identifikasi akurat gulma tanpa butuh ahli
    
    ### 3. 📚 Database Gulma Indonesia
    
    Database komprehensif dengan:
    - 11+ spesies gulma utama
    - Informasi morfologi lengkap
    - Dampak dan pengendalian
    - Rekomendasi herbisida
    - Filter berdasarkan famili, habitat, danger level
    
    **Manfaat**: Reference lengkap tentang gulma Indonesia
    
    ### 4. 💡 Rekomendasi Pengendalian
    
    Sistem rekomendasi yang mempertimbangkan:
    - Jenis gulma
    - Tingkat serangan
    - Luas lahan
    - Jenis tanaman budidaya
    - Metode pengendalian (mekanis, biologis, kultur, kimia)
    
    **Manfaat**: Pengendalian gulma yang efektif dan terukur
    
    ### 5. 📊 Monitoring Gulma
    
    Fitur tracking dengan kemampuan:
    - Input data monitoring lapangan
    - Pencatatan lokasi, jenis gulma, tingkat serangan
    - Penyimpanan data CSV/JSON
    - Analisis tren monitoring
    
    **Manfaat**: Tracking perkembangan gulma over time
    
    ### 6. 📈 Statistik Gulma
    
    Visualisasi data dengan:
    - Grafik distribusi gulma
    - Analisis monitoring
    - Perbandingan data
    - Export laporan
    
    **Manfaat**: Insight mendalam tentang pola gulma
    
    ### 7. 📖 Referensi & Jurnal
    
    Akses ke publikasi ilmiah:
    - 10+ jurnal dari institusi terkemuka
    - Filter berdasarkan kategori dan tahun
    - Link akses langsung
    - Format citasi
    
    **Manfaat**: Pembelajaran dari sumber ilmiah terpercaya
    
    ### 8. ℹ️ Tentang Aplikasi
    
    Informasi lengkap tentang:
    - Visi dan misi GULMAFY
    - Fitur dan fungsi
    - Teknologi yang digunakan
    - Panduan penggunaan
    - Kontak dan support
    """)

with tab3:
    st.markdown("""
    ## 🔧 Teknologi yang Digunakan
    
    ### Backend & Frontend
    
    - **Streamlit**: Web framework interaktif untuk data science
    - **Python 3.9+**: Bahasa pemrograman utama
    - **Pandas**: Data manipulation dan analysis
    - **Plotly**: Visualisasi data interaktif dan modern
    
    ### Database & Storage
    
    - **JSON**: Format penyimpanan database gulma dan jurnal
    - **CSV**: Format monitoring data
    - **Local Storage**: Penyimpanan lokal untuk privacy
    
    ### Sistem Artificial Intelligence
    
    - **Rule-Based Expert System**: Identifikasi berbasis aturan
    - **Fuzzy Matching**: Pencarian dan matching ciri-ciri
    - **Confidence Scoring**: Perhitungan akurasi identifikasi
    
    ### Architecture
    
    ```
    GULMAFY Structure:
    ├── app.py (Main Application)
    ├── pages/ (8 halaman fitur)
    ├── utils/ (Helper modules)
    │   ├── database_utils.py
    │   ├── expert_system.py
    │   ├── recommendation_utils.py
    │   ├── monitoring_utils.py
    │   └── styling.py
    ├── data/ (Databases)
    │   ├── gulma_database.json
    │   ├── jurnal_database.json
    └── monitoring/ (Data monitoring)
        └── monitoring_data.csv
    ```
    
    ### Requirements
    
    - streamlit >= 1.28
    - pandas >= 1.5
    - plotly >= 5.0
    - pillow >= 9.0
    - numpy >= 1.23
    
    ### Deployment
    
    - **Local**: Streamlit run app.py
    - **Server**: Streamlit Cloud, Heroku, AWS, GCP
    - **Desktop**: PyInstaller packaging
    
    ### Performance
    
    - **Caching**: @st.cache_data untuk optimasi loading
    - **Lazy Loading**: Loading on-demand untuk efisiensi
    - **Responsive Design**: Mobile-friendly interface
    - **Fast Identification**: Expert system real-time
    """)

with tab4:
    st.markdown("""
    ## 📖 Panduan Penggunaan Lengkap
    
    ### 🚀 Memulai
    
    1. Buka aplikasi GULMAFY di browser Anda
    2. Lihat Dashboard untuk overview
    3. Pilih fitur yang ingin digunakan dari sidebar
    
    ### 📖 Tutorial Fitur
    
    #### Identifikasi Gulma
    
    **Langkah-langkah:**
    1. Pergi ke halaman "Identifikasi Gulma"
    2. Amati gulma di lapangan dengan teliti
    3. Pilih ciri-ciri yang Anda lihat:
       - Bentuk batang (segitiga, bulat, dll)
       - Tipe daun (sempit, lebar, dll)
       - Warna daun
       - Habitat (sawah, tegalan, dll)
       - Tipe akar
       - Bunga/perbungaan
       - Pola pertumbuhan
    4. Semakin banyak ciri yang dipilih, semakin akurat
    5. Klik "Identifikasi Gulma"
    6. Lihat hasil dengan confidence score
    7. Klik hasil untuk info detail
    
    #### Rekomendasi Pengendalian
    
    **Langkah-langkah:**
    1. Pergi ke halaman "Rekomendasi Pengendalian"
    2. Pilih jenis gulma dari dropdown
    3. Atur tingkat serangan dengan slider (1-5)
    4. Masukkan luas lahan dalam hektar
    5. Pilih jenis tanaman budidaya
    6. Klik "Dapatkan Rekomendasi"
    7. Lihat rekomendasi metode pengendalian
    8. Download rekomendasi jika diperlukan
    
    #### Monitoring Gulma
    
    **Langkah-langkah:**
    1. Pergi ke halaman "Monitoring Gulma"
    2. Klik tab "Input Data Baru"
    3. Isi informasi:
       - Lokasi pengamatan
       - Jenis gulma
       - Tingkat serangan
       - Tanggal pengamatan
       - Catatan tambahan
    4. Klik "Simpan Data"
    5. Lihat data di tab "Lihat Data"
    6. Analisis tren di tab "Analisis"
    
    ### 💡 Tips & Trik
    
    - Gunakan Database Gulma untuk referensi sebelum identifikasi
    - Amati gulma saat siang hari untuk hasil terbaik
    - Catat foto gulma untuk verifikasi lebih lanjut
    - Lakukan monitoring rutin untuk tracking akurat
    - Export data monitoring untuk laporan
    - Gunakan referensi jurnal untuk pembelajaran mendalam
    
    ### ⚠️ Limitasi
    
    - Akurasi identifikasi tergantung pada detail ciri yang diinput
    - Database terbatas pada gulma utama Indonesia
    - Memerlukan pengetahuan dasar morfologi gulma
    """)

with tab5:
    st.markdown("""
    ## 📞 Kontak & Support
    
    ### 📧 Email
    
    **Support Team:**
    - 4442230002@untirta.ac.id
    - 4442230003@untirta.ac.id
    - 4442230082@untirta.ac.id
    - 4442230086@untirta.ac.id
    
    **Feedback & Suggestion:**
    - feedback@gulmafy.id
    
    ### 📱 Media Sosial
    
    - Instagram: @gulmafy_indonesia
    - Facebook: GULMAFY Indonesia
    - LinkedIn: GULMAFY
    - Twitter: @gulmafy_id
    
    ### 🏫 Institusi Pengembang
    
    - **Universitas Sultan Ageng Tirtayasa**
    
    ### 📋 FAQ (Frequently Asked Questions)
    
    **Q: Apakah GULMAFY menggunakan AI/Deep Learning?**
    A: Iya, Gulmafy menggunakan sistem AI/Deep Learning ringan untuk mengidentifikasi gulma
    
    **Q: Berapa akurasi identifikasi GULMAFY?**
    A: Akurasi tergantung pada detail ciri input. Dengan 5+ ciri, akurasi 70-90%.
    
    **Q: Bagaimana cara menggunakan monitoring?**
    A: Lihat panduan di tab "Panduan Penggunaan" halaman ini.
    
    **Q: Bisakah saya export data?**
    A: Ya, semua data dapat diexport dalam format CSV atau JSON.
    
    **Q: Apakah aplikasi ini gratis?**
    A: Ya, GULMAFY adalah aplikasi open-source yang gratis untuk semua pengguna.
    
    **Q: Bagaimana cara menambah database gulma baru?**
    A: Hubungi tim support kami dengan data lengkap.
    
    ### 🐛 Bug Reporting
    
    Jika Anda menemukan bug atau error:
    1. Catat langkah-langkah untuk reproduce bug
    2. Email ke support@gulmafy.id dengan:
       - Deskripsi bug
       - Screenshot
       - Browser/device yang digunakan
       - Langkah-langkah reproduce
    
    ### 💬 Feedback
    
    Kami sangat menghargai feedback dan saran Anda untuk pengembangan GULMAFY.
    Silakan kirim feedback ke feedback@gulmafy.id
    
    ### 📚 Dokumentasi Lengkap
    
    - GitHub Repository: github.com/gulmafy/gulmafy
    - API Documentation: docs.gulmafy.id
    - User Guide: guide.gulmafy.id
    """)

st.markdown("---")
create_footer()
