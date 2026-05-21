"""
Page 3: Database Gulma - GULMAFY Application
"""
import streamlit as st
import pandas as pd
from utils.styling import apply_custom_css, create_footer, format_scientific_name
from utils.image_utils import display_weed_image
from utils.database_utils import (
    load_gulma_database,
    get_all_famili,
    get_all_habitat,
    get_gulma_by_famili,
    get_gulma_by_habitat,
    search_gulma
)

# Configure page
st.set_page_config(
    page_title="Database Gulma - GULMAFY",
    page_icon="📚",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

st.title("📚 Database Gulma Indonesia")
st.markdown("Informasi lengkap tentang gulma yang ditemukan di Indonesia")
st.markdown("---")

database = load_gulma_database()

# Search and filter section
st.markdown("### 🔍 Pencarian & Filter")

col1, col2, col3 = st.columns(3)

with col1:
    search_query = st.text_input("🔎 Cari gulma (nama atau nama ilmiah)")

with col2:
    filter_famili = st.selectbox(
        "Pilih Famili",
        ["Semua"] + get_all_famili(database)
    )

with col3:
    filter_habitat = st.selectbox(
        "Pilih Habitat",
        ["Semua"] + get_all_habitat(database)
    )

# Apply filters
filtered_data = database

if search_query:
    filtered_data = search_gulma(search_query, filtered_data)

if filter_famili != "Semua":
    filtered_data = get_gulma_by_famili(filter_famili, filtered_data)

if filter_habitat != "Semua":
    filtered_data = get_gulma_by_habitat(filter_habitat, filtered_data)

st.markdown(f"**Menemukan {len(filtered_data)} gulma**")
st.markdown("---")

# Display gulma in tabs by name
if filtered_data:
    # Create tabs
    tab_names = [weed["nama"] for weed in filtered_data]
    tabs = st.tabs(tab_names)
    
    for idx, weed in enumerate(filtered_data):
        with tabs[idx]:
            col1, col2 = st.columns([1, 1])
            
            # Danger level mapping
            danger_color = {
                1: "🟢",
                2: "🟢",
                3: "🟡",
                4: "🟠",
                5: "🔴"
            }
            
            # Left column - Basic info
            with col1:
                st.markdown(f"## {weed['nama']}")
                st.markdown(f"### {format_scientific_name(weed['nama_ilmiah'])}", unsafe_allow_html=True)
                
                st.markdown("#### ℹ️ Informasi Dasar")
                st.markdown(f"- **Famili:** {weed['famili']}")
                st.markdown(f"- **Tingkat Bahaya:** {'⭐' * weed['tingkat_bahaya']} ({weed['tingkat_bahaya']}/5)")
                st.markdown(f"- **Habitat:** {', '.join(weed['habitat'])}")
                
                st.markdown("#### 🌿 Ciri Khas")
                for ciri in weed["ciri_khas"]:
                    st.markdown(f"✓ {ciri}")
            
            # Right column - Image and danger level
            with col2:
                # Display weed image
                image_displayed = display_weed_image(weed['nama'], width="stretch")
                if not image_displayed:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #E8F8EE 0%, #D1EDDF 100%);
                                padding: 48px 16px;
                                text-align: center;
                                border-radius: 16px;
                                box-shadow: 0 4px 12px rgba(27, 67, 50, 0.08);">
                        <p style="font-size: 3em; margin: 0;">🌿</p>
                        <p style="color: #666; margin: 12px 0 0 0; font-size: 0.9em;">Gambar belum tersedia</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("")
                st.markdown("### Tingkat Bahaya")
                st.markdown(f"### {danger_color.get(weed['tingkat_bahaya'], '⚪')} Level {weed['tingkat_bahaya']}/5")
                
                danger_text = {
                    1: "Sangat Rendah - Tidak berbahaya",
                    2: "Rendah - Mudah dikendalikan",
                    3: "Sedang - Perlu perhatian",
                    4: "Tinggi - Pengendalian penting",
                    5: "Sangat Tinggi - Urgent!"
                }
                st.markdown(f"_{danger_text.get(weed['tingkat_bahaya'], 'N/A')}_")
            
            st.markdown("---")
            
            # Detailed tabs
            detail_tab1, detail_tab2, detail_tab3, detail_tab4, detail_tab5 = st.tabs([
                "Morfologi",
                "Dampak & Manfaat",
                "Pengendalian",
                "Herbisida",
                "Referensi"
            ])
            
            with detail_tab1:
                st.markdown("### 🌿 Deskripsi Morfologi")
                
                for key, value in weed["morfologi"].items():
                    st.markdown(f"**{key.capitalize()}:** {value}")
            
            with detail_tab2:
                st.markdown("### 📊 Dampak & Manfaat")
                
                st.markdown("#### Dampak Negatif")
                st.error(weed["dampak"])
                
                if weed.get("manfaat"):
                    st.markdown("#### Manfaat Positif")
                    st.success(weed["manfaat"])
                else:
                    st.info("Tidak ada manfaat khusus yang dicatat untuk gulma ini.")
            
            with detail_tab3:
                st.markdown("### 🛡️ Metode Pengendalian")
                
                # Mechanical control
                st.markdown("#### 🔧 Pengendalian Mekanis")
                st.info(weed["pengendalian_mekanis"])
                
                # Biological control
                st.markdown("#### 🦋 Pengendalian Biologis")
                st.info(weed["pengendalian_biologis"])
                
                # Cultural control
                st.markdown("#### 🌾 Pengendalian Kultur Teknis")
                st.info(weed["pengendalian_kultur_teknis"])
            
            with detail_tab4:
                st.markdown("### 💊 Rekomendasi Herbisida")
                
                st.markdown("#### Herbisida yang Efektif:")
                for herb in weed["herbisida"]:
                    st.markdown(f"- {herb}")
                
                st.markdown("#### Dosis Aplikasi:")
                st.info(weed["dosis_herbisida"])
                
                st.markdown("#### Waktu Aplikasi:")
                st.warning(weed["waktu_aplikasi"])
            
            with detail_tab5:
                st.markdown("### 📚 Referensi & Sumber Ilmiah")
                
                st.markdown("#### Jurnal Terkait:")
                for ref in weed.get("referensi_jurnal", []):
                    st.markdown(f"- {ref}")
                
                st.markdown("#### Sumber Ilmiah:")
                st.markdown(f"**{weed.get('sumber_ilmiah', 'N/A')}**")
                
                if weed.get("url_referensi"):
                    st.markdown(f"**URL:** {weed['url_referensi']}")
else:
    st.warning("Tidak ada gulma yang sesuai dengan filter yang Anda pilih.")

# Database info
st.markdown("---")
st.markdown("### 📊 Statistik Database")

famili_unique = len(set(weed["famili"] for weed in database))
habitat_unique = len(set(h for weed in database for h in weed["habitat"]))
dangerous_count = len([w for w in database if w["tingkat_bahaya"] >= 4])

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Gulma", len(database))
with col2:
    st.metric("Famili Unik", famili_unique)
with col3:
    st.metric("Habitat Unik", habitat_unique)
with col4:
    st.metric("Gulma Berbahaya", dangerous_count)

# Export option
st.markdown("---")
st.markdown("### 📥 Export Data")

export_format = st.selectbox(
    "Pilih format export",
    ["CSV", "JSON"]
)

if export_format == "CSV":
    csv_data = pd.DataFrame([
        {
            "Nama": w["nama"],
            "Nama Ilmiah": w["nama_ilmiah"],
            "Famili": w["famili"],
            "Tingkat Bahaya": w["tingkat_bahaya"],
            "Habitat": ", ".join(w["habitat"]),
            "Dampak": w["dampak"]
        }
        for w in database
    ])
    st.download_button(
        label="📥 Download sebagai CSV",
        data=csv_data.to_csv(index=False),
        file_name="gulma_database.csv",
        mime="text/csv"
    )
else:
    import json
    json_data = json.dumps(database, ensure_ascii=False, indent=2)
    st.download_button(
        label="📥 Download sebagai JSON",
        data=json_data,
        file_name="gulma_database.json",
        mime="application/json"
    )

st.markdown("---")
create_footer()
