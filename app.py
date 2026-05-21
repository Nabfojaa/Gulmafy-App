"""
GULMAFY - Smart Weed Knowledge System Indonesia
Main application file - Modern Premium Design
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils.styling import apply_custom_css, create_footer, format_scientific_name
from utils.database_utils import (
    load_gulma_database, 
    load_jurnal_database,
    get_database_statistics,
    get_most_dangerous_gulma,
    get_all_famili,
    get_all_habitat
)

# Configure page
st.set_page_config(
    page_title="GULMAFY - Smart Weed Knowledge System Indonesia",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_custom_css()

# Sidebar Header
st.sidebar.markdown("""
<div style="text-align: center; padding: 30px 0; border-bottom: 2px solid rgba(255, 255, 255, 0.1); margin-bottom: 20px;">
    <h1 style="color: white; font-size: 2em; margin: 0;">🌿 GULMAFY</h1>
    <p style="color: rgba(255, 255, 255, 0.8); font-size: 0.9em; margin: 10px 0 0 0;">Smart Weed Knowledge System</p>
</div>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div style="background: linear-gradient(135deg, #1B4332 0%, #2D6A4F 50%, #52B788 100%);
            padding: 50px 30px;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 40px;
            box-shadow: 0 12px 32px rgba(27, 67, 50, 0.2);">
    <h1 style="color: white; margin: 0; font-size: 3em; font-weight: 800; letter-spacing: -1px;">🌿 GULMAFY</h1>
   <p style="
    color: #FFFFFF;
    margin: 15px 0 0 0;
    font-size: 1.2em;
    font-weight: 800;
    text-shadow:
        0 0 6px rgba(255,255,255,0.85),
        0 0 12px rgba(255,255,255,0.75),
        0 0 18px rgba(255,255,255,0.65),
        0 3px 12px rgba(0,0,0,0.28);
">
    Smart Weed Knowledge System Indonesia
</p>

<p style="
    color: #FFFFFF;
    margin: 10px 0 0 0;
    font-size: 1rem;
    font-weight: 700;
    text-shadow:
        0 0 5px rgba(245,255,255,0.8),
        0 0 10px rgba(245,255,255,0.7),
        0 0 15px rgba(245,255,255,0.55),
        0 2px 10px rgba(0,0,0,0.25);
">
    Sistem Pengetahuan Gulma Cerdas untuk Pertanian Presisi
