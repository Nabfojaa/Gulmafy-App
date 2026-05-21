"""
Page 1: Dashboard - GULMAFY Application
Premium Modern Dashboard with Advanced Analytics
"""
import streamlit as st
import streamlit.components.v1 as components
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
from utils.monitoring_utils import monitoring_system

# Configure page
st.set_page_config(
    page_title="Dashboard - GULMAFY",
    page_icon="📊",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

# Premium Header
st.markdown("""
<div style="background: linear-gradient(135deg, #1B4332 0%, #2D6A4F 50%, #52B788 100%);
            padding: 50px 30px;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 40px;
            box-shadow: 0 12px 32px rgba(27, 67, 50, 0.2);">
    <h1 style="color: white; margin: 0; font-size: 2.8em; font-weight: 800;">📊 Dashboard GULMAFY</h1>
    <p style="
    color: #FFFFFF;
    margin: 15px 0 0 0;
    font-size: 1.02em;
    font-weight: 700;
    letter-spacing: 0.2px;
    text-shadow:
        0 0 5px rgba(245,255,255,0.8),
        0 0 10px rgba(245,255,255,0.7),
        0 0 15px rgba(245,255,255,0.55),
        0 2px 10px rgba(0,0,0,0.25);
">
    Tampilan utama sistem pengetahuan gulma Indonesia dengan analytics real-time
</p>
""", unsafe_allow_html=True)

# Load data
database = load_gulma_database()
jurnal = load_jurnal_database()
stats = get_database_statistics()

# Key Metrics Row 1
st.markdown("### 📈 Metrik Database Utama")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "📋 Total Gulma",
        stats["total_gulma"],
        delta="spesies database",
        delta_color="off"
    )

with col2:
    st.metric(
        "🏷️ Famili",
        stats["total_famili"],
        delta="kelompok taksonomi",
        delta_color="off"
    )

with col3:
    st.metric(
        "🌍 Habitat",
        stats["total_habitat"],
        delta="tipe lingkungan",
        delta_color="off"
    )

with col4:
    st.metric(
        "📚 Referensi",
        stats["total_jurnal"],
        delta="artikel ilmiah",
        delta_color="off"
    )

with col5:
    st.metric(
        "⚠️ Berbahaya",
        stats["dangerous_count"],
        delta="tingkat ≥4",
        delta_color="off"
    )

# Monitoring Statistics
st.markdown("---")
st.markdown("### 📊 Statistik Monitoring Lapangan")

monitoring_stats = monitoring_system.get_statistics()
mcol1, mcol2, mcol3, mcol4 = st.columns(4)

with mcol1:
    st.metric(
        "📍 Lokasi Monitoring",
        monitoring_stats["total_locations"],
        delta="lokasi",
        delta_color="off"
    )

with mcol2:
    st.metric(
        "🎯 Jumlah Record",
        monitoring_stats["total_records"],
        delta="pengamatan",
        delta_color="off"
    )

with mcol3:
    st.metric(
        "📊 Rata-rata Serangan",
        f"{monitoring_stats['average_attack']}/5",
        delta="tingkat",
        delta_color="off"
    )

with mcol4:
    st.metric(
        "🌿 Gulma Dominan",
        monitoring_stats["most_recorded_weed"] if monitoring_stats["most_recorded_weed"] != "N/A" else "Belum ada",
        delta=f"{monitoring_stats['most_recorded_count']} record" if monitoring_stats["most_recorded_weed"] != "N/A" else "Tambah data monitoring",
        delta_color="off"
    )

# Charts Section
st.markdown("---")
st.markdown("### 📊 Visualisasi Data & Analytics")

# Row 1: Danger Level & Habitat
col1, col2 = st.columns(2)

