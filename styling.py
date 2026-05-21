"""
Styling utilities for Gulmafy application
Modern Premium Agriculture AI Design System - Soft Green Premium Theme
"""
import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to Streamlit app - Modern Premium Soft Green Design"""
    # Add Google Fonts link
    st.markdown('<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,0..100&display=swap" rel="stylesheet">', unsafe_allow_html=True)
    
    # Add CSS styles
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,0..100&display=swap');
    
    /* ============================================
       THEME COLORS - Premium Modern Soft Green Palette
       ============================================ */
    :root {
        --primary-dark: #1B4332;      /* Very dark green - main color */
        --primary: #2D6A4F;           /* Dark green primary */
        --primary-light: #52B788;     /* Medium green */
        --accent: #74C69D;            /* Soft green accent */
        --accent-light: #95D5B2;      /* Light green accent */
        --bg-primary: #F4FFF8;        /* Very soft green background */
        --bg-secondary: #E8F8EE;      /* Secondary soft green */
        --bg-white: #FFFFFF;          /* Pure white */
        --bg-soft-gray: #F9FAFB;      /* Soft gray background */
        --text-dark: #1B4332;         /* Dark green for high contrast text */
        --text-light: #2D6A4F;        /* Medium green for secondary text */
        --border-color: rgba(45, 106, 79, 0.15);
        --shadow-sm: 0 2px 8px rgba(27, 67, 50, 0.06);
        --shadow-md: 0 4px 16px rgba(27, 67, 50, 0.10);
        --shadow-lg: 0 8px 24px rgba(27, 67, 50, 0.12);
        --shadow-xl: 0 12px 32px rgba(27, 67, 50, 0.15);
    }
    
    /* ============================================
       GLOBAL STYLES
       ============================================ */
    html, body, .main {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24 !important;
        font-feature-settings: 'liga' 1 !important;
        text-rendering: optimizeLegibility;
        letter-spacing: normal !important;
        speak: none;
    }
    
    html, body {
        background: linear-gradient(135deg, #F4FFF8 0%, #E8F8EE 100%);
        color: var(--text-dark);
    }
    
    .main {
        background: linear-gradient(135deg, #F4FFF8 0%, #E8F8EE 100%);
        padding: 3rem 2rem;
    }
    
    /* ============================================
       SIDEBAR STYLING
       ============================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1B4332 0%, #2D6A4F 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 700;
    }

    [data-testid="stSidebar"] a {
        color: white !important;
        text-decoration: none !important;
    }

    [data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
        border-radius: 14px;
        margin: 8px 10px;
        padding: 12px 14px;
        background: rgba(255,255,255,0.08);
        transition: all 0.25s ease;
        font-weight: 600;
    }

    [data-testid="stSidebar"] [data-testid="stSidebarNavLink"][aria-current="page"] {
        background: rgba(255,255,255,0.18) !important;
        box-shadow: 0 10px 24px rgba(0,0,0,0.16);
        border-left: 4px solid var(--accent-light);
    }

    [data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover {
        background: rgba(255,255,255,0.14);
        transform: translateX(2px);
    }

    /* ============================================
       HEADERS & TYPOGRAPHY
       ============================================ */
  h1 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 2.5rem !important;
    letter-spacing: -0.5px;
    margin-bottom: 0.5rem !important;

    /* outline soft dark green */
    text-shadow:
        -1.5px -1.5px 0 #1B4332,
         1.5px -1.5px 0 #1B4332,
        -1.5px  1.5px 0 #1B4332,
         1.5px  1.5px 0 #1B4332,
         0 4px 10px rgba(0,0,0,0.20);
}

    }
    
    h1.white-heading {
        color: #FFFFFF !important;
    }
    
    h2 {
        color: var(--primary) !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        margin-top: 2rem !important;
    }
    
    h2.white-heading {
        color: #FFFFFF !important;
    }
    
    h3 {
        color: var(--primary) !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
    }
    
    h3.white-heading {
        color: #FFFFFF !important;
    }
    
    h4 {
        color: var(--text-dark) !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    p {
        color: var(--text-dark) !important;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    /* ============================================
       METRIC CARDS - Modern Premium Style
       ============================================ */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.90) 100%);
        border-radius: 16px;
        padding: 24px;
        box-shadow: var(--shadow-md);
        border-left: 5px solid var(--primary-light);
        border: 1px solid var(--border-color);
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-left: 5px solid var(--primary);
    }
    
    /* ============================================
       CARDS & CONTAINERS
       ============================================ */
    .card-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.90) 100%);
        border-radius: 16px;
        padding: 24px;
        box-shadow: var(--shadow-md);
        border: 1px solid var(--border-color);
        margin-bottom: 20px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
    }
    
    .card-container:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
    }
    
    .premium-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(147, 197, 253, 0.05) 100%);
        border-radius: 20px;
        padding: 32px 24px;
        border: 2px solid var(--accent-light);
        box-shadow: 0 8px 32px rgba(30, 64, 175, 0.08);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .premium-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 48px rgba(30, 64, 175, 0.15);
        border-color: var(--primary);
    }

    .result-card {
        background: rgba(255,255,255,0.95);
        border-radius: 24px;
        padding: 22px;
        margin-bottom: 26px;
        border: 1px solid rgba(59,130,246,0.18);
        box-shadow: 0 18px 46px rgba(30,64,175,0.08);
        backdrop-filter: blur(16px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        max-width: 100%;
        min-width: 0;
        overflow: hidden;
        overflow-wrap: break-word;
        word-break: break-word;
    }

    .result-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 22px 58px rgba(30,64,175,0.12);
    }

    .result-card h2 {
        margin: 0 0 4px 0;
        font-size: 1.8rem;
        color: #1B4332 !important;
        font-weight: 800;
        word-wrap: break-word;
    }

    .result-card p {
        margin: 0;
        word-wrap: break-word;
        color: #1B4332 !important;
        font-weight: 500;
    }
    
    .result-card span {
        color: #2D6A4F !important;
        font-weight: 600;
    }

    /* AI Confidence Score Card */
    .ai-confidence-card {
        background: linear-gradient(135deg, rgba(229, 248, 240, 0.95) 0%, rgba(216, 243, 220, 0.95) 100%);
        border: 2px solid var(--primary-light);
        border-radius: 20px;
        padding: 20px;
        margin: 16px 0;
        backdrop-filter: blur(10px);
    }
    
    .ai-confidence-card p,
    .ai-confidence-card div {
        color: #1B4332 !important;
        font-weight: 600;
    }

    .confidence-badge {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.9rem;
        white-space: nowrap;
    }

    .confidence-high { background: #2563EB; color: white; }
    .confidence-medium { background: #F59E0B; color: white; }
    .confidence-low { background: #EF4444; color: white; }

    /* Modern Image Container */
    .image-wrapper {
        border-radius: 28px;
        overflow: hidden;
        box-shadow: 0 24px 60px rgba(30, 64, 175, 0.12);
        transition: all 0.3s ease;
    }

    .image-wrapper img {
        width: 100%;
        height: auto;
        display: block;
        object-fit: cover;
    }

    .image-wrapper:hover {
        box-shadow: 0 32px 80px rgba(30, 64, 175, 0.18);
        transform: translateY(-2px);
    }
    
    /* ============================================
       BUTTONS - Modern Premium Style
       ============================================ */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
        color: white !important;
        border-radius: 12px;
        border: none;
        padding: 12px 32px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: var(--shadow-md);
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* ============================================
       TABS - Modern Premium
       ============================================ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        border-bottom: 2px solid var(--border-color);
        padding: 16px 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: var(--bg-soft-gray);
        border-radius: 12px 12px 0 0;
        color: var(--text-light);
        border: none;
        padding: 12px 24px;
        transition: all 0.3s;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
    }
    
    /* ============================================
       EXPANDERS
       ============================================ */
    .streamlit-expanderHeader {
        background-color: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 197, 253, 0.1) 100%) !important;
        border-radius: 12px;
        border: 1px solid var(--accent-light);
        color: var(--primary) !important;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(147, 197, 253, 0.15) 100%) !important;
    }
    
    /* ============================================
       INPUT FIELDS
       ============================================ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background-color: var(--bg-white) !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        color: var(--text-dark) !important;
        transition: all 0.3s;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
        outline: none !important;
    }
    
    /* ============================================
       DATAFRAME & TABLE
       ============================================ */
    .dataframe {
        background-color: var(--bg-white) !important;
        border-radius: 12px !important;
        overflow: hidden;
    }
    
    .dataframe th {
        background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%) !important;
        color: white !important;
        font-weight: 700;
        padding: 12px 16px !important;
    }
    
    .dataframe td {
        padding: 12px 16px !important;
        border-bottom: 1px solid var(--border-color) !important;
        color: var(--text-dark) !important;
    }
    
    .dataframe tbody tr:hover {
        background-color: rgba(59, 130, 246, 0.05) !important;
    }
    
    /* ============================================
       INFO & WARNING BOXES
       ============================================ */
    .stInfo, [data-testid="stInfo"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(191, 219, 254, 0.1) 100%);
        border-left: 5px solid var(--primary);
        border-radius: 12px;
        padding: 16px;
    }
    
    .stWarning, [data-testid="stWarning"] {
        background: linear-gradient(135deg, rgba(255, 193, 7, 0.1) 0%, rgba(255, 235, 59, 0.1) 100%);
        border-left: 5px solid #FFC107;
        border-radius: 12px;
        padding: 16px;
    }
    
    .stError, [data-testid="stError"] {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.1) 0%, rgba(255, 87, 87, 0.1) 100%);
        border-left: 5px solid #F44336;
        border-radius: 12px;
        padding: 16px;
    }
    
    .stSuccess, [data-testid="stSuccess"] {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(129, 199, 132, 0.1) 100%);
        border-left: 5px solid #4CAF50;
        border-radius: 12px;
        padding: 16px;
    }
    
    /* ============================================
       DIVIDER & HR
       ============================================ */
    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent 0%, var(--border-color) 50%, transparent 100%) !important;
        margin: 2rem 0 !important;
    }
    
    /* ============================================
       SLIDER
       ============================================ */
    .stSlider > div > div > div {
        background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
    }
    
    /* ============================================
       FILE UPLOADER
       ============================================ */
    .stFileUploader {
        border-radius: 12px;
        border: 2px dashed var(--accent-light);
        padding: 32px;
    }
    
    /* ============================================
       SCROLLBAR
       ============================================ */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-soft-gray);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--primary-light) 0%, var(--primary) 100%);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--primary) 0%, var(--primary-dark) 100%);
    }
    
    /* ============================================
       IMAGE CONTAINER
       ============================================ */
    .image-container {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: var(--shadow-lg);
        border: 1px solid var(--border-color);
    }
    
    img {
        border-radius: 12px;
        transition: all 0.3s;
    }
    
    img:hover {
        transform: scale(1.02);
    }
    
    /* ============================================
       FOOTER
       ============================================ */
    .footer {
        text-align: center;
        padding: 40px 20px;
        margin-top: 60px;
        border-top: 2px solid var(--border-color);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.5) 0%, rgba(234, 242, 255, 0.3) 100%);
        backdrop-filter: blur(10px);
    }
    
    .footer-text {
        color: #1B4332 !important;
        font-size: 0.95rem;
        line-height: 1.8;
        font-weight: 500;
    }

    .footer-text strong {
        color: #2D6A4F !important;
    }
    
    /* ============================================
       ANIMATIONS
       ============================================ */
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes glow {
        0% {
            box-shadow: 0 0 5px rgba(59, 130, 246, 0.3);
        }
        50% {
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
        }
        100% {
            box-shadow: 0 0 5px rgba(59, 130, 246, 0.3);
        }
    }
    
    .animate-in {
        animation: slideInUp 0.6s ease-out;
    }
    
    .glow-effect {
        animation: glow 3s ease-in-out infinite;
    }
    
    /* ============================================
       RESPONSIVE DESIGN - Mobile First
       ============================================ */
    @media (max-width: 1024px) {
        h1 {
            font-size: 2.2rem !important;
        }
        
        .result-card {
            padding: 18px;
        }
    }

    @media (max-width: 768px) {
        h1 {
            font-size: 1.8rem !important;
        }

        h2 {
            font-size: 1.4rem !important;
            margin-top: 1.5rem !important;
        }

        h3 {
            font-size: 1.1rem !important;
        }
        
        p {
            font-size: 0.95rem;
        }
        
        .main {
            padding: 1.5rem 1rem;
        }
        
        [data-testid="metric-container"] {
            padding: 12px;
        }
        
        .card-container {
            padding: 12px;
        }

        .result-card {
            padding: 14px;
            margin-bottom: 16px;
            width: 100% !important;
        }

        .result-card h2 {
            font-size: 1.4rem;
        }

        .premium-card {
            padding: 20px 16px;
        }
        
        /* Responsive grid for result card content */
        [data-testid="column"] > div > div > div[style*="display: grid"] {
            grid-template-columns: 1fr !important;
        }
        
        [data-testid="column"] > div > div > div[style*="grid-template-columns: repeat(2"] {
            grid-template-columns: 1fr !important;
        }

        [data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
            margin: 4px 8px;
            padding: 10px 12px;
            font-size: 0.9rem;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 10px 16px;
            font-size: 0.9rem;
        }

        [data-testid="stFileUploader"] {
            padding: 20px;
        }

        .image-wrapper {
            border-radius: 20px;
        }

        .ai-confidence-card {
            padding: 16px;
            margin: 12px 0;
        }
    }

    @media (max-width: 480px) {
        h1 {
            font-size: 1.5rem !important;
            margin-bottom: 0.3rem !important;
        }

        h2 {
            font-size: 1.2rem !important;
            margin-top: 1rem !important;
        }

        h3 {
            font-size: 1rem !important;
        }

        p {
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .main {
            padding: 1rem 0.75rem;
        }

        [data-testid="stSidebar"] {
            width: 280px !important;
        }

        [data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
            margin: 2px 6px;
            padding: 8px 10px;
            font-size: 0.85rem;
        }

        .result-card {
            padding: 12px;
            margin-bottom: 12px;
        }

        .result-card h2 {
            font-size: 1.2rem;
        }

        .premium-card {
            padding: 16px 12px;
        }

        .stButton > button {
            padding: 10px 24px;
            font-size: 0.9rem;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 8px 12px;
            font-size: 0.8rem;
        }

        .ai-confidence-card {
            padding: 12px;
            margin: 10px 0;
        }
    }
    
    /* ============================================
       RESPONSIVE DESIGN - Tablet (768px)
       ============================================ */
    @media (min-width: 768px) and (max-width: 1024px) {
        h1 { font-size: 2rem !important; }
        h2 { font-size: 1.5rem !important; }
        h3 { font-size: 1.1rem !important; }
        
        [data-testid="column"] > div {
            padding: 12px 8px !important;
        }
    }
    
    /* ============================================
       RESPONSIVE DESIGN - Desktop (1024px+)
       ============================================ */
    @media (min-width: 1024px) {
        h1 { font-size: 2.8rem !important; }
        h2 { font-size: 1.9rem !important; }
        h3 { font-size: 1.4rem !important; }
        
        [data-testid="column"] > div {
            padding: 16px 12px !important;
        }
        
        .stImage {
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(27, 67, 50, 0.12);
        }
    }
    </style>
    """, unsafe_allow_html=True)