</p>
</div>
""", unsafe_allow_html=True)

# Get statistics
stats = get_database_statistics()
database = load_gulma_database()
jurnal = load_jurnal_database()

# Key Metrics
st.markdown("### 📈 Statistik Database")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("📋 Total Gulma", stats["total_gulma"], delta="spesies database", delta_color="off")
with col2:
    st.metric("🏷️ Famili", stats["total_famili"], delta="jenis famili", delta_color="off")
with col3:
    st.metric("🌍 Habitat", stats["total_habitat"], delta="tipe habitat", delta_color="off")
with col4:
    st.metric("📚 Jurnal", stats["total_jurnal"], delta="referensi akademik", delta_color="off")
with col5:
    st.metric("⚠️ Berbahaya", stats["dangerous_count"], delta="tingkat ≥4", delta_color="off")

st.markdown("---")

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview Dashboard",
    "⚠️ Gulma Berbahaya",
    "📖 Informasi Aplikasi",
    "🎓 Panduan Penggunaan"
])

with tab1:
    st.markdown("#### 📊 Dashboard Utama GULMAFY")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(27, 67, 50, 0.08) 0%, rgba(82, 183, 136, 0.08) 100%);
                    border-radius: 16px;
                    padding: 24px;
                    border: 2px solid #74C69D;
                    margin-bottom: 20px;">
            <h3 style="color: #1B4332; margin-top: 0;">💡 Tentang GULMAFY</h3>
            <p style="color: #333; line-height: 1.8;">
            GULMAFY adalah sistem pengetahuan gulma cerdas yang dirancang untuk membantu petani, peneliti, dan
            praktisi pertanian Indonesia dalam mengidentifikasi, memahami, dan mengendalikan gulma secara efektif.
            </p>
            <p style="color: #333; line-height: 1.8;">
            Sistem ini menggunakan teknologi AI dan database ilmiah terpercaya untuk memberikan rekomendasi 
            pengendalian yang akurat dan ramah lingkungan.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### ✨ Fitur Utama")
        features = [
            ("🔍", "Identifikasi Gulma", "Identifikasi gulma berdasarkan ciri-ciri morfologi"),
            ("📋", "Database Lengkap", "Database 11+ spesies gulma dengan data ilmiah"),
            ("💊", "Rekomendasi Pengendalian", "Metode kimia, mekanis, dan biologis terintegrasi"),
            ("📊", "Monitoring Real-time", "Tracking perkembangan gulma di lapangan"),
            ("📚", "Jurnal Referensi", "Basis data jurnal ilmiah terkini"),
            ("📈", "Statistik Analisis", "Visualisasi data monitoring dan analisis tren")
        ]
        
        for icon, title, desc in features:
            st.markdown(f"""
            <div style="background: white; border-left: 4px solid #52B788; padding: 12px; margin: 8px 0; border-radius: 8px;">
                <p style="margin: 0; font-weight: 600; color: #1B4332;">{icon} {title}</p>
                <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #666;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 📊 Distribusi Gulma Berdasarkan Tingkat Bahaya")
        
        # Create pie chart
        danger_counts = [len([g for g in database if g["tingkat_bahaya"] == i]) for i in range(1, 6)]
        danger_labels = ["Rendah (1)", "Rendah-Sedang (2)", "Sedang (3)", "Tinggi (4)", "Sangat Tinggi (5)"]
        danger_colors = ["#2D6A4F", "#52B788", "#F59E0B", "#F97316", "#DC2626"]
        
        fig = go.Figure(data=[go.Pie(
            labels=danger_labels,
            values=danger_counts,
            marker=dict(colors=danger_colors),
            textinfo='label+value+percent',
            hoverinfo='label+value+percent'
        )])
        
        fig.update_layout(
            height=400,
            template="plotly_white",
            font=dict(size=11),
            showlegend=True
        )
        
        st.plotly_chart(fig, width='stretch')
        
        st.markdown("#### 🏆 Top 5 Gulma Paling Berbahaya")
        dangerous = get_most_dangerous_gulma(5, database)
        
        for idx, weed in enumerate(dangerous, 1):
            danger_level = weed["tingkat_bahaya"]
            
            # Color based on danger level
            if danger_level == 5:
                color = "#d32f2f"
                badge = "🔴 Sangat Tinggi"
            elif danger_level == 4:
                color = "#f57c00"
                badge = "🟠 Tinggi"
            else:
                color = "#fbc02d"
                badge = "🟡 Sedang"
            
            st.markdown(f"""
            <div style="background: white;
                        border-left: 4px solid {color};
                        padding: 12px;
                        margin: 8px 0;
                        border-radius: 8px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <p style="margin: 0; font-weight: 700; color: {color};">{idx}. {weed['nama']}</p>
                <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #666;">{format_scientific_name(weed['nama_ilmiah'])}</p>
                <p style="margin: 4px 0 0 0; font-size: 0.85em; color: white; display: inline-block; background: {color}; padding: 2px 8px; border-radius: 12px;">{badge}</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### ⚠️ Gulma 5 Paling Berbahaya")
    
    dangerous = get_most_dangerous_gulma(5, database)
    
    for idx, weed in enumerate(dangerous, 1):
        with st.expander(f"{idx}. {weed['nama']} - ⭐ Tingkat Bahaya: {weed['tingkat_bahaya']}/5", expanded=(idx==1)):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(74, 145, 108, 0.1) 0%, rgba(116, 198, 157, 0.1) 100%);
                            border-radius: 12px;
                            padding: 16px;
                            text-align: center;">
                    <h3 style="color: #1B4332; margin-top: 0; font-size: 1.5em;">⚠️</h3>
                    <p style="margin: 8px 0; font-weight: 700; color: #1B4332;">Tingkat Bahaya</p>
                    <p style="margin: 8px 0; font-size: 2em; font-weight: 800; color: #d32f2f;">{weed['tingkat_bahaya']}/5</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                **Nama Lokal:** {weed['nama']}
                
                **Nama Ilmiah:** {format_scientific_name(weed['nama_ilmiah'])}
                
                **Famili:** {weed['famili']}
                
                **Habitat:** {', '.join(weed['habitat']) if isinstance(weed['habitat'], list) else weed['habitat']}
                
                **Deskripsi:** {weed['deskripsi'] if 'deskripsi' in weed else 'Data tidak tersedia'}
                
                **Dampak:** {weed['dampak_tanaman'] if 'dampak_tanaman' in weed else 'Data tidak tersedia'}
                """, unsafe_allow_html=True)

