"""
Page 4: Rekomendasi Pengendalian - GULMAFY Application
"""
import streamlit as st
import pandas as pd
from utils.styling import apply_custom_css, create_footer, format_scientific_name
from utils.image_utils import display_weed_image
from utils.recommendation_utils import recommendation_engine
from utils.database_utils import load_gulma_database, get_all_gulma_names
from utils.herbisida_db import get_herbisida_for_gulma, display_herbisida_card

# Configure page
st.set_page_config(
    page_title="Rekomendasi Pengendalian - GULMAFY",
    page_icon="💡",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

st.markdown("""
<h1 style="color: var(--primary-dark); text-align: center; margin-bottom: 10px; font-size: 2.2rem; font-weight: 800;">💡 Rekomendasi Pengendalian Gulma</h1>
""", unsafe_allow_html=True)
st.markdown("Dapatkan rekomendasi pengendalian gulma yang tepat berdasarkan kondisi Anda", unsafe_allow_html=True)
st.markdown("---")

st.info("""
💡 **Cara Menggunakan:**
1. Pilih jenis gulma yang ingin dikendalikan
2. Masukkan tingkat serangan, luas lahan, dan jenis tanaman
3. Sistem akan memberikan rekomendasi pengendalian yang optimal
4. Bandingkan berbagai metode pengendalian
""")

# Input form
st.markdown("---")
st.markdown("### 📋 Input Informasi Lahan")

col1, col2 = st.columns(2)

with col1:
    # Weed selection
    gulma_names = get_all_gulma_names(load_gulma_database())
    selected_gulma = st.selectbox(
        "🌿 Pilih Jenis Gulma",
        gulma_names
    )
    
    # Attack level
    attack_level = st.slider(
        "📊 Tingkat Serangan",
        min_value=1,
        max_value=5,
        value=3,
        help="1 = Ringan, 5 = Sangat Berat"
    )
    
    # Luas lahan
    field_size = st.number_input(
        "📐 Luas Lahan (Hektar)",
        min_value=0.1,
        value=1.0,
        step=0.5
    )

with col2:
    # Crop type
    crop_type = st.selectbox(
        "🌾 Jenis Tanaman Budidaya",
        [
            "Padi",
            "Jagung",
            "Kacang",
            "Sayuran",
            "Buah-buahan",
            "Perkebunan",
            "Lainnya"
        ]
    )
    
    # Available resources
    available_resources = st.multiselect(
        "🛠️ Sumber Daya Tersedia",
        [
            "Tenaga kerja manual",
            "Peralatan mekanis",
            "Akses herbisida",
            "Musuh alami",
            "Pupuk organik"
        ],
        default=["Tenaga kerja manual"]
    )

# Generate recommendations button
st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🔍 Dapatkan Rekomendasi", width='stretch', type="primary"):
        # Get recommendations
        recommendations = recommendation_engine.get_recommendations(
            selected_gulma,
            attack_level=attack_level,
            field_size=field_size,
            crop_type=crop_type
        )
        
        if recommendations:
            st.markdown("---")
            st.markdown("### ✅ Rekomendasi Pengendalian")
            
            # Urgency indicator
            urgency_emoji = {
                1: "🟢",
                2: "🟢",
                3: "🟡",
                4: "🟠",
                5: "🔴"
            }
            
            col1, col2 = st.columns([0.95, 1.05], gap="medium")
            
            with col1:
                st.markdown('<div style="padding: 8px;">', unsafe_allow_html=True)
                st.markdown(f"### {recommendations['gulma']}")
                st.markdown(f"**{format_scientific_name(recommendations['nama_ilmiah'])}**", unsafe_allow_html=True)
                st.markdown(f"**Tingkat Bahaya:** {'⭐' * recommendations['tingkat_bahaya']}")
                
                # Display weed image
                st.markdown("#### 🌿 Gambar Gulma")
                image_displayed = display_weed_image(recommendations['gulma'], width="stretch")
                if not image_displayed:
                    st.info("Gambar gulma belum tersedia di database")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div style="padding: 8px;">', unsafe_allow_html=True)
                st.markdown(f"### {urgency_emoji[recommendations['urgency']]} Status Urgensi")
                st.warning(recommendations['prioritas'])
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Recommendations tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "Mekanis",
                "Biologis",
                "Kultur Teknis",
                "Kimiawi (Herbisida)",
                "Perbandingan Metode"
            ])
            
            with tab1:
                st.markdown("### 🔧 Pengendalian Mekanis")
                st.info(recommendations["metode_mekanis"])
            
            with tab2:
                st.markdown("### 🦋 Pengendalian Biologis")
                st.info(recommendations["metode_biologis"])
            
            with tab3:
                st.markdown("### 🌾 Pengendalian Kultur Teknis")
                st.info(recommendations["metode_kultur"])
            
            with tab4:
                st.markdown("### 💊 Pengendalian Kimiawi")
                
                if recommendations["herbisida"]:
                    for herb_rec in recommendations["herbisida"]:
                        st.markdown(f"**{herb_rec['nama']}**")
                        st.markdown(f"- Dosis: {herb_rec['dosis']}")
                        st.markdown(f"- Waktu Aplikasi: {herb_rec['waktu_aplikasi']}")
                        st.markdown(f"- Catatan: {herb_rec['catatan']}")
                        st.markdown("")
                
                # Add Indonesian Herbicide Database options
                st.markdown("---")
                st.markdown("#### 🌿 Herbisida Indonesia Tersedia")
                st.markdown("*Pilihan herbisida yang tersedia di pasaran Indonesia dengan spesifikasi lengkap:*")
                
                indonesian_herbicides = get_herbisida_for_gulma(selected_gulma)
                if indonesian_herbicides:
                    herb_cols = st.columns(min(2, len(indonesian_herbicides)))
                    for i, merk_dagang in enumerate(indonesian_herbicides):
                        with herb_cols[i % 2]:
                            display_herbisida_card(merk_dagang)
                else:
                    st.info("Herbisida khusus untuk gulma ini sedang dikurasi. Silakan konsultasi dengan ahli pertanian.")
            
            with tab5:
                st.markdown("### 🔄 Perbandingan Metode Pengendalian")
                
                comparison = recommendation_engine.compare_methods(selected_gulma)
                
                if comparison:
                    for method in comparison["methods"]:
                        with st.expander(f"**{method['metode']}**"):
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.markdown(f"**Deskripsi:**")
                                st.markdown(method["deskripsi"])
                            
                            with col2:
                                st.markdown(f"**Karakteristik:**")
                                st.markdown(f"- **Efektivitas:** {method['efektivitas']}")
                                st.markdown(f"- **Biaya:** {method['biaya']}")
                                st.markdown(f"- **Waktu:** {method['waktu']}")
                                st.markdown(f"- **Ramah Lingkungan:** {method['ramah_lingkungan']}")
            
            # Additional recommendations
            st.markdown("---")
            st.markdown("### 📋 Rekomendasi Tambahan")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### ⏰ Timeline Pengendalian")
                st.markdown("""
                1. **Minggu 1-2:** Identifikasi dan pemetaan gulma
                2. **Minggu 2-3:** Persiapan peralatan dan bahan
                3. **Minggu 3-4:** Eksekusi pengendalian
                4. **Minggu 4-6:** Monitoring dan evaluasi
                """)
            
            with col2:
                st.markdown("#### ⚠️ Hal yang Perlu Diperhatikan")
                st.warning("""
                - Gunakan APD (Alat Pelindung Diri) jika menggunakan herbisida
                - Perhatikan cuaca untuk aplikasi yang optimal
                - Lakukan monitoring berkala setelah pengendalian
                - Siapkan rencana tindak lanjut jika gulma muncul kembali
                """)
            
            # Export recommendation
            st.markdown("---")
            
            recommendation_text = f"""
REKOMENDASI PENGENDALIAN GULMA
==============================

Gulma: {recommendations['gulma']} ({recommendations['nama_ilmiah']})
Tingkat Bahaya: {recommendations['tingkat_bahaya']}/5
Status: {recommendations['prioritas']}

METODE PENGENDALIAN:
- Mekanis: {recommendations['metode_mekanis']}
- Biologis: {recommendations['metode_biologis']}
- Kultur Teknis: {recommendations['metode_kultur']}

HERBISIDA YANG DIREKOMENDASIKAN:
{chr(10).join([f"- {h['nama']} ({h['dosis']})" for h in recommendations['herbisida']])}

Untuk informasi lebih detail, lihat di halaman Rekomendasi Pengendalian GULMAFY.
            """
            
            st.download_button(
                label="📥 Download Rekomendasi",
                data=recommendation_text,
                file_name="rekomendasi_pengendalian.txt",
                mime="text/plain"
            )
        else:
            st.error(f"Gulma '{selected_gulma}' tidak ditemukan dalam database.")

# Help section
st.markdown("---")
st.markdown("### ℹ️ Panduan Pemilihan Metode")

with st.expander("Bagaimana memilih metode pengendalian yang tepat?"):
    st.markdown("""
    **Pertimbangan Utama:**
    
    1. **Tingkat Serangan:**
       - Ringan (1-2): Metode manual atau biologis bisa efektif
       - Sedang (3): Kombinasi metode disarankan
       - Berat (4-5): Herbisida mungkin diperlukan
    
    2. **Luas Lahan:**
       - Kecil (< 1 ha): Manual atau mekanis efisien
       - Sedang (1-5 ha): Kombinasi metode optimal
       - Besar (> 5 ha): Mekanis/kimia untuk efisiensi
    
    3. **Jenis Tanaman:**
       - Padi: Anilofos, 2,4-D efektif
       - Jagung: Pendimethalin pre-tanam
       - Sayuran: Metode manual lebih aman
    
    4. **Sumber Daya:**
       - Tenaga kerja: Metode manual
       - Modal: Herbisida
       - Ekosistem: Biologis/kultur teknis
    """)

st.markdown("---")
create_footer()
