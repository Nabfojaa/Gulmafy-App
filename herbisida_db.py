"""
Database Herbisida Indonesia
Herbicide information for weed control recommendations
"""

HERBISIDA_INDONESIA = {
    "Roundup": {
        "merk_dagang": "Roundup",
        "bahan_aktif": "Glyphosate 360 g/L",
        "target": "Gulma daun sempit dan tahunan",
        "dosis": "2–5 L/ha",
        "cara_kerja": "Sistemik, absorbsi lewat daun dan ditranslokasi ke akar",
        "catatan": "Gunakan sesuai dosis anjuran. Tanaman pangan harus dalam fase istirahat sebelum aplikasi herbisida."
    },
    "Gramoxone": {
        "merk_dagang": "Gramoxone",
        "bahan_aktif": "Paraquat 20% w/v",
        "target": "Gulma daun sempit, tahunan, dan musiman",
        "dosis": "1–2 L/ha",
        "cara_kerja": "Kontak, merusak klorofil dan sel tumbuhan dalam beberapa jam",
        "catatan": "Herbisida kontak yang cepat bekerja. Sangat efektif pada gulma muda."
    },
    "DMA 6": {
        "merk_dagang": "DMA 6",
        "bahan_aktif": "2,4-D Amine 60% w/v",
        "target": "Gulma daun lebar musiman (dikot)",
        "dosis": "0.5–1 L/ha",
        "cara_kerja": "Sistemik selektif, terutama untuk dikotil",
        "catatan": "Sangat efektif untuk teki dan gulma daun lebar. Jangan gunakan pada padi."
    },
    "Ally Plus": {
        "merk_dagang": "Ally Plus",
        "bahan_aktif": "Metsulfuron + 2,4-D amine",
        "target": "Gulma daun lebar dan sempit musiman",
        "dosis": "0.3–0.5 kg/ha",
        "cara_kerja": "Sistemik pre-emergent dan post-emergent",
        "catatan": "Untuk padi dan tanaman pangan lainnya. Campurkan dengan air secukupnya."
    },
    "Lindomin": {
        "merk_dagang": "Lindomin",
        "bahan_aktif": "Pendimethalin 38% w/v",
        "target": "Gulma daun lebar dan sempit musiman (pre-emergent)",
        "dosis": "2–2.5 L/ha",
        "cara_kerja": "Pre-emergent, bekerja pada perkecambahan gulma",
        "catatan": "Aplikasi 2–3 hari sebelum tanam. Sangat efektif pada teki dan gulma musiman."
    },
    "Supremo": {
        "merk_dagang": "Supremo",
        "bahan_aktif": "Glyphosate 100% SL",
        "target": "Gulma tahunan dan musiman",
        "dosis": "2–4 L/ha",
        "cara_kerja": "Sistemik non-selektif",
        "catatan": "Untuk pengendalian gulma sebelum tanam. Jangan semprotkan langsung ke tanaman."
    },
    "Polaris": {
        "merk_dagang": "Polaris",
        "bahan_aktif": "Metolachlor 50% EC",
        "target": "Gulma daun lebar dan sempit musiman",
        "dosis": "1.5–2 L/ha",
        "cara_kerja": "Pre-emergent",
        "catatan": "Aplikasi pada lahan kering sebelum penggenangan untuk padi."
    },
    "Sidafos": {
        "merk_dagang": "Sidafos",
        "bahan_aktif": "Glyphosate + Amonium sulfat",
        "target": "Gulma perennial dan annual",
        "dosis": "2–5 L/ha",
        "cara_kerja": "Sistemik, butuh waktu 7–10 hari untuk efek maksimal",
        "catatan": "Tambahkan amonium sulfat untuk meningkatkan efektivitas."
    },
    "Noxone": {
        "merk_dagang": "Noxone",
        "bahan_aktif": "2,4-D Ester 60% v/v",
        "target": "Gulma daun lebar (dikotil)",
        "dosis": "0.75–1.5 L/ha",
        "cara_kerja": "Sistemik selektif untuk tumbuhan monokotil",
        "catatan": "Sangat aman untuk padi, sangat efektif untuk teki dan gulma daun lebar."
    },
    "Basmilang": {
        "merk_dagang": "Basmilang",
        "bahan_aktif": "Glifosat 486 SL",
        "target": "Gulma semusim dan perennial",
        "dosis": "2–4 L/ha",
        "cara_kerja": "Sistemik non-selektif dengan rapid action",
        "catatan": "Cocok untuk persiapan lahan. Hasil visible dalam 3–5 hari."
    }
}

def get_herbisida_for_gulma(nama_gulma):
    """Get recommended herbicides for specific weed"""
    rekomendasi = {
        "teki": ["DMA 6", "Lindomin", "Noxone", "Ally Plus"],
        "alang-alang": ["Roundup", "Gramoxone", "Supremo", "Polaris"],
        "bandotan": ["DMA 6", "2,4-D Amine", "Ally Plus"],
        "rumput grinting": ["Lindomin", "Polaris", "Pendimethalin"],
        "babandotan": ["DMA 6", "Noxone"],
        "putri malu": ["DMA 6", "Ally Plus"],
        "krokot": ["DMA 6", "Gramoxone"],
    }
    
    nama_lower = nama_gulma.lower()
    return rekomendasi.get(nama_lower, ["Roundup", "Gramoxone", "DMA 6"])

def get_herbisida_details(merk_dagang):
    """Get detailed information about specific herbicide"""
    return HERBISIDA_INDONESIA.get(merk_dagang, {})

def display_herbisida_card(merk_dagang):
    """Display herbicide information in card format"""
    import streamlit as st
    
    info = get_herbisida_details(merk_dagang)
    if not info:
        return
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #E8F8EE 0%, #F4FFF8 100%);
                border: 2px solid #74C69D;
                border-radius: 14px;
                padding: 20px;
                margin: 12px 0;">
        <h4 style="color: #1B4332; margin-top: 0; font-size: 1.1em;">💊 {info.get('merk_dagang', '')}</h4>
        <div style="color: #2D6A4F; font-size: 0.95em; line-height: 1.8;">
            <p><strong>Bahan Aktif:</strong> {info.get('bahan_aktif', '')}</p>
            <p><strong>Target Gulma:</strong> {info.get('target', '')}</p>
            <p><strong>Dosis Umum:</strong> {info.get('dosis', '')}</p>
            <p><strong>Cara Kerja:</strong> {info.get('cara_kerja', '')}</p>
            <p style="border-top: 1px solid #74C69D; padding-top: 12px; margin-top: 12px; font-size: 0.9em; color: #1B4332;"><strong>⚠️ Catatan:</strong> {info.get('catatan', '')}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