def get_danger_level_color(level):
    """Return color based on danger level (1-5)"""
    colors = {
        1: "#2563EB",  # Blue - Low
        2: "#52B788",  # Light green - Low-Medium
        3: "#F59E0B",  # Amber - Medium
        4: "#EF6F2A",  # Orange - High
        5: "#DC2626"   # Red - Critical
    }
    return colors.get(level, "#6B7280")

def get_confidence_color(confidence):
    """Return color based on confidence score (0-100)"""
    if confidence >= 70:
        return "#2563EB"  # Blue - High confidence
    elif confidence >= 40:
        return "#F59E0B"  # Amber - Medium confidence
    else:
        return "#DC2626"  # Red - Low confidence

def create_metric_card(title, value, unit="", icon="📊"):
    """Create a styled metric card"""
    st.markdown(f"""
    <div class="card-container">
        <p style="color: #999; font-size: 0.9em; margin: 0;">{icon} {title}</p>
        <h3 style="margin: 10px 0; color: #2D6A4F;">{value} <span style="font-size: 0.7em; color: #52B788;">{unit}</span></h3>
    </div>
    """, unsafe_allow_html=True)

def create_success_box(message):
    """Create a success notification box"""
    st.markdown(f'<div class="success-box">{message}</div>', unsafe_allow_html=True)