# Chart 1: Danger Level Distribution
with col1:
    danger_counts = {}
    for weed in database:
        level = weed["tingkat_bahaya"]
        danger_counts[level] = danger_counts.get(level, 0) + 1
    
    danger_df = pd.DataFrame(
        list(danger_counts.items()),
        columns=["Tingkat Bahaya", "Jumlah Gulma"]
    ).sort_values("Tingkat Bahaya")
    
    danger_df["Label"] = danger_df["Tingkat Bahaya"].apply(
        lambda x: f"Tingkat {x}"
    )
    
    colors_danger = ["#2D6A4F", "#52B788", "#F59E0B", "#F97316", "#DC2626"]
    
    fig1 = go.Figure(data=[
        go.Bar(
            x=danger_df["Label"],
            y=danger_df["Jumlah Gulma"],
            marker=dict(color=danger_df["Tingkat Bahaya"], colorscale="Reds"),
            text=danger_df["Jumlah Gulma"],
            textposition="auto",
        )
    ])
    
    fig1.update_layout(
        title="Distribusi Gulma Berdasarkan Tingkat Bahaya",
        xaxis_title="Tingkat Bahaya",
        yaxis_title="Jumlah Gulma",
        hovermode="x unified",
        template="plotly_white"
    )
    st.plotly_chart(fig1, width='stretch')

# Chart 2: Habitat Distribution
with col2:
    habitat_counts = {}
    for weed in database:
        for habitat in (weed["habitat"] if isinstance(weed["habitat"], list) else [weed["habitat"]]):
            habitat_counts[habitat] = habitat_counts.get(habitat, 0) + 1
    
    habitat_df = pd.DataFrame(
        list(habitat_counts.items()),
        columns=["Habitat", "Jumlah Gulma"]
    ).sort_values("Jumlah Gulma", ascending=True)
    
    fig2 = go.Figure(data=[
        go.Bar(
            y=habitat_df["Habitat"],
            x=habitat_df["Jumlah Gulma"],
            orientation="h",
            marker=dict(color=habitat_df["Jumlah Gulma"], colorscale="Greens"),
            text=habitat_df["Jumlah Gulma"],
            textposition="auto",
        )
    ])
    
    fig2.update_layout(
        title="Distribusi Gulma Berdasarkan Habitat",
        xaxis_title="Jumlah Gulma",
        yaxis_title="Habitat",
        hovermode="y unified",
        template="plotly_white"
    )
    st.plotly_chart(fig2, width='stretch')

# Row 2: Family & Top Dangerous
col1, col2 = st.columns(2)

# Chart 3: Family Distribution (Pie)
with col1:
    famili_counts = {}
    for weed in database:
        famili = weed["famili"]
        famili_counts[famili] = famili_counts.get(famili, 0) + 1
    
    famili_df = pd.DataFrame(
        list(famili_counts.items()),
        columns=["Famili", "Jumlah Gulma"]
    ).sort_values("Jumlah Gulma", ascending=False)
    
    fig3 = go.Figure(data=[
        go.Pie(
            labels=famili_df["Famili"],
            values=famili_df["Jumlah Gulma"],
            marker=dict(colors=px.colors.sequential.Greens[::-1]),
            hoverinfo="label+value+percent"
        )
    ])
    
    fig3.update_layout(
        title="Distribusi Gulma Berdasarkan Famili",
        template="plotly_white"
    )
    st.plotly_chart(fig3, width='stretch')

# Chart 4: Top 5 Most Dangerous
with col2:
    top_dangerous = get_most_dangerous_gulma(5, database)
    
    if top_dangerous:
        dangerous_df = pd.DataFrame([
            {
                "Nama": weed["nama"],
                "Tingkat Bahaya": weed["tingkat_bahaya"]
            }
            for weed in top_dangerous
        ])
        
        fig4 = go.Figure(data=[
            go.Bar(
                y=dangerous_df["Nama"],
                x=dangerous_df["Tingkat Bahaya"],
                orientation="h",
                marker=dict(color=dangerous_df["Tingkat Bahaya"], colorscale="Reds"),
                text=dangerous_df["Tingkat Bahaya"],
                textposition="auto",
            )
        ])
        
        fig4.update_layout(
            title="Top 5 Gulma Paling Berbahaya",
            xaxis_title="Tingkat Bahaya",
            yaxis_title="Nama Gulma",
            xaxis=dict(range=[0, 5]),
            hovermode="y unified",
            template="plotly_white"
        )
        st.plotly_chart(fig4, width='stretch')

