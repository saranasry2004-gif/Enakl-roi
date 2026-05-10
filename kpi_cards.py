"""Composant KPI cards dashboard"""
import streamlit as st


def render_kpi_cards(
    total_annual: float,
    enakl_annual: float,
    savings_annual: float,
    savings_pct: float,
    heures_month: float,
    heures_year: float,
):
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi-card kpi-card-orange">
            <div class="kpi-icon">💳</div>
            <div class="kpi-label">Charges annuelles actuelles</div>
            <div class="kpi-value kpi-value-orange">{total_annual:,.0f}</div>
            <div class="kpi-sub">MAD / an</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card kpi-card-purple">
            <div class="kpi-icon">✨</div>
            <div class="kpi-label">Charges annuelles avec Enakl</div>
            <div class="kpi-value kpi-value-purple">{enakl_annual:,.0f}</div>
            <div class="kpi-sub">MAD / an</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        sign = "−" if savings_annual >= 0 else "+"
        st.markdown(f"""
        <div class="kpi-card kpi-card-green">
            <div class="kpi-icon">📉</div>
            <div class="kpi-label">Économies annuelles estimées</div>
            <div class="kpi-value kpi-value-green">{sign}{abs(savings_annual):,.0f}</div>
            <div class="kpi-sub">{sign}{abs(savings_pct):.1f}% vs coût actuel</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">⏱</div>
            <div class="kpi-label">Temps de gestion économisé</div>
            <div class="kpi-value">{heures_year:.0f}h</div>
            <div class="kpi-sub">{heures_month:.0f}h économisées/mois</div>
        </div>
        """, unsafe_allow_html=True)
