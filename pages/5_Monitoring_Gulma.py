"""
Page 5: Monitoring Gulma - GULMAFY Application
Advanced Weed Monitoring Dashboard
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from utils.styling import apply_custom_css, create_footer
from utils.monitoring_utils import monitoring_system
from utils.database_utils import load_gulma_database, get_all_gulma_names

# Configure page
st.set_page_config(
    page_title="Monitoring Gulma - GULMAFY",
    page_icon="📊",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

st.markdown("""
<div style="background: linear-gradient(135deg, #1B4332 0%, #2D6A4F 50%, #52B788 100%);
            padding: 40px 30px;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 40px;
            box-shadow: 0 12px 32px rgba(27, 67, 50, 0.2);">
    <h1 style="color: white; margin: 0; font-size: 2.5em; font-weight: 800;">📊 Monitoring Gulma</h1>
    <p style="
    color: #FFFFFF;
    margin: 15px 0 0 0;
    font-size: 1em;
    font-weight: 700;
    text-shadow:
        0 0 5px rgba(245,255,255,0.8),
        0 0 10px rgba(245,255,255,0.7),
        0 0 15px rgba(245,255,255,0.55),
        0 2px 10px rgba(0,0,0,0.25);
">
    Track perkembangan gulma di lapangan Anda dengan sistem monitoring real-time
</p>
</div>
""", unsafe_allow_html=True)

# Tab selection
tab1, tab2, tab3 = st.tabs(["➕ Input Data Baru", "📋 Lihat Data", "📊 Analisis"])

with tab1:
    st.markdown("### ➕ Tambah Data Monitoring Baru")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Location input
        lokasi = st.text_input(
            "📍 Lokasi Pengamatan",
            placeholder="Contoh: Sawah Bogor, Jawa Barat"
        )
        
        # Weed type input
        gulma_options = [""] + get_all_gulma_names(load_gulma_database())
        gulma = st.selectbox(
            "🌿 Jenis Gulma",
            gulma_options
        )
        
        if gulma == "":
            gulma_custom = st.text_input(
                "Atau masukkan jenis gulma lainnya:",
                placeholder="Tuliskan jenis gulma yang tidak ada di list"
            )
            if gulma_custom:
                gulma = gulma_custom
    
    with col2:
        # Attack level
        tingkat_serangan = st.slider(
            "📊 Tingkat Serangan",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Ringan, 5 = Sangat Berat"
        )
        
        # Date
        tanggal = st.date_input(
            "📅 Tanggal Pengamatan",
            value=datetime.now()
        )
    
    # Notes
    catatan = st.text_area(
        "📝 Catatan Tambahan",
        placeholder="Kondisi lahan, cuaca, tindakan yang sudah dilakukan, dll...",
        height=100
    )
    
    # Submit button
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("✅ Simpan Data", width='stretch', type="primary"):
            if not lokasi or not gulma:
                st.error("⚠️ Lokasi dan jenis gulma harus diisi!")
            else:
                # Prepare data
                new_data = {
                    "location": lokasi,
                    "gulma": gulma,
                    "tingkat_serangan": tingkat_serangan,
                    "tanggal": tanggal.strftime("%Y-%m-%d"),
                    "catatan": catatan
                }
                
                # Create DataFrame
                new_df = pd.DataFrame([new_data])
                
                # Add to monitoring system
                monitoring_system.data = pd.concat(
                    [monitoring_system.data, new_df],
                    ignore_index=True
                )
                
                # Save to file
                if monitoring_system.save_monitoring_data(monitoring_system.data):
                    st.success("✅ Data berhasil disimpan!")
                    st.balloons()
                else:
                    st.error("❌ Gagal menyimpan data!")

with tab2:
    st.markdown("### 📋 Data Monitoring")
    
    # Get current data
    monitoring_data = monitoring_system.get_records()
    
    if not monitoring_data.empty:
        # Filter section
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_lokasi = st.text_input(
                "🔍 Filter Lokasi"
            )
        
        with col2:
            filter_gulma = st.text_input(
                "🔍 Filter Gulma"
            )
        
        with col3:
            filter_bulan = st.selectbox(
                "🔍 Filter Bulan",
                ["Semua"] + [f"{i:02d}" for i in range(1, 13)]
            )
        
        # Apply filters
        filtered_data = monitoring_data.copy()
        
        if filter_lokasi:
            filtered_data = filtered_data[
                filtered_data["location"].str.contains(filter_lokasi, case=False, na=False)
            ]
        
        if filter_gulma:
            filtered_data = filtered_data[
                filtered_data["gulma"].str.contains(filter_gulma, case=False, na=False)
            ]
        
        if filter_bulan != "Semua":
            tanggal_parsed = pd.to_datetime(filtered_data["tanggal"], errors="coerce")
            filtered_data = filtered_data[
                tanggal_parsed.dt.strftime("%m") == filter_bulan
            ]
        
        # Display data
        st.markdown(f"**Total: {len(filtered_data)} record**")
        
        # Display as cards with edit/delete buttons
        for original_idx, row in filtered_data.iterrows():
            danger_level = row['tingkat_serangan']
            if danger_level == 1 or danger_level == 2:
                danger_color = "#2563EB"
                danger_emoji = "🟢"
            elif danger_level == 3:
                danger_color = "#fbc02d"
                danger_emoji = "🟡"
            else:
                danger_color = "#d32f2f"
                danger_emoji = "🔴"
            
            col_card, col_actions = st.columns([0.92, 0.08])
            
            with col_card:
                st.markdown(f"""
                <div style="background: white; border-left: 4px solid {danger_color}; padding: 16px; margin: 12px 0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <div style="display: flex; gap: 24px; align-items: center;">
                        <div>
                            <p style="margin: 0 0 8px 0; font-weight: 700; color: #1B4332; font-size: 1.1em;">{danger_emoji} {row['location']} - {row['gulma']}</p>
                            <p style="margin: 0; color: #666; font-size: 0.9em;">📅 {row['tanggal']} | Tingkat: {danger_level}/5</p>
                            {f'<p style="margin: 8px 0 0 0; color: #333; font-size: 0.9em;">💬 {row["catatan"]}</p>' if pd.notna(row['catatan']) and row['catatan'] != "" else ''}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_actions:
                col_edit, col_delete = st.columns(2, gap="small")
                
                with col_edit:
                    if st.button("✏️", key=f"edit_{original_idx}", help="Edit catatan"):
                        st.session_state[f"edit_mode_{original_idx}"] = True
                
                with col_delete:
                    if st.button("🗑️", key=f"delete_{original_idx}", help="Hapus record"):
                        if monitoring_system.delete_record(original_idx):
                            st.success("✅ Data berhasil dihapus!")
                            st.rerun()
                        else:
                            st.error("❌ Gagal menghapus data!")
            
            # Edit mode
            if st.session_state.get(f"edit_mode_{original_idx}", False):
                st.markdown("#### ✏️ Edit Catatan")
                
                new_catatan = st.text_area(
                    f"Edit catatan untuk {row['location']} - {row['gulma']}:",
                    value=row['catatan'] if pd.notna(row['catatan']) else "",
                    key=f"catatan_input_{original_idx}",
                    height=80
                )
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("💾 Simpan Perubahan", key=f"save_edit_{original_idx}"):
                        if monitoring_system.update_record(
                            original_idx,
                            catatan=new_catatan
                        ):
                            st.success("✅ Catatan berhasil diperbarui!")
                            st.session_state[f"edit_mode_{original_idx}"] = False
                            st.rerun()
                        else:
                            st.error("❌ Gagal memperbarui catatan!")
                
                with col2:
                    if st.button("❌ Batal", key=f"cancel_edit_{original_idx}"):
                        st.session_state[f"edit_mode_{original_idx}"] = False
                        st.rerun()
                
                st.markdown("---")
        
        # Export option
        st.markdown("---")
        st.markdown("### 📥 Export Data")
        
        col1, col2 = st.columns(2)
        
        with col1:
            csv_data = filtered_data.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv_data,
                file_name="monitoring_data.csv",
                mime="text/csv"
            )
        
        with col2:
            import json
            json_data = filtered_data.to_json(orient="records", indent=2)
            st.download_button(
                label="📥 Download JSON",
                data=json_data,
                file_name="monitoring_data.json",
                mime="application/json"
            )
    else:
        st.info("📭 Belum ada data monitoring. Mulai dengan menambahkan data baru di tab 'Input Data Baru'.")

