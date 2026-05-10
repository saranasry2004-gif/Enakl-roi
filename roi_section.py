"""Composant section ROI — bannière orange"""
import streamlit as st


def render_roi_section(
    savings_monthly: float,
    savings_annual: float,
    savings_pct: float,
    total_annual: float,
    enakl_annual: float,
):
    roi_ratio = (savings_annual / enakl_annual * 100) if enakl_annual > 0 else 0
    sign = "+" if savings_annual >= 0 else ""

    st.markdown(f"""
    <div class="roi-banner">
        <div class="roi-banner-title">🏆 &nbsp;Résumé ROI — Votre retour sur investissement</div>
        <div class="roi-grid">
            <div>
                <div class="roi-val">{sign}{savings_pct:.1f}%</div>
                <div class="roi-lbl">Réduction des coûts</div>
            </div>
            <div>
                <div class="roi-val">{sign}{savings_monthly:,.0f} MAD</div>
                <div class="roi-lbl">Économies / mois</div>
            </div>
            <div>
                <div class="roi-val">{sign}{savings_annual:,.0f} MAD</div>
                <div class="roi-lbl">Économies / an</div>
            </div>
            <div>
                <div class="roi-val">{sign}{savings_annual * 3:,.0f} MAD</div>
                <div class="roi-lbl">Économies sur 3 ans</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
