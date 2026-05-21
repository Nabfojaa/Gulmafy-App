"""
Page 6: Statistik Gulma - GULMAFY Application
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.styling import apply_custom_css, create_footer
from utils.database_utils import load_gulma_database, get_all_famili
from utils.monitoring_utils import monitoring_system

# Configure page
st.set_page_config(
    page_title="Statistik Gulma - GULMAFY",
    page_icon="📈",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

st.title("📈 Statistik Gulma")
st.markdown("Visualisasi dan analisis data gulma di Indonesia")
st.markdown("---")

database = load_gulma_database()
monitoring_data = monitoring_system.data

# Tab selection
tab1, tab2, tab3, tab4 = st.tabs([
    "Database Gulma",
    "Monitoring",
    "Perbandingan",
    "Laporan"
])

with tab1:
    st.markdown("### 📊 Statistik Database Gulma")
    
    col1, col2 = st.columns(2)
    
    # Distribution by danger level
    with col1:
        danger_counts = {}
        for weed in database:
            level = weed["tingkat_bahaya"]
            danger_counts[level] = danger_counts.get(level, 0) + 1
        
        danger_df = pd.DataFrame(
            list(danger_counts.items()),
            columns=["Tingkat Bahaya", "Jumlah"]
        ).sort_values("Tingkat Bahaya")
        
        danger_df["Label"] = danger_df["Tingkat Bahaya"].apply(
            lambda x: f"Level {x}: {'⭐' * x}"
        )
        
        fig1 = px.bar(
            danger_df,
            x="Label",
            y="Jumlah",
            title="Distribusi Gulma Berdasarkan Tingkat Bahaya",
            color="Tingkat Bahaya",
            color_continuous_scale="Reds",
            labels={"Label": "Tingkat Bahaya", "Jumlah": "Jumlah Gulma"}
        )
        st.plotly_chart(fig1, width='stretch')
    
    # Distribution by family
    with col2:
        famili_counts = {}
        for weed in database:
            famili = weed["famili"]
            famili_counts[famili] = famili_counts.get(famili, 0) + 1
        
        famili_df = pd.DataFrame(
            list(famili_counts.items()),
            columns=["Famili", "Jumlah"]
        ).sort_values("Jumlah", ascending=False)
        
        fig2 = px.pie(
            famili_df,
            names="Famili",
            values="Jumlah",
            title="Distribusi Gulma Berdasarkan Famili",
            color_discrete_sequence=px.colors.sequential.Greens[::-1]
        )
        st.plotly_chart(fig2, width='stretch')
    
    col1, col2 = st.columns(2)
    
    # Habitat distribution
    with col1:
        habitat_counts = {}
        for weed in database:
            for habitat in weed["habitat"]:
                habitat_counts[habitat] = habitat_counts.get(habitat, 0) + 1
        
        habitat_df = pd.DataFrame(
            list(habitat_counts.items()),
            columns=["Habitat", "Jumlah"]
        ).sort_values("Jumlah", ascending=True)
        
        fig3 = px.bar(
            habitat_df,
            x="Jumlah",
            y="Habitat",
            orientation="h",
            title="Distribusi Gulma Berdasarkan Habitat",
            color="Jumlah",
            color_continuous_scale="Greens"
        )
        st.plotly_chart(fig3, width='stretch')
    
    # Danger level statistics
    with col2:
        st.markdown("### 📊 Statistik Tingkat Bahaya")
        
        danger_level_dist = {
            "🟢 Level 1-2 (Rendah)": len([w for w in database if w["tingkat_bahaya"] <= 2]),
            "🟡 Level 3 (Sedang)": len([w for w in database if w["tingkat_bahaya"] == 3]),
            "🟠 Level 4 (Tinggi)": len([w for w in database if w["tingkat_bahaya"] == 4]),
            "🔴 Level 5 (Sangat Tinggi)": len([w for w in database if w["tingkat_bahaya"] == 5])
        }
        
        for label, count in danger_level_dist.items():
            st.metric(label, count, delta=f"{count/len(database)*100:.1f}%")

with tab2:
    st.markdown("### 📊 Statistik Monitoring")
    
    if not monitoring_data.empty:
        stats = monitoring_system.get_statistics()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📍 Lokasi", stats["total_locations"])
        with col2:
            st.metric("🌿 Gulma", stats["total_weeds"])
        with col3:
            st.metric("📋 Record", stats["total_records"])
        with col4:
            st.metric("📊 Rata-rata", f"{stats['average_attack']}/5")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        # Location monitoring
        with col1:
            loc_stats = monitoring_system.get_location_statistics()
            if not loc_stats.empty:
                loc_stats_reset = loc_stats.reset_index()
                
                fig_loc = px.bar(
                    loc_stats_reset,
                    x="location",
                    y="Rata-rata",
                    title="Tingkat Serangan Rata-rata per Lokasi",
                    labels={"location": "Lokasi", "Rata-rata": "Tingkat Serangan Rata-rata"},
                    color="Rata-rata",
                    color_continuous_scale="RdYlGn_r"
                )
                st.plotly_chart(fig_loc, width='stretch')
        
        # Weed monitoring
        with col2:
            weed_stats = monitoring_system.get_weed_statistics()
            if not weed_stats.empty:
                weed_stats_reset = weed_stats.reset_index()
                
                fig_weed = px.bar(
                    weed_stats_reset.head(8),
                    x="gulma",
                    y="Rata-rata",
                    title="Top 8 Gulma Paling Sering Dipantau",
                    labels={"gulma": "Gulma", "Rata-rata": "Tingkat Serangan Rata-rata"},
                    color="Rata-rata",
                    color_continuous_scale="Reds"
                )
                st.plotly_chart(fig_weed, width='stretch')
    else:
        st.info("📭 Belum ada data monitoring.")

with tab3:
    st.markdown("### 🔄 Perbandingan Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Database vs Monitoring")
        
        db_stats = {
            "Database Gulma": len(database),
            "Gulma Monitoring": monitoring_system.get_statistics()["total_weeds"]
        }
        
        comp_df = pd.DataFrame(
            list(db_stats.items()),
            columns=["Kategori", "Jumlah"]
        )
        
        fig_comp = px.bar(
            comp_df,
            x="Kategori",
            y="Jumlah",
            title="Perbandingan Database vs Monitoring",
            color="Kategori",
            color_discrete_map={
                "Database Gulma": "#52B788",
                "Gulma Monitoring": "#d62828"
            }
        )
        st.plotly_chart(fig_comp, width='stretch')
    
    with col2:
        st.markdown("#### Tingkat Bahaya - Database vs Monitoring")
        
        if not monitoring_data.empty:
            monitoring_avg_danger = monitoring_data["tingkat_serangan"].mean()
            
            danger_comparison = pd.DataFrame({
                "Metrik": ["Database Rata-rata", "Monitoring Rata-rata"],
                "Nilai": [
                    sum(w["tingkat_bahaya"] for w in database) / len(database),
                    monitoring_avg_danger
                ]
            })
            
            fig_danger = px.bar(
                danger_comparison,
                x="Metrik",
                y="Nilai",
                title="Perbandingan Tingkat Bahaya Rata-rata",
                color="Metrik",
                color_discrete_map={
                    "Database Rata-rata": "#2D6A4F",
                    "Monitoring Rata-rata": "#d62828"
                },
                range_y=[0, 5]
            )
            st.plotly_chart(fig_danger, width='stretch')

with tab4:
    st.markdown("### 📄 Laporan Ringkasan")
    
    # Generate summary report
    db_stats = {
        "Total Gulma": len(database),
        "Total Famili": len(set(w["famili"] for w in database)),
        "Total Habitat": len(set(h for w in database for h in w["habitat"])),
        "Gulma Level 4-5": len([w for w in database if w["tingkat_bahaya"] >= 4]),
        "Gulma Level 1-2": len([w for w in database if w["tingkat_bahaya"] <= 2])
    }
    
    monitoring_stats = monitoring_system.get_statistics()
    
    report_data = []
    for key, value in db_stats.items():
        report_data.append({"Metrik": key, "Nilai": value})
    
    report_df = pd.DataFrame(report_data)
    
    st.markdown("#### 📊 Ringkasan Database")
    st.dataframe(report_df, width='stretch', hide_index=True)
    
    st.markdown("#### 📊 Ringkasan Monitoring")
    monitoring_report = pd.DataFrame({
        "Metrik": ["Total Lokasi", "Total Gulma Unik", "Total Record", "Rata-rata Serangan"],
        "Nilai": [
            monitoring_stats["total_locations"],
            monitoring_stats["total_weeds"],
            monitoring_stats["total_records"],
            f"{monitoring_stats['average_attack']}/5"
        ]
    })
    st.dataframe(monitoring_report, width='stretch', hide_index=True)
    
    # Export report
    st.markdown("---")
    st.markdown("#### 📥 Export Laporan")
    
    report_text = f"""
LAPORAN RINGKASAN GULMAFY
=========================
Tanggal: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

DATABASE GULMA:
- Total Gulma: {db_stats['Total Gulma']}
- Total Famili: {db_stats['Total Famili']}
- Total Habitat: {db_stats['Total Habitat']}
- Gulma Berbahaya (Level 4-5): {db_stats['Gulma Level 4-5']}
- Gulma Rendah (Level 1-2): {db_stats['Gulma Level 1-2']}

MONITORING:
- Total Lokasi: {monitoring_stats['total_locations']}
- Total Gulma Unik: {monitoring_stats['total_weeds']}
- Total Record: {monitoring_stats['total_records']}
- Rata-rata Tingkat Serangan: {monitoring_stats['average_attack']}/5
- Gulma Dominan: {monitoring_stats['most_recorded_weed']}

Laporan dibuat otomatis oleh GULMAFY System.
    """
    
    st.download_button(
        label="📥 Download Laporan",
        data=report_text,
        file_name=f"laporan_gulmafy_{pd.Timestamp.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )

st.markdown("---")
create_footer()