def create_warning_box(message):
    """Create a warning notification box"""
    st.markdown(f'<div class="warning-box">{message}</div>', unsafe_allow_html=True)

def create_info_box(message):
    """Create an info notification box"""
    st.markdown(f'<div class="info-box">{message}</div>', unsafe_allow_html=True)

def create_danger_box(message):
    """Create a danger notification box"""
    st.markdown(f'<div class="danger-box">{message}</div>', unsafe_allow_html=True)

def create_result_card(title, subtitle="", content=""):
    """Create a premium result card"""
    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">{title}</div>
        {f'<div class="result-subtitle">{subtitle}</div>' if subtitle else ''}
        {f'<div style="color: var(--text-dark); font-size: 0.95rem; line-height: 1.8;">{content}</div>' if content else ''}
    </div>
    """, unsafe_allow_html=True)

def format_scientific_name(scientific_name):
    """
    Format scientific name according to botanical nomenclature rules.
    Genus and species are italicized, author and year are not.
    Returns HTML formatted string that can be used with unsafe_allow_html=True.
    
    Rules:
    - Genus + species should be italic (via HTML <i> tags)
    - Author citation (L., Beauv., etc.) should NOT be italic
    - Subspecies/variety indicators should NOT be italic
    
    Examples:
        Input: "Imperata cylindrica (L.) Beauv."
        Output: "<i>Imperata cylindrica</i> (L.) Beauv."
        
        Input: "Cyperus rotundus L."
        Output: "<i>Cyperus rotundus</i> L."
        
        Input: "Eichhornia crassipes (Mart.) Solms"
        Output: "<i>Eichhornia crassipes</i> (Mart.) Solms"
    
    Args:
        scientific_name: Full scientific name including author
    
    Returns:
        HTML formatted string with proper italics using <i> tags
    """
    if not scientific_name or not isinstance(scientific_name, str):
        return scientific_name
    
    name = scientific_name.strip()
    
    if not name:
        return name
    
    # Split into parts
    parts = name.split()
    
    if len(parts) < 2:
        # Single word, italicize it
        return f"<i>{name}</i>"
    
    # Identify italic parts (genus + species) vs author parts
    italic_parts = []
    author_parts = []
    found_author = False
    
    for i, part in enumerate(parts):
        if found_author:
            author_parts.append(part)
            continue
        
        # Check for author markers
        # 1. Starts with parenthesis: (L.), (Mart.), etc.
        # 2. Single letters with dot: L., J., K.
        # 3. Abbreviated names with dot: Beauv., Merr., Solms., etc.
        # 4. var. or subsp. indicators
        if (part.startswith('(') or 
            (len(part) <= 4 and part.endswith('.') and len(part) > 1 and part[0].isupper()) or
            part in ['var.', 'subsp.', 'f.', 'subvar.']):
            # This is the start of author/taxonomic rank info
            author_parts.append(part)
            found_author = True
        else:
            # Still in genus/species
            italic_parts.append(part)
    
    # Build result with HTML formatting
    if not italic_parts:
        return name  # Safety fallback
    
    italic_text = ' '.join(italic_parts)
    author_text = ' '.join(author_parts) if author_parts else ""
    
    if author_text:
        return f"<i>{italic_text}</i> {author_text}"
    else:
        return f"<i>{italic_text}</i>"

def display_latin_name(scientific_name):
    """
    Display scientific name in Streamlit with proper formatting.
    Automatically uses unsafe_allow_html=True for proper rendering.
    
    Example:
        display_latin_name("Imperata cylindrica (L.) Beauv.")
        Output: Displays as italic "Imperata cylindrica" with non-italic author
    
    Args:
        scientific_name: The scientific name to display
    """
    formatted = format_scientific_name(scientific_name)
    st.markdown(formatted, unsafe_allow_html=True)

def create_footer():
    """Create modern premium footer"""
    st.markdown("""
    <div class="footer">
        <div class="footer-text">
            🌿 <strong>GULMAFY - Smart Weed Knowledge System Indonesia</strong><br><br>
            Version 1.0 | © 2026 | Dikembangkan dengan ❤️ dari<br>
            <strong>Mahasiswa Agroekoteknologi Untirta</strong><br>
            <strong>Pertanian Presisi Kelompok 1 (6C)</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_confidence_bar(confidence):
    """Create a modern confidence progress bar"""
    # Determine color based on confidence
    if confidence >= 70:
        color = "#2563EB"  # Blue
        status = "Tinggi"
    elif confidence >= 40:
        color = "#F59E0B"  # Amber
        status = "Sedang"
    else:
        color = "#DC2626"  # Red
        status = "Rendah"
    
    st.markdown(f"""
    <div style="margin: 16px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-weight: 600; color: var(--text-dark);">Kepercayaan AI</span>
            <span style="font-weight: 700; color: {color};">{confidence}% ({status})</span>
        </div>
        <div style="background-color: rgba(30, 64, 175, 0.1); border-radius: 10px; height: 10px; overflow: hidden;">
            <div style="background: linear-gradient(90deg, #52B788, #2D6A4F); width: {confidence}%; height: 100%; border-radius: 10px; transition: width 0.3s ease;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