with tab3:
    st.markdown("#### 📖 Tentang Aplikasi GULMAFY")
    
    st.markdown("""
    ##### Visi
    Menjadi sistem pengetahuan gulma terkemuka di Indonesia yang mendukung pertanian presisi
    dan berkelanjutan melalui teknologi AI dan data ilmiah.
    
    ##### Misi
    - Menyediakan informasi gulma yang akurat dan mudah diakses
    - Membantu petani dalam identifikasi dan pengendalian gulma
    - Mendukung penelitian pertanian berkelanjutan
    - Mengintegrasikan pengetahuan tradisional dengan teknologi modern
    
    ##### Tim Pengembang
    - **Institusi:** Universitas Sultan Ageng Tirtayasa (Untirta)
    - **Program Studi:** Agroekoteknologi
    - **Kelompok:** Pertanian Presisi Kelompok 1 (6C)
    - **Tahun:** 2026
    
    ##### Sumber Data
    - Database gulma dari penelitian pertanian Indonesia terkini
    - Jurnal ilmiah dari institusi penelitian nasional dan internasional
    - Konsultasi dengan ahli agronomis dan botanis
    - Data monitoring lapangan dari berbagai wilayah pertanian Indonesia
    """)

with tab4:
    st.markdown("#### 🎓 Panduan Penggunaan GULMAFY")
    
    st.markdown("""
    ##### 1️⃣ Identifikasi Gulma
    Halaman **Identifikasi Gulma** membantu Anda mengidentifikasi gulma berdasarkan ciri-ciri morfologi:
    - Pilih ciri-ciri yang Anda amati di lapangan
    - Semakin banyak ciri yang dipilih, semakin akurat hasil identifikasi
    - Sistem akan menampilkan hasil dengan confidence score dan peringkat
    
    ##### 2️⃣ Database Gulma
    Halaman **Database Gulma** menyediakan informasi lengkap tentang setiap spesies:
    - Klasifikasi ilmiah lengkap
    - Ciri-ciri morfologi detail
    - Habitat dan distribusi
    - Metode pengendalian
    
    ##### 3️⃣ Rekomendasi Pengendalian
    Dapatkan rekomendasi pengendalian yang disesuaikan dengan jenis gulma:
    - Metode pengendalian mekanis
    - Metode pengendalian biologis
    - Rekomendasi herbisida spesifik
    - Praktik terbaik pertanian
    
    ##### 4️⃣ Monitoring Gulma
    Tracking real-time perkembangan gulma di lapangan:
    - Catat observasi gulma di berbagai lokasi
    - Monitor tingkat serangan
    - Analisis tren monitoring
    - Export data untuk analisis lebih lanjut
    
    ##### 5️⃣ Statistik & Analisis
    Visualisasi data monitoring dengan chart modern:
    - Distribusi jenis gulma
    - Trend perkembangan
    - Analisis berdasarkan lokasi dan waktu
    
    ##### 💡 Tips Penggunaan
    - Gunakan fitur pencarian untuk menemukan gulma spesifik
    - Baca deskripsi lengkap untuk pemahaman mendalam
    - Ikuti rekomendasi pengendalian yang diberikan
    - Catat monitoring secara berkala untuk analisis tren
    """)

st.markdown("---")
create_footer()