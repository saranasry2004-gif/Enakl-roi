"""
CSS custom — Branding Enakl
Orange #FF5A00, Purple #4B3FB5, blanc, dark #1A1A2E
"""

import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    /* ── Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* ── Reset & base ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 0 !important; padding-bottom: 2rem; max-width: 1200px; }
    .stDeployButton { display: none; }
    [data-testid="collapsedControl"] { display: none; }

    /* ── Enakl variables ── */
    :root {
        --orange: #FF5A00;
        --orange-light: #FF7A30;
        --orange-bg: #FFF3ED;
        --purple: #4B3FB5;
        --purple-bg: #EEEDFE;
        --dark: #1A1A2E;
        --gray-bg: #F8F8F6;
        --border: rgba(0,0,0,0.08);
        --text: #1A1A2E;
        --text-muted: #6B7280;
    }

    /* ── Custom header (top bar) ── */
    .enakl-header {
        background: var(--orange);
        padding: 14px 32px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0;
    }
    .enakl-logo {
        display: flex;
        align-items: center;
        gap: 10px;
        color: white;
        font-size: 22px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .logo-badge {
        background: rgba(255,255,255,0.2);
        color: white;
        font-size: 12px;
        padding: 4px 12px;
        border-radius: 50px;
    }

    /* ── Hero section ── */
    .hero-section {
        background: var(--orange);
        padding: 48px 40px 52px;
        text-align: center;
        margin-bottom: 32px;
    }
    .hero-title {
        color: white;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 14px;
        line-height: 1.2;
    }
    .hero-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 16px;
        max-width: 580px;
        margin: 0 auto 28px;
        line-height: 1.6;
    }
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 60px;
    }
    .hero-stat {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
    }
    .stat-val {
        color: white;
        font-size: 30px;
        font-weight: 700;
    }
    .stat-lbl {
        color: rgba(255,255,255,0.8);
        font-size: 13px;
    }

    /* ── Form cards ── */
    .form-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 20px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }
    .section-label {
        font-size: 13px;
        font-weight: 600;
        color: var(--orange);
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-bottom: 18px;
    }

    /* ── Plan cards ── */
    .plan-card {
        background: white;
        border: 1.5px solid var(--border);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.2s ease;
    }
    .plan-card:hover {
        border-color: var(--orange-light);
        transform: translateY(-2px);
    }
    .plan-featured {
        border: 2.5px solid var(--orange) !important;
        background: var(--orange-bg) !important;
    }
    .plan-badge {
        background: var(--orange);
        color: white;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 50px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .plan-name {
        font-size: 15px;
        font-weight: 600;
        color: var(--dark);
        margin-bottom: 6px;
    }
    .plan-price {
        font-size: 26px;
        font-weight: 700;
        color: var(--orange);
        margin-bottom: 2px;
    }
    .plan-unit {
        font-size: 12px;
        color: var(--text-muted);
    }
    .plan-desc {
        font-size: 12px;
        color: var(--text-muted);
        margin-top: 8px;
        font-style: italic;
    }

    /* ── Primary button override ── */
    .stButton > button[kind="primary"] {
        background: var(--orange) !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 14px 36px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(255,90,0,0.35) !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(255,90,0,0.4) !important;
    }
    .stButton > button {
        border-radius: 50px !important;
    }

    /* ── Dashboard title ── */
    .dash-title h2 {
        font-size: 22px;
        font-weight: 700;
        color: var(--dark);
        margin-bottom: 4px;
    }
    .dash-title p {
        font-size: 13px;
        color: var(--text-muted);
    }
    .dash-divider {
        border: none;
        border-top: 1px solid var(--border);
        margin: 16px 0 24px;
    }

    /* ── KPI cards ── */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 24px;
    }
    .kpi-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 18px 20px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }
    .kpi-card-orange { border-left: 4px solid var(--orange); }
    .kpi-card-green  { border-left: 4px solid #22c55e; }
    .kpi-card-purple { border-left: 4px solid var(--purple); }
    .kpi-label {
        font-size: 12px;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.4px;
        margin-bottom: 10px;
    }
    .kpi-value {
        font-size: 22px;
        font-weight: 700;
        color: var(--dark);
        margin-bottom: 4px;
        line-height: 1.1;
    }
    .kpi-value-orange { color: var(--orange); }
    .kpi-value-green  { color: #16a34a; }
    .kpi-value-purple { color: var(--purple); }
    .kpi-sub {
        font-size: 12px;
        color: var(--text-muted);
    }
    .kpi-icon {
        position: absolute;
        top: 14px; right: 14px;
        font-size: 22px;
        opacity: 0.15;
    }

    /* ── Chart cards ── */
    .chart-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 20px 22px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        margin-bottom: 16px;
    }
    .chart-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--dark);
        margin-bottom: 14px;
    }

    /* ── Insights ── */
    .insight-item {
        display: flex;
        gap: 12px;
        align-items: flex-start;
        padding: 14px 16px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .insight-orange { background: var(--orange-bg); }
    .insight-purple { background: var(--purple-bg); }
    .insight-green  { background: #f0fdf4; }
    .insight-blue   { background: #eff6ff; }
    .insight-icon { font-size: 20px; margin-top: 1px; flex-shrink: 0; }
    .insight-text {
        font-size: 14px;
        color: var(--dark);
        line-height: 1.6;
    }

    /* ── ROI banner ── */
    .roi-banner {
        background: var(--orange);
        border-radius: 16px;
        padding: 28px 32px;
        color: white;
        margin-top: 24px;
        margin-bottom: 24px;
    }
    .roi-banner-title {
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 20px;
        opacity: 0.9;
    }
    .roi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        text-align: center;
    }
    .roi-val {
        font-size: 26px;
        font-weight: 700;
    }
    .roi-lbl {
        font-size: 12px;
        opacity: 0.85;
        margin-top: 4px;
    }

    /* ── Radio buttons style ── */
    .stRadio > div {
        background: var(--gray-bg);
        border-radius: 50px;
        padding: 4px;
        display: inline-flex;
        gap: 4px;
    }
    .stRadio label {
        border-radius: 50px !important;
        padding: 6px 16px !important;
        cursor: pointer;
    }

    /* ── Inputs ── */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div {
        border-radius: 10px !important;
        border: 1.5px solid #E5E7EB !important;
        font-size: 14px !important;
    }
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus {
        border-color: var(--orange) !important;
        box-shadow: 0 0 0 2px rgba(255,90,0,0.1) !important;
    }

    /* ── Download button ── */
    .stDownloadButton button {
        background: transparent !important;
        border: 1.5px solid var(--orange) !important;
        color: var(--orange) !important;
        border-radius: 50px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }

    /* ── Link button ── */
    .stLinkButton a {
        background: var(--dark) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)