with tab3:
    st.markdown("### 📊 Analisis & Statistik")
    
    monitoring_data = monitoring_system.data
    
    if not monitoring_data.empty:
        # Overall statistics
        stats = monitoring_system.get_statistics()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📍 Total Lokasi", stats["total_locations"], delta="lokasi", delta_color="off")
        
        with col2:
            st.metric("🌿 Total Gulma", stats["total_weeds"], delta="spesies", delta_color="off")
        
        with col3:
            st.metric("📊 Rata-rata Serangan", f"{stats['average_attack']}/5", delta="tingkat", delta_color="off")
        
        with col4:
            st.metric("📋 Total Record", stats["total_records"], delta="pengamatan", delta_color="off")
        
        st.markdown("---")
        
        # Trends Chart
        trends = monitoring_system.get_trends()
        if not trends.empty:
            st.markdown("#### 📈 Tren Monitoring Seiring Waktu")
            
            fig_trend = go.Figure()
            
            fig_trend.add_trace(go.Scatter(
                x=trends.index,
                y=trends['mean'],
                mode='lines+markers',
                name='Rata-rata Serangan',
                line=dict(color='#52B788', width=3),
                marker=dict(size=8)
            ))
            
            fig_trend.add_trace(go.Scatter(
                x=trends.index,
                y=trends['max'],
                mode='lines',
                name='Maksimal Serangan',
                line=dict(color='#d32f2f', width=2, dash='dash'),
                marker=dict(size=6)
            ))
            
            fig_trend.update_layout(
                title="Tren Tingkat Serangan Gulma",
                xaxis_title="Tanggal",
                yaxis_title="Tingkat Serangan",
                hovermode="x unified",
                template="plotly_white"
            )
            
            st.plotly_chart(fig_trend, width='stretch')
        
        st.markdown("---")
        
        # Location statistics
        st.markdown("#### 📍 Statistik Berdasarkan Lokasi")
        
        loc_stats = monitoring_system.get_location_statistics()
        if not loc_stats.empty:
            st.dataframe(loc_stats, width='stretch')
        
        st.markdown("---")
        
        # Weed statistics
        st.markdown("#### 🌿 Statistik Berdasarkan Gulma")
        
        weed_stats = monitoring_system.get_weed_statistics()
        if not weed_stats.empty:
            st.dataframe(weed_stats, width='stretch')
    else:
        st.info("📭 Belum ada data monitoring untuk analisis. Mulai dengan menambahkan data monitoring di tab 'Input Data Baru'.")

st.markdown("---")
create_footer()
