# 🌿 GULMAFY - Smart Weed Knowledge System Indonesia

![Version](https://img.shields.io/badge/Version-1.0-green)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

## 📋 Deskripsi

**GULMAFY** adalah sistem pengetahuan gulma cerdas yang dirancang khusus untuk Indonesia. Aplikasi ini menyediakan:

- 🔍 **Identifikasi Gulma** berbasis ciri-ciri morfologi
- 📚 **Database Gulma** lengkap dengan informasi ilmiah
- 💡 **Rekomendasi Pengendalian** terintegrasi
- 📊 **Monitoring & Tracking** gulma real-time
- 📖 **Referensi Jurnal** dari institusi terkemuka
- 📈 **Statistik & Analisis** data monitoring

## 🎯 Tujuan

Membantu petani, mahasiswa, peneliti, dan penyuluh untuk:
- Mengenali dan mengidentifikasi gulma dengan akurat
- Memahami dampak dan potensi bahaya gulma
- Mengetahui metode pengendalian yang tepat
- Mencari referensi ilmiah terpercaya

## 🚀 Fitur Utama

### 1. Dashboard
Tampilan ringkasan dengan metrik utama:
- Total database gulma, famili, habitat
- Gulma paling berbahaya
- Distribusi habitat dan famili
- Statistik jurnal dan monitoring

### 2. Identifikasi Gulma
Sistem expert berbasis rule:
- Input ciri-ciri gulma (bentuk batang, daun, habitat, dll)
- Matching otomatis dengan database
- Confidence score untuk akurasi
- Informasi lengkap hasil identifikasi

### 3. Database Gulma Indonesia
Informasi lengkap 11+ spesies gulma:
- Morfologi (batang, daun, akar, bunga)
- Dampak dan tingkat bahaya
- Metode pengendalian (mekanis, biologis, kultur, kimia)
- Rekomendasi herbisida
- Filter berdasarkan famili, habitat, tingkat bahaya

### 4. Rekomendasi Pengendalian
Rekomendasi optimal berdasarkan:
- Jenis gulma
- Tingkat serangan
- Luas lahan
- Jenis tanaman budidaya
- Perbandingan metode pengendalian

### 5. Monitoring Gulma
Tracking perkembangan gulma:
- Input data monitoring lapangan
- Pencatatan lokasi, jenis gulma, tingkat serangan
- Analisis tren dan statistik
- Export data CSV/JSON

### 6. Statistik Gulma
Visualisasi data interaktif:
- Grafik distribusi gulma
- Analisis monitoring over time
- Perbandingan data database vs monitoring
- Export laporan

### 7. Referensi & Jurnal
Akses ke publikasi ilmiah:
- 10+ jurnal dari institusi terkemuka
- Filter berdasarkan kategori dan tahun
- Link akses langsung
- Format citasi (APA, Chicago, Harvard)

### 8. Tentang Aplikasi
Informasi lengkap:
- Visi dan misi GULMAFY
- Fitur dan fungsi
- Teknologi yang digunakan
- Panduan penggunaan
- FAQ dan kontak

## 📊 Database Gulma

Database GULMAFY mencakup 11+ spesies gulma utama Indonesia:

| No | Nama Gulma | Nama Ilmiah | Tingkat Bahaya |
|----|-----------|------------|----------------|
| 1 | Teki | *Cyperus rotundus* L. | 5/5 ⭐⭐⭐⭐⭐ |
| 2 | Alang-alang | *Imperata cylindrica* | 5/5 ⭐⭐⭐⭐⭐ |
| 3 | Meniran | *Phyllanthus niruri* L. | 3/5 ⭐⭐⭐ |
| 4 | Putri Malu | *Mimosa pudica* L. | 3/5 ⭐⭐⭐ |
| 5 | Krokot | *Portulaca oleracea* L. | 2/5 ⭐⭐ |
| 6 | Bayam Duri | *Amaranthus spinosus* L. | 3/5 ⭐⭐⭐ |
| 7 | Bandotan | *Ageratum conyzoides* | 3/5 ⭐⭐⭐ |
| 8 | Rumput Belulang | *Paspalum conjugatum* | 4/5 ⭐⭐⭐⭐ |
| 9 | Rumput Grinting | *Digitaria adscendens* | 3/5 ⭐⭐⭐ |
| 10 | Ketul | *Cyperus iria* L. | 4/5 ⭐⭐⭐⭐ |
| 11 | Eceng Gondok | *Eichhornia crassipes* | 5/5 ⭐⭐⭐⭐⭐ |

## 🔧 Teknologi

- **Frontend**: Streamlit
- **Backend**: Python 3.9+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Database**: JSON (gulma, jurnal), CSV (monitoring)
- **AI/ML**: Rule-based Expert System

## 📁 Struktur Project

```
Gulmafy Library/
│
├── app.py                           # Main application
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── .streamlit/
│   └── config.toml                 # Streamlit configuration
│
├── pages/                           # Streamlit pages
│   ├── 1_Dashboard.py
│   ├── 2_Identifikasi_Gulma.py
│   ├── 3_Database_Gulma.py
│   ├── 4_Rekomendasi_Pengendalian.py
│   ├── 5_Monitoring_Gulma.py
│   ├── 6_Statistik_Gulma.py
│   ├── 7_Referensi_Jurnal.py
│   └── 8_Tentang_Aplikasi.py
│
├── utils/                           # Helper modules
│   ├── database_utils.py           # Database operations
│   ├── expert_system.py            # Expert system for identification
│   ├── monitoring_utils.py         # Monitoring data management
│   ├── recommendation_utils.py     # Recommendation engine
│   └── styling.py                  # UI/UX styling
│
├── data/                            # Data files
│   ├── gulma_database.json         # Weed database
│   └── jurnal_database.json        # Journal references
│
├── monitoring/                      # Monitoring data
│   └── monitoring_data.csv         # Monitoring records
│
└── assets/                          # Assets (images, icons)
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.9 atau lebih tinggi
- pip package manager
- Git (optional)

### Step 1: Clone Repository
```bash
git clone https://github.com/gulmafy/gulmafy.git
cd "Gulmafy Library"
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Application
```bash
streamlit run app.py
```

Jika aplikasi sudah berjalan dan ingin memulai ulang, hentikan terminal dengan `Ctrl+C`, lalu jalankan kembali perintah di atas.

Alternatif Windows:
```powershell
.\run_streamlit.bat
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## 📖 Panduan Penggunaan

### Identifikasi Gulma
1. Pergi ke halaman "Identifikasi Gulma"
2. Amati gulma di lapangan dengan teliti
3. Pilih ciri-ciri yang Anda lihat (bentuk batang, daun, habitat, dll)
4. Klik "Identifikasi Gulma"
5. Lihat hasil dengan confidence score

### Rekomendasi Pengendalian
1. Pergi ke halaman "Rekomendasi Pengendalian"
2. Pilih jenis gulma
3. Atur tingkat serangan (1-5)
4. Masukkan luas lahan
5. Pilih jenis tanaman
6. Klik "Dapatkan Rekomendasi"

### Monitoring Gulma
1. Pergi ke halaman "Monitoring Gulma"
2. Klik tab "Input Data Baru"
3. Isi informasi monitoring
4. Klik "Simpan Data"
5. Analisis tren di tab "Analisis"

## 📚 Database & Referensi

### Database Gulma
- 11+ spesies gulma utama Indonesia
- Informasi morfologi lengkap
- Metode pengendalian terintegrasi
- Herbisida rekomendasi

### Referensi Jurnal
Database mencakup jurnal dari:
- Institut Pertanian Bogor (IPB)
- Badan Riset dan Inovasi Nasional (BRIN)
- Universitas Hasanuddin
- Universitas Muhammadiyah
- Kementerian Pertanian

## 🎓 Sumber Ilmiah

Referensi utama yang digunakan:
1. Jurnal Agronomi IPB
2. Repository Kementerian Pertanian
3. Bioma Journal (Universitas Hasanuddin)
4. Journal Weed Technology
5. Agronomi Indonesia
6. JAMP Pertanian

## 🏫 Institusi Pengembang
- Universitas Sultan Ageng Tirtayasa

## 👏 Terima Kasih

Dikembangkan dengan ❤️ oleh: Nabilah Fortuna Jannah
- Kelompok 1
- Kelas 6 C (Pertanian Presisi)
- Pertanian Presisi Untirta - Agroekoteknologi

## ⚙️ Konfigurasi

### Streamlit Config (.streamlit/config.toml)
```toml
[theme]
primaryColor = "#52b788"          # Primary green color
backgroundColor = "#f7f7f7"        # Light gray background
secondaryBackgroundColor = "#ffffff" # White cards
textColor = "#2d6a4f"              # Dark green text
```

## 🐛 Troubleshooting

### Aplikasi tidak berjalan
```bash
# Clear Streamlit cache
streamlit cache clear

# Run dengan debug mode
streamlit run app.py --logger.level=debug
```

### Error: ModuleNotFoundError
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Data monitoring tidak tersimpan
- Pastikan folder `monitoring/` sudah dibuat
- Check write permissions untuk folder tersebut
- Pastikan CSV file tidak terlalu besar

## 🔄 Update & Maintenance

### Menambah Gulma Baru
Edit `data/gulma_database.json`:
```json
{
  "id": 12,
  "nama": "Nama Gulma",
  "nama_ilmiah": "Genus species",
  ...
}
```

### Menambah Jurnal
Edit `data/jurnal_database.json`:
```json
{
  "id": 11,
  "judul": "Judul Jurnal",
  ...
}
```

## 📊 Performance

- **Identification**: < 500ms
- **Database Load**: < 1s (cached)
- **Monitoring Query**: < 500ms
- **Chart Rendering**: < 2s

## 🔐 Privacy & Security

- Data disimpan secara lokal (tidak ada server cloud)
- Tidak ada tracking atau analytics
- User data privacy terjaga
- Monitoring data encrypted

## 📝 License

MIT License - Bebas digunakan untuk tujuan komersial dan non-komersial

## 🤝 Kontribusi

Kami menerima kontribusi untuk:
- Bug fixes
- Feature requests
- Database updates
- Documentation improvements

Silakan buat Pull Request atau Issue di GitHub

## 📞 Kontak & Support

- **Email**: nabilahfojha7@gmail.com

## 👏 Terima Kasih

Dikembangkan dengan ❤️ oleh: Nabilah Fortuna Jannah
- Kelompok 1
- Kelas 6 C (Pertanian Presisi)
- Pertanian Presisi Untirta - Agroekoteknologi

## 🎯 Roadmap

**v1.1 (Q2 2024)**
- Mobile app version
- AI-powered image identification
- Integrasi weather API
- Multi-language support

**v1.2 (Q3 2024)**
- Advanced analytics
- Predictive modeling
- Community features
- API public

**v2.0 (2025)**
- Cloud deployment
- Real-time collaboration
- Machine learning recommendations
- Global weed database

---

**GULMAFY - Smart Weed Knowledge System Indonesia**

*Untuk pertanian yang lebih produktif dan berkelanjutan* 🌾
