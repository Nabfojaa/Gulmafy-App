"""
Page 2: Identifikasi Gulma - GULMAFY Application
Premium AI-Powered Weed Identification with RapidFuzz + Smart Recommendations + Google Lens Integration
"""
import streamlit as st
import pandas as pd
from utils.styling import apply_custom_css, create_confidence_bar, create_footer, format_scientific_name
from utils.expert_system import expert_system
from utils.database_utils import load_gulma_database
from utils.image_utils import display_weed_image, image_exists
from utils.ai_engine import similarity_ai, recommendation_engine, insight_generator
from utils.herbisida_db import get_herbisida_for_gulma, display_herbisida_card
import os
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="Identifikasi Gulma - GULMAFY",
    page_icon="🔍",
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
    <h1 style="color: white; margin: 0; font-size: 2.5em; font-weight: 800;">🔍 Identifikasi Gulma AI</h1>
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
    Sistem AI berbasis RapidFuzz & Similarity Scoring untuk identifikasi gulma yang akurat
</p>

<p style="
    color: #FFFFFF;
    margin: 12px 0 0 0;
    font-size: 0.95em;
    font-weight: 700;
    text-shadow:
        0 0 5px rgba(245,255,255,0.8),
        0 0 10px rgba(245,255,255,0.7),
        0 0 15px rgba(245,255,255,0.55),
        0 2px 10px rgba(0,0,0,0.25);
">
    ✨ Dengan integrasi Google Lens untuk pengalaman scan modern