# Most Dangerous Weeds Table
st.markdown("---")
st.markdown("### ⚠️ Gulma 5 Paling Berbahaya")

top_5 = get_most_dangerous_gulma(5, database)

# Create HTML table for better scientific name rendering
html_table = """
<style>
    .danger-table { width: 100%; border-collapse: collapse; }
    .danger-table th { background: #1B4332; color: white; padding: 12px; text-align: left; font-weight: 600; border: 1px solid #2D6A4F; }
    .danger-table td { padding: 12px; border: 1px solid #D1EDDF; }
    .danger-table tr:hover { background: #F4FFF8; }
    .danger-table tr:nth-child(even) { background: #FAFBFA; }
    .danger-table .num { text-align: center; font-weight: 600; color: #1B4332; }
    .danger-table .danger-level { text-align: center; }
</style>
<table class="danger-table">
    <tr>
        <th>No</th>
        <th>Nama Gulma</th>
        <th>Nama Ilmiah</th>
        <th>Tingkat</th>
        <th>Famili</th>
    </tr>
"""

for idx, weed in enumerate(top_5, 1):
    danger_level = weed["tingkat_bahaya"]
    if danger_level == 5:
        danger_badge = "🔴 Sangat Tinggi"
    elif danger_level == 4:
        danger_badge = "🟠 Tinggi"
    else:
        danger_badge = "🟡 Sedang"
    
    scientific_name_html = format_scientific_name(weed['nama_ilmiah'])
    
    html_table += f"""
    <tr>
        <td class="num">{idx}</td>
        <td><strong>{weed["nama"]}</strong></td>
        <td>{scientific_name_html}</td>
        <td class="danger-level">{danger_badge}</td>
        <td>{weed["famili"]}</td>
    </tr>
"""

html_table += "</table>"

components.html(html_table, height=320, scrolling=True)

# Reference Statistics
st.markdown("---")
st.markdown("### 📚 Statistik Referensi Jurnal")

if jurnal:
    # Count by category
    category_counts = {}
    for j in jurnal:
        cat = j.get("kategori", "Umum")
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    cat_df = pd.DataFrame(
        list(category_counts.items()),
        columns=["Kategori", "Jumlah Artikel"]
    ).sort_values("Jumlah Artikel", ascending=False)
    
    fig_cat = go.Figure(data=[
        go.Bar(
            x=cat_df["Kategori"],
            y=cat_df["Jumlah Artikel"],
            marker=dict(color=cat_df["Jumlah Artikel"], colorscale="Blues"),
            text=cat_df["Jumlah Artikel"],
            textposition="auto",
        )
    ])
    
    fig_cat.update_layout(
        title="Distribusi Jurnal Berdasarkan Kategori",
        xaxis_title="Kategori",
        yaxis_title="Jumlah Artikel",
        template="plotly_white"
    )
    st.plotly_chart(fig_cat, width='stretch')

# Summary Info
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(116, 198, 157, 0.1) 0%, rgba(212, 243, 220, 0.1) 100%);
            border-radius: 16px;
            padding: 24px;
            border-left: 4px solid #52B788;">
    <h3 style="margin-top: 0; color: #1B4332;">📊 Informasi Dashboard</h3>
    <ul style="color: #333; line-height: 1.8;">
        <li><strong>Real-time Data:</strong> Semua data diperbarui secara real-time dari database GULMAFY</li>
        <li><strong>Monitoring Integration:</strong> Statistik monitoring terintegrasi dari pengamatan lapangan</li>
        <li><strong>Advanced Analytics:</strong> Visualisasi data dengan Plotly untuk analisis mendalam</li>
        <li><strong>Navigation:</strong> Gunakan menu di sidebar untuk mengakses fitur-fitur lainnya</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
create_footer()

