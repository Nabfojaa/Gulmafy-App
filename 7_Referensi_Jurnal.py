"""
Page 7: Referensi & Jurnal - GULMAFY Application
"""
import streamlit as st
import pandas as pd
from utils.styling import apply_custom_css, create_footer
from utils.database_utils import load_jurnal_database

# Configure page
st.set_page_config(
    page_title="Referensi & Jurnal - GULMAFY",
    page_icon="📖",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

st.title("📖 Referensi & Jurnal Ilmiah")
st.markdown("Akses ke jurnal dan publikasi ilmiah tentang gulma Indonesia")
st.markdown("---")

jurnal = load_jurnal_database()

# Filter section
st.markdown("### 🔍 Filter & Pencarian")

col1, col2, col3 = st.columns(3)

with col1:
    search_query = st.text_input(
        "🔎 Cari jurnal"
    )

with col2:
    categories = sorted(set(j.get("kategori", "Umum") for j in jurnal))
    selected_category = st.selectbox(
        "Kategori",
        ["Semua"] + categories
    )

with col3:
    year_filter = st.slider(
        "Tahun",
        min_value=min(j.get("tahun", 2020) for j in jurnal) if jurnal else 2020,
        max_value=max(j.get("tahun", 2024) for j in jurnal) if jurnal else 2024,
        value=(2018, 2024)
    )

# Apply filters
filtered_jurnal = jurnal.copy()

if search_query:
    search_lower = search_query.lower()
    filtered_jurnal = [
        j for j in filtered_jurnal
        if (search_lower in j.get("judul", "").lower() or
            search_lower in j.get("penulis", "").lower() or
            search_lower in j.get("abstrak", "").lower())
    ]

if selected_category != "Semua":
    filtered_jurnal = [j for j in filtered_jurnal if j.get("kategori", "Umum") == selected_category]

filtered_jurnal = [
    j for j in filtered_jurnal
    if year_filter[0] <= j.get("tahun", 2020) <= year_filter[1]
]

st.markdown(f"**Menemukan {len(filtered_jurnal)} jurnal**")
st.markdown("---")

# Display journals
if filtered_jurnal:
    for idx, journal in enumerate(filtered_jurnal, 1):
        with st.expander(
            f"**{idx}. {journal.get('judul', 'Untitled')}** - {journal.get('tahun', 'N/A')} ({journal.get('kategori', 'Umum')})"
        ):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {journal.get('judul', 'Untitled')}")
                
                st.markdown(f"**Penulis:** {journal.get('penulis', 'N/A')}")
                st.markdown(f"**Tahun:** {journal.get('tahun', 'N/A')}")
                st.markdown(f"**Sumber:** {journal.get('sumber', 'N/A')}")
                st.markdown(f"**Institusi:** {journal.get('institusi', 'N/A')}")
                st.markdown(f"**Kategori:** `{journal.get('kategori', 'Umum')}`")
                
                st.markdown("#### 📝 Abstrak")
                st.info(journal.get('abstrak', 'Abstrak tidak tersedia'))
            
            with col2:
                st.markdown("#### 🔗 Akses")
                
                if journal.get('url'):
                    st.markdown(f"[🌐 Buka Jurnal]({journal.get('url')})")
                    st.markdown(
                        f"""
                    <a href="{journal.get('url')}" target="_blank" class="stButton stDownloadButton">
                        <button>📥 Download PDF</button>
                    </a>
                    """,
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("URL tidak tersedia")
            
            # Additional info
            st.markdown("---")
            st.markdown("#### ℹ️ Informasi Tambahan")
            
            additional_info = {
                "DOI": journal.get("doi", "N/A"),
                "Volume": journal.get("volume", "N/A"),
                "Issue": journal.get("issue", "N/A"),
                "Pages": journal.get("pages", "N/A")
            }
            
            for key, value in additional_info.items():
                if value != "N/A":
                    st.markdown(f"- **{key}:** {value}")
else:
    st.warning("Tidak ada jurnal yang sesuai dengan filter Anda.")

# Statistics
st.markdown("---")
st.markdown("### 📊 Statistik Jurnal")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Total Jurnal", len(jurnal))

with col2:
    st.metric("📂 Total Kategori", len(set(j.get("kategori", "Umum") for j in jurnal)))

with col3:
    st.metric("📆 Tahun Terawal", min(j.get("tahun", 2020) for j in jurnal) if jurnal else "N/A")

with col4:
    st.metric("📆 Tahun Terbaru", max(j.get("tahun", 2020) for j in jurnal) if jurnal else "N/A")

# Category distribution
st.markdown("---")
st.markdown("### 📂 Distribusi Jurnal Berdasarkan Kategori")

category_counts = {}
for j in jurnal:
    cat = j.get("kategori", "Umum")
    category_counts[cat] = category_counts.get(cat, 0) + 1

cat_df = pd.DataFrame(
    list(category_counts.items()),
    columns=["Kategori", "Jumlah"]
).sort_values("Jumlah", ascending=False)

import plotly.express as px

fig = px.bar(
    cat_df,
    x="Kategori",
    y="Jumlah",
    title="Distribusi Jurnal Berdasarkan Kategori",
    color="Jumlah",
    color_continuous_scale="Blues"
)
st.plotly_chart(fig, width='stretch')

# References from specific sources
st.markdown("---")
st.markdown("### 🎓 Institusi Penerbit")

institution_counts = {}
for j in jurnal:
    inst = j.get("institusi", "N/A")
    institution_counts[inst] = institution_counts.get(inst, 0) + 1

inst_df = pd.DataFrame(
    list(institution_counts.items()),
    columns=["Institusi", "Jumlah"]
).sort_values("Jumlah", ascending=False)

for idx, row in inst_df.iterrows():
    st.markdown(f"- **{row['Institusi']}**: {row['Jumlah']} publikasi")

# How to cite
st.markdown("---")
st.markdown("### 📎 Cara Mengutip Jurnal")

with st.expander("Panduan Format Citation"):
    st.markdown("""
    **Format APA:**
    
    ```
    Penulis, T. (Tahun). Judul artikel. Nama Jurnal, Volume(Issue), Halaman.
    ```
    
    **Contoh:**
    
    ```
    Soetomo dan Koesrianto. (2019). Strategi Pengendalian Gulma Terpadu 
    di Lahan Pertanian Indonesia. Jurnal Agronomi IPB, 45(2), 120-135.
    ```
    
    **Format Chicago:**
    
    ```
    Penulis, T. "Judul Artikel." Nama Jurnal Volume, no. Issue (Tahun): pages.
    ```
    
    **Format Harvard:**
    
    ```
    Penulis, T. Tahun. Judul artikel. Nama Jurnal. Volume(Issue). pp.pages.
    ```
    """)

# Help section
st.markdown("---")
st.markdown("### ℹ️ Informasi Tambahan")

with st.expander("Bagaimana cara mengakses jurnal penuh?"):
    st.markdown("""
    **Metode Akses Jurnal:**
    
    1. **Direct Access:**
       - Klik tombol "Buka Jurnal" untuk akses langsung
       - Beberapa jurnal dapat diunduh langsung
    
    2. **Melalui Institusi:**
       - Gunakan akses institusi Anda (IPB, BRIN, Universitas, dll)
       - Login dengan akun institusional
    
    3. **ResearchGate:**
       - Cari penulis di ResearchGate
       - Minta PDF langsung dari penulis
    
    4. **Google Scholar:**
       - Cari jurnal di Google Scholar
       - Lihat link alternatif untuk akses
    
    5. **Kontak Penulis:**
       - Email langsung ke penulis untuk meminta PDF
       - Biasanya penulis bersedia berbagi
    """)

st.info("""
📚 **GULMAFY Database Jurnal** menyediakan akses ke publikasi ilmiah terkait gulma Indonesia 
dari institusi terkemuka seperti IPB, BRIN, Universitas Hasanuddin, dan lainnya.
""")

st.markdown("---")
create_footer()