</p>
</div>
""", unsafe_allow_html=True)

st.info("""
💡 **Cara Menggunakan:**
1. Pilih ciri-ciri yang Anda amati dari gulma di lapangan
2. Sistem AI akan menghitung similarity score berbasis RapidFuzz
3. Confidence dihitung dari: morfologi + habitat + feature completeness
4. Lihat hasil top 3 dengan smart recommendations & AI insights
""")

st.markdown("---")


st.markdown("---")
st.markdown("### 📋 Identifikasi dengan Memasukkan Ciri-ciri Gulma")

# Create form for user input
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🌱 Morfologi")
    
    bentuk_batang = st.selectbox(
        "Bentuk Batang",
        ["", "Segitiga", "Bulat", "Persegi", "Pipih", "Lainnya"],
        key="bentuk_batang"
    )
    
    tipe_daun = st.selectbox(
        "Tipe Daun",
        ["", "Sempit", "Lebar", "Oblong", "Bujur telur", "Majemuk", "Lainnya"],
        key="tipe_daun"
    )
    
    warna_daun = st.selectbox(
        "Warna Daun",
        ["", "Hijau muda", "Hijau gelap", "Merah", "Kekuningan", "Lainnya"],
        key="warna_daun"
    )
    
    tipe_akar = st.selectbox(
        "Tipe Akar",
        ["", "Serabut", "Tunggang", "Umbi", "Rimpang", "Lainnya"],
        key="tipe_akar"
    )

with col2:
    st.markdown("#### 🌍 Lingkungan & Ciri Khusus")
    
    habitat = st.selectbox(
        "Habitat/Lokasi",
        ["", "Sawah", "Tegalan", "Kebun", "Pekarangan", "Lahan terganggu", "Lainnya"],
        key="habitat"
    )
    
    bunga = st.selectbox(
        "Bunga/Perbungaan",
        ["", "Putih", "Kuning", "Merah", "Ungu", "Tiada/tidak terlihat", "Lainnya"],
        key="bunga"
    )
    
    pola_pertumbuhan = st.selectbox(
        "Pola Pertumbuhan",
        ["", "Tegak", "Merambat", "Merayap", "Terapung", "Berkelompok", "Lainnya"],
        key="pola_pertumbuhan"
    )

# Prepare features dictionary
user_features = {
    "bentuk_batang": bentuk_batang if bentuk_batang else None,
    "tipe_daun": tipe_daun if tipe_daun else None,
    "warna_daun": warna_daun if warna_daun else None,
    "tipe_akar": tipe_akar if tipe_akar else None,
    "habitat": habitat if habitat else None,
    "bunga": bunga if bunga else None,
    "pola_pertumbuhan": pola_pertumbuhan if pola_pertumbuhan else None,
}

# Remove None values
user_features = {k: v for k, v in user_features.items() if v and v != ""}


def premium_progress_bar(score: float) -> str:
    bar_color = "#2563EB" if score >= 70 else "#F59E0B" if score >= 40 else "#DC2626"
    return f"""
    <div style='background: rgba(255,255,255,0.75); border-radius: 14px; overflow: hidden; height: 14px; box-shadow: inset 0 1px 4px rgba(0,0,0,0.08);'>
      <div style='width: {score}%; min-width: 8px; height: 100%; background: linear-gradient(90deg, {bar_color}, #52B788); transition: width 0.4s ease;'></div>
    </div>
    """

# Identification button
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🤖 Identifikasi dengan AI", width='stretch', type="primary"):
        if not user_features:
            st.warning("⚠️ Silakan pilih minimal satu ciri gulma!")
        else:
            st.markdown("---")
            st.markdown("### 🎯 Hasil Identifikasi AI")
            
            # Load database
            database = load_gulma_database()
            
            # Use AI similarity ranking
            ai_results = similarity_ai.rank_weeds(user_features, database)
            
            # Filter top 3 and only show with positive confidence
            top_results = [r for r in ai_results if r["confidence"] > 0][:3]
            
            if top_results:
                st.markdown(f"#### ✅ Ditemukan {len(top_results)} kemungkinan gulma (Ranked by AI):")
                
                for idx, result in enumerate(top_results, 1):
                    gulma = result["weed"]
                    confidence = result["confidence"]
                    
                    # Determine confidence level and color
                    if confidence >= 70:
                        confidence_color = "#2563EB"
                        confidence_badge = "🟢 TINGGI"
                        confidence_text = "Sangat Akurat"
                    elif confidence >= 40:
                        confidence_color = "#F59E0B"
                        confidence_badge = "🟡 SEDANG"
                        confidence_text = "Cukup Akurat"
                    else:
                        confidence_color = "#DC2626"
                        confidence_badge = "🔴 RENDAH"
                        confidence_text = "Verifikasi Diperlukan"
                    
                    # Premium Result Card - Responsive Layout
                    st.markdown("""
                    <style>
                    .result-wrapper { display: flex; gap: 20px; flex-wrap: wrap; }
                    .result-img-box { flex: 0 0 45%; min-width: 280px; }
                    .result-content-box { flex: 1; min-width: 280px; }
                    @media (max-width: 768px) {
                        .result-img-box, .result-content-box { flex: 0 0 100% !important; min-width: auto; }
                        .result-wrapper { gap: 15px; }
                    }
                    </style>
                    """, unsafe_allow_html=True)
                    
                    st.markdown('<div class="result-wrapper">', unsafe_allow_html=True)
                    st.markdown('<div class="result-img-box">', unsafe_allow_html=True)
                    image_displayed = display_weed_image(gulma['nama'], width="stretch")
                    if not image_displayed:
                        st.markdown("""
                        <div style="background: linear-gradient(135deg, #E8F8EE 0%, #D1EDDF 100%);
                                    padding: 72px 16px;
                                    text-align: center;
                                    border-radius: 24px;
                                    box-shadow: 0 12px 30px rgba(27, 67, 50, 0.08);">
                            <p style="font-size: 3.5em; margin: 0;">🌿</p>
                            <p style="color: #1B4332; margin: 12px 0 0 0; font-size: 1rem; font-weight: 600;">Gambar gulma tidak ditemukan</p>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-content-box">', unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="result-card" style="width: 100%; max-width: 100%;">
                        <div style="display: grid; gap: 20px;">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 18px; flex-wrap: wrap;">
                                <div style="min-width: 240px; max-width: 100%;">
                                    <h2 style="margin: 0 0 8px 0; color: #1B4332; font-size: 2rem; line-height: 1.1;">{gulma['nama']}</h2>
                                    <p style="margin: 0; color: #2D6A4F; font-size: 1.05rem; line-height: 1.5;">{format_scientific_name(gulma['nama_ilmiah'])}</p>
                                </div>
                                <div style="padding: 12px 24px; border-radius: 999px; background: {confidence_color}; color: #fff; font-weight: 700; white-space: nowrap; font-size: 0.95rem; letter-spacing: 0.02em;">
                                    {confidence_badge}
                                    </div>
                                </div>
                                <div style="background: linear-gradient(135deg, rgba(236, 255, 239, 0.95) 0%, rgba(232, 245, 233, 0.95) 100%);
                                            border: 1px solid rgba(82, 183, 136, 0.18);
                                            border-radius: 20px;
                                            padding: 22px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap;">
                                        <div>
                                            <p style="margin: 0 0 6px 0; font-weight: 700; color: #1B4332; font-size: 0.98rem;">🤖 AI Confidence Score</p>
                                            <p style="margin: 0; font-size: 1.65rem; font-weight: 800; color: {confidence_color};">{confidence}%</p>
                                        </div>
                                        <div style="font-size: 0.98rem; color: {confidence_color}; font-weight: 700;">{confidence_text}</div>
                                    </div>
                                    <div style="margin-top: 18px;">{premium_progress_bar(confidence)}</div>
                                </div>
                                <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
                                    <div style="background: white; border-radius: 18px; padding: 20px; border: 1px solid rgba(27, 67, 50, 0.08);">
                                        <p style="margin: 0 0 10px 0; font-size: 0.95rem; color: #666; font-weight: 700; letter-spacing: 0.01em;">Famili</p>
                                        <p style="margin: 0; color: #1B4332; font-size: 1.05rem; font-weight: 700;">{gulma['famili']}</p>
                                    </div>
                                    <div style="background: white; border-radius: 18px; padding: 20px; border: 1px solid rgba(27, 67, 50, 0.08);">
                                        <p style="margin: 0 0 10px 0; font-size: 0.95rem; color: #666; font-weight: 700; letter-spacing: 0.01em;">Tingkat Bahaya</p>
                                        <p style="margin: 0; color: #d32f2f; font-size: 1.05rem; font-weight: 700;">{'⭐' * gulma['tingkat_bahaya']} ({gulma['tingkat_bahaya']}/5)</p>
                                    </div>
                                </div>
                                <div style="background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(232, 245, 233, 0.95) 100%);
                                            border-radius: 18px; padding: 20px; border: 1px solid rgba(116, 198, 157, 0.18);">
                                    <p style="margin: 0; font-size: 0.98rem; color: #333; line-height: 1.75;">
                                        <strong>Habitat:</strong> {', '.join(gulma['habitat']) if isinstance(gulma['habitat'], list) else gulma['habitat']}
                                    </p>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)  # Close result-content-box
                    st.markdown('</div>', unsafe_allow_html=True)  # Close result-wrapper

                    st.markdown("")
                    
                    # AI Insights Section
                    with st.expander(f"🧠 AI Insights & Smart Recommendations untuk {gulma['nama']}", expanded=(idx==1)):
                        st.markdown("""
                        <style>
                        .insights-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
                        @media (max-width: 768px) { .insights-grid { grid-template-columns: 1fr; } }
                        </style>
                        """, unsafe_allow_html=True)
                        
                        st.markdown('<div class="insights-grid">', unsafe_allow_html=True)
                        
                        # Danger Level & Threat Assessment
                        danger_level = gulma['tingkat_bahaya']
                        threat_color = "#DC2626" if danger_level >= 4 else "#F59E0B" if danger_level >= 3 else "#2563EB"
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {threat_color}20 0%, {threat_color}10 100%);
                                    border: 2px solid {threat_color};
                                    border-radius: 12px;
                                    padding: 16px;
                                    text-align: center;">
                            <p style="margin: 0 0 8px 0; font-size: 0.85em; color: #666; font-weight: 600;">TINGKAT ANCAMAN</p>
                            <p style="margin: 0; color: {threat_color}; font-weight: 800; font-size: 1.5em;">{'⚠️' if danger_level >= 4 else '⚡'} Level {danger_level}/5</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Morphology Match Score
                        morph_score = result["morphology_score"]
                        morph_color = "#2563EB" if morph_score >= 70 else "#F59E0B" if morph_score >= 40 else "#DC2626"
                        
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {morph_color}20 0%, {morph_color}10 100%);
                                    border: 2px solid {morph_color};
                                    border-radius: 12px;
                                    padding: 16px;
                                    text-align: center;">
                            <p style="margin: 0 0 8px 0; font-size: 0.85em; color: #666; font-weight: 600;">MORFOLOGI MATCH</p>
                            <p style="margin: 0; color: {morph_color}; font-weight: 800; font-size: 1.5em;">{morph_score:.0f}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Habitat Match Score
                        habitat_score = result["habitat_score"]
                        habitat_color = "#2563EB" if habitat_score >= 70 else "#F59E0B" if habitat_score >= 40 else "#DC2626"
                        
                        st.markdown(f"""
                            <div style="background: linear-gradient(135deg, {habitat_color}20 0%, {habitat_color}10 100%);
                                        border: 2px solid {habitat_color};
                                        border-radius: 12px;
                                        padding: 16px;
                                        text-align: center;">
                                <p style="margin: 0 0 8px 0; font-size: 0.85em; color: #666; font-weight: 600;">HABITAT MATCH</p>
                                <p style="margin: 0; color: {habitat_color}; font-weight: 800; font-size: 1.5em;">{habitat_score:.0f}%</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)  # Close insights-grid
                        
                        # Smart Recommendations
                        st.markdown("#### 💡 Rekomendasi Pengendalian Cerdas")
                        
                        recommendations = recommendation_engine.get_best_control_method(
                            gulma, 
                            habitat if habitat else "Tegalan",
                            danger_level
                        )
                        
                        for rec in recommendations:
                            rec_color = "#DC2626" if rec["priority"] == "UTAMA" else "#F59E0B" if rec["priority"] == "TINGGI" else "#2563EB"
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, {rec_color}20 0%, {rec_color}10 100%);
                                        border-left: 4px solid {rec_color};
                                        border-radius: 8px;
                                        padding: 12px;
                                        margin-bottom: 8px;">
                                <p style="margin: 0 0 4px 0; font-weight: 700; color: {rec_color};">⚡ {rec['method']}</p>
                                <p style="margin: 0; font-size: 0.9em; color: #333;">Efektivitas: {rec['effectiveness']}% | {rec['reason']}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Herbicide Recommendations
                        st.markdown("#### 💊 Rekomendasi Herbisida")
                        
                        herbicides = recommendation_engine.get_herbicide_recommendation(
                            gulma['nama'],
                            habitat if habitat else "Tegalan",
                            danger_level,
                            gulma
                        )
                        
                        herb_cols = st.columns(min(3, len(herbicides)))
                        for i, herb in enumerate(herbicides[:3]):
                            with herb_cols[i % 3]:
                                herb_name = herb.get('name', 'N/A')
                                herb_confidence = herb.get('confidence', 0)
                                herb_dosis = herb.get('dosis', 'Sesuai label')
                                
                                herb_html = f"""
                                <div style="background: white;
                                            border: 2px solid #52B788;
                                            border-radius: 12px;
                                            padding: 12px;
                                            text-align: center;">
                                    <p style="margin: 0 0 4px 0; font-weight: 700; color: #1B4332;">{herb_name}</p>
                                    <p style="margin: 0; font-size: 0.8em; color: #666;">Confidence: {herb_confidence}%</p>
                                """
                                
                                if herb.get('dosis'):
                                    herb_html += f'<p style="margin: 4px 0 0 0; font-size: 0.8em; color: #2D6A4F;">Dosis: {herb_dosis}</p>'
                                
                                herb_html += '</div>'
                                st.markdown(herb_html, unsafe_allow_html=True)
                        
                        # Add Indonesian Herbicide Database options
                        st.markdown("")
                        st.markdown("#### 🌿 Herbisida Indonesia Tersedia")
                        st.markdown("*Pilihan herbisida yang tersedia di pasaran Indonesia:*")
                        
                        indonesian_herbicides = get_herbisida_for_gulma(gulma['nama'])
                        if indonesian_herbicides:
                            herb_cols = st.columns(min(2, len(indonesian_herbicides)))
                            for i, merk_dagang in enumerate(indonesian_herbicides):
                                with herb_cols[i % 2]:
                                    display_herbisida_card(merk_dagang)
                        else:
                            st.info("Herbisida khusus untuk gulma ini sedang dikurasi. Silakan konsultasi dengan ahli pertanian.")
                        
                        st.markdown("</div>", unsafe_allow_html=True)  # Close grid div
                        st.markdown("</div>", unsafe_allow_html=True)  # Close result-card div
                        st.markdown("</div>", unsafe_allow_html=True)  # Close padding div
                    
                    # Detailed information tabs
                    st.markdown("")
                    
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "📋 Morfologi",
                        "⚠️ Dampak & Bahaya",
                        "💊 Pengendalian",
                        "📚 Referensi"
                    ])
                    
                    with tab1:
                        st.markdown("**Deskripsi Morfologi Lengkap:**")
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if "morfologi" in gulma:
                                for key, value in list(gulma["morfologi"].items())[:3]:
                                    st.markdown(f"""
                                    <div style="background: white; border-left: 4px solid #52B788; padding: 12px; margin: 8px 0; border-radius: 6px;">
                                        <p style="margin: 0; font-weight: 600; color: #1B4332;">{key.replace('_', ' ').title()}</p>
                                        <p style="margin: 4px 0 0 0; color: #333; font-size: 0.9em;">{value}</p>
                                    </div>
                                    """, unsafe_allow_html=True)
                        with col_b:
                            if "morfologi" in gulma:
                                for key, value in list(gulma["morfologi"].items())[3:6]:
                                    st.markdown(f"""
                                    <div style="background: white; border-left: 4px solid #52B788; padding: 12px; margin: 8px 0; border-radius: 6px;">
                                        <p style="margin: 0; font-weight: 600; color: #1B4332;">{key.replace('_', ' ').title()}</p>
                                        <p style="margin: 4px 0 0 0; color: #333; font-size: 0.9em;">{value}</p>
                                    </div>
                                    """, unsafe_allow_html=True)
                    
                    with tab2:
                        st.markdown("**Dampak Terhadap Tanaman:**")
                        st.markdown(f"🚨 {gulma['dampak_tanaman'] if 'dampak_tanaman' in gulma else gulma.get('dampak', 'Data tidak tersedia')}")
                        
                        if 'manfaat' in gulma and gulma['manfaat']:
                            st.markdown("**Potensi Manfaat:**")
                            st.markdown(f"✅ {gulma['manfaat']}")
                    
                    with tab3:
                        st.markdown("**Metode Pengendalian:**")
                        col_m1, col_m2 = st.columns(2)
                        
                        with col_m1:
                            st.markdown("**🔧 Mekanis:**")
                            st.markdown(gulma.get('pengendalian_mekanis', 'Data tidak tersedia'))
                            
                            st.markdown("**🌱 Biologis:**")
                            st.markdown(gulma.get('pengendalian_biologis', 'Data tidak tersedia'))
                        
                        with col_m2:
                            st.markdown("**🌾 Kultur Teknis:**")
                            st.markdown(gulma.get('pengendalian_kultur_teknis', 'Data tidak tersedia'))
                            
                            st.markdown("**⏰ Waktu Aplikasi:**")
                            st.markdown(gulma.get('waktu_aplikasi', 'Data tidak tersedia'))
                    
                    with tab4:
                        st.markdown("**📚 Referensi Jurnal:**")
                        if 'referensi_jurnal' in gulma and gulma['referensi_jurnal']:
                            for ref in gulma['referensi_jurnal'][:5]:
                                st.markdown(f"- {ref}")
                        else:
                            st.markdown("- Data referensi tidak tersedia")
                        
                        st.markdown(f"**Sumber Ilmiah:** {gulma.get('sumber_ilmiah', 'GULMAFY Database')}")
                    
                    st.markdown("---")
            else:
                st.error("❌ Tidak ada gulma yang cocok dengan ciri yang Anda masukkan. Silakan coba lagi dengan ciri yang berbeda.")

# Google Lens - Direct Access
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(147, 197, 253, 0.08) 100%);
            border: 2px solid rgba(59, 130, 246, 0.3);
            border-radius: 24px;
            padding: 40px 32px;
            margin-bottom: 36px;
            box-shadow: 0 8px 24px rgba(27, 67, 50, 0.06);
            backdrop-filter: blur(10px);">
    <div style="text-align: center;">
        <p style="margin: 0 0 16px 0; font-size: 0.95rem; color: #2D6A4F; font-weight: 700; letter-spacing: 0.02em;">🔍 PENCARIAN VISUAL DENGAN GOOGLE LENS</p>
        <h2 style="margin: 0 0 12px 0; color: #1B4332; font-size: 2rem; font-weight: 800;">Analisis Gambar dengan Google Lens</h2>
        <p style="margin: 0 0 24px 0; color: #2D6A4F; font-size: 0.98rem; line-height: 1.6;">
            Akses Google Lens untuk menganalisis foto tanaman Anda. Upload atau ambil foto gulma untuk mendapatkan hasil pencarian visual dari database global Google secara langsung dan otomatis.
        </p>
        <a href="https://lens.google.com" target="_blank" style="display: inline-block; padding: 18px 50px; background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%); color: white; border-radius: 14px; text-decoration: none; font-weight: 700; font-size: 1.1rem; cursor: pointer; box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3); transition: all 0.3s ease; letter-spacing: 0.02em;"
           onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 12px 32px rgba(59, 130, 246, 0.4)';"
           onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 24px rgba(59, 130, 246, 0.3)';">
            📸 Buka Google Lens Sekarang
        </a>
        <p style="color: #666; font-size: 0.9rem; margin: 24px 0 0 0; line-height: 1.8;">
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Help section
st.markdown("---")
st.markdown("### ℹ️ Panduan Identifikasi Berbasis AI")

with st.expander("❓ Bagaimana AI RapidFuzz kami bekerja?"):
    st.markdown("""
    Sistem identifikasi kami menggunakan **teknologi AI modern**:
    
    **🤖 RapidFuzz Similarity Scoring:**
    - Token-based fuzzy matching untuk perbandingan ciri-ciri
    - String similarity (ratio, token_set_ratio) hingga 100%
    - Intelligent comparison tanpa case-sensitivity
    
    **📊 Weighted Feature Matching:**
    - Bentuk Batang: 12% |  Tipe Daun: 15% | Warna Daun: 10%
    - Tipe Akar: 13% | Habitat: 15% | Bunga: 12% | Pola Pertumbuhan: 13%
    
    **✨ Confidence Calculation:**
    - Morphology Score (60% weight)
    - Habitat Match (40% weight)
    - Feature Completeness Bonus (0-20%)
    - Total: 0-100% AI Confidence
    """)

with st.expander("📊 Bagaimana Confidence Score dihitung?"):
    st.markdown("""
    | Rentang | Interpretasi | Akurasi | Rekomendasi |
    |---------|-------------|---------|-------------|
    | **80-100%** | 🟢 Sangat Tinggi | Identifikasi sangat akurat | Dapat langsung diterapkan |
    | **60-79%** | 🟢 Tinggi | Identifikasi kemungkinan akurat | Cukup dapat dipercaya |
    | **40-59%** | 🟡 Sedang | Mungkin perlu verifikasi | Verifikasi lapangan disarankan |
    | **< 40%** | 🔴 Rendah | Kemungkinan identifikasi kurang akurat | Konsultasi ahli diperlukan |
    
    **💡 Tips AI:** 
    - Semakin banyak ciri yang Anda pilih dengan akurat → Confidence lebih tinggi
    - Habitat yang tepat → Boosts confidence score hingga 40%
    - Morphology match sempurna → Garantikan akurasi tertinggi
    """)

with st.expander("🎯 Smart Recommendations System"):
    st.markdown("""
    Sistem rekomendasi kami secara otomatis memilih metode pengendalian berdasarkan:
    
    **⚡ Danger Level Analysis:**
    - Level 4-5 (Bahaya Tinggi): Rekomendasi herbisida + mekanis agresif
    - Level 2-3 (Sedang): Kultur teknis + pengendalian manual
    - Level 1 (Rendah): Pemantauan & pengendalian manual
    
    **🌍 Habitat-Specific Strategies:**
    - **Sawah**: Herbisida selektif (2,4-D, Anilofos, Pendimethalin)
    - **Tegalan**: Herbisida non-selektif (Glifosad, Paraquat)
    - **Kebun**: Pengendalian lokal (Glifosad, combined spraying)
    
    **✅ Effectiveness Rating:**
    - UTAMA (90-95%): Rekomendasi utama untuk pengendalian maksimal
    - TINGGI (75-90%): Alternatif efektif dengan environmental care
    - SEDANG (60-75%): Supplementary methods untuk kontrol komprehensif
    """)

with st.expander("🧠 Bagaimana AI Insights bekerja?"):
    st.markdown("""
    Setiap identifikasi dilengkapi dengan **AI-Generated Insights**:
    
    1. **Threat Assessment** 🚨
       - Mengevaluasi tingkat ancaman berdasarkan danger level
       - Memberikan urgency indicator
    
    2. **Morphology Match Score** 📐
       - Mengukur seberapa cocok ciri yang Anda input
       - Range: 0-100% dengan RapidFuzz matching
    
    3. **Habitat Match Score** 🌍
       - Mengevaluasi kecocokan habitat yang dipilih
       - Boost confidence jika sempurna, reduce jika tidak cocok
    
    4. **Smart Control Recommendations** 💡
       - Otomatis memilih strategi terbaik
       - Berdasarkan danger level + habitat
       - Dengan effectiveness rating untuk each method
    
    5. **Herbicide Matching** 💊
       - AI-powered herbicide selection
       - Berdasarkan weed characteristics
       - Dengan confidence scores per recommendation
    """)

st.markdown("---")
create_footer()
