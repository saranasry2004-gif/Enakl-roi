"""
Enakl ROI Simulator
Application Streamlit B2B premium pour simuler les économies Enakl
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils.calculations import (
    get_enakl_price,
    compute_savings,
    compute_time_savings,
    generate_insights,
    project_3_years,
)
from utils.styles import inject_css
from components.header import render_header
from components.kpi_cards import render_kpi_cards
from components.charts import render_charts
from components.roi_section import render_roi_section
from components.insights import render_insights

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Simulateur ROI — Enakl",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
render_header()

# ── Session state ─────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "form"

# ═════════════════════════════════════════════════════════════════════════════
# PAGE 1 — FORMULAIRE
# ═════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "form":

    # Hero section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Calculez vos économies avec Enakl</h1>
        <p class="hero-subtitle">
            Découvrez en quelques minutes combien votre entreprise pourrait économiser
            en confiant la mobilité de vos collaborateurs à Enakl.
        </p>
        <div class="hero-stats">
            <div class="hero-stat"><span class="stat-val">−30%</span><span class="stat-lbl">Réduction des coûts</span></div>
            <div class="hero-stat"><span class="stat-val">−50%</span><span class="stat-lbl">CO₂ par trajet</span></div>
            <div class="hero-stat"><span class="stat-val">4.9/5</span><span class="stat-lbl">Satisfaction usagers</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Section 1 : Informations générales ───────────────────────────────────
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">🏢 &nbsp;Informations générales</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        secteur = st.selectbox(
            "Secteur d'activité *",
            ["", "Industrie", "Services", "BTP", "Agroalimentaire",
             "Retail", "IT", "Santé", "Finance", "Logistique", "Autre"],
        )
    with col2:
        ville = st.text_input("Ville principale *", placeholder="ex: Casablanca")
    with col3:
        nb_salaries = st.number_input(
            "Nombre de salariés bénéficiant du transport *",
            min_value=1, max_value=10000, value=100, step=10,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Section 2 : Mode de transport ────────────────────────────────────────
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">🚌 &nbsp;Mode de transport actuel</p>', unsafe_allow_html=True)

    mode = st.radio(
        "Quel est votre mode de transport actuel ?",
        ["Externalisation transporteur", "Flotte interne", "Indemnités de transport"],
        horizontal=True,
        label_visibility="collapsed",
    )

    cost_breakdown = {}

    if mode == "Externalisation transporteur":
        c1, c2, c3 = st.columns(3)
        with c1:
            cost_breakdown["Mensualité transporteur"] = st.number_input(
                "Mensualité transporteur (MAD/mois)", min_value=0, value=45000, step=1000,
            )
        with c2:
            cost_breakdown["Frais additionnels"] = st.number_input(
                "Frais additionnels (MAD/mois)", min_value=0, value=5000, step=500,
            )
        with c3:
            cost_breakdown["Coûts administratifs"] = st.number_input(
                "Coûts administratifs (MAD/mois)", min_value=0, value=3000, step=500,
            )

    elif mode == "Flotte interne":
        c1, c2, c3 = st.columns(3)
        with c1:
            cost_breakdown["Salaires chauffeurs"] = st.number_input(
                "Salaires chauffeurs (MAD/mois)", min_value=0, value=20000, step=1000,
            )
            cost_breakdown["Assurance"] = st.number_input(
                "Assurance (MAD/mois)", min_value=0, value=3000, step=500,
            )
        with c2:
            cost_breakdown["Carburant"] = st.number_input(
                "Carburant (MAD/mois)", min_value=0, value=12000, step=500,
            )
            cost_breakdown["Amortissement véhicules"] = st.number_input(
                "Amortissement véhicules (MAD/mois)", min_value=0, value=8000, step=500,
            )
        with c3:
            cost_breakdown["Maintenance"] = st.number_input(
                "Maintenance (MAD/mois)", min_value=0, value=5000, step=500,
            )
            cost_breakdown["Redevance crédit-bail"] = st.number_input(
                "Redevance crédit-bail (MAD/mois)", min_value=0, value=0, step=500,
            )

    else:  # Indemnités
        cost_breakdown["Indemnités de transport"] = st.number_input(
            "Montant total mensuel des indemnités (MAD)", min_value=0, value=30000, step=1000,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Section 3 : Gestion opérationnelle ───────────────────────────────────
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">⏱ &nbsp;Gestion opérationnelle</p>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        heures_sem = st.number_input(
            "Heures/semaine consacrées à la gestion transport",
            min_value=0, max_value=80, value=8,
        )
    with c2:
        nb_gestionnaires = st.number_input(
            "Nombre de personnes gérant le transport",
            min_value=0, max_value=50, value=2,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Section 4 : Plan Enakl ────────────────────────────────────────────────
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">✨ &nbsp;Simulation Enakl — Choisissez votre modèle</p>', unsafe_allow_html=True)

    price_std = get_enakl_price(nb_salaries, "Standard")
    price_pre = get_enakl_price(nb_salaries, "Premium")
    price_ent = get_enakl_price(nb_salaries, "Enterprise")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="plan-card">
            <p class="plan-name">Standard</p>
            <p class="plan-price">{price_std:,.0f} MAD</p>
            <p class="plan-unit">/ mois</p>
            <p class="plan-desc">Plateforme SaaS</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="plan-card plan-featured">
            <span class="plan-badge">⭐ Recommandé</span>
            <p class="plan-name">Premium</p>
            <p class="plan-price">{price_pre:,.0f} MAD</p>
            <p class="plan-unit">/ mois</p>
            <p class="plan-desc">Gestion + technologie</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="plan-card">
            <p class="plan-name">Enterprise</p>
            <p class="plan-price">{price_ent:,.0f} MAD</p>
            <p class="plan-unit">/ mois</p>
            <p class="plan-desc">Transport complet</p>
        </div>""", unsafe_allow_html=True)

    plan_choice = st.radio(
        "Plan sélectionné",
        ["Standard", "Premium", "Enterprise"],
        index=1,
        horizontal=True,
        label_visibility="collapsed",
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # ── CTA ───────────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    col_cta = st.columns([2, 1, 2])
    with col_cta[1]:
        if st.button("📊 Voir mes économies avec Enakl →", use_container_width=True, type="primary"):
            # Sauvegarder dans la session
            st.session_state.form_data = {
                "secteur": secteur,
                "ville": ville,
                "nb_salaries": nb_salaries,
                "mode": mode,
                "cost_breakdown": cost_breakdown,
                "heures_sem": heures_sem,
                "nb_gestionnaires": nb_gestionnaires,
                "plan_choice": plan_choice,
            }
            st.session_state.page = "dashboard"
            st.rerun()


# ═════════════════════════════════════════════════════════════════════════════
# PAGE 2 — DASHBOARD RÉSULTATS
# ═════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "dashboard":

    fd = st.session_state.form_data
    breakdown = fd["cost_breakdown"]
    total_monthly = sum(breakdown.values())
    total_annual = total_monthly * 12
    enakl_monthly = get_enakl_price(fd["nb_salaries"], fd["plan_choice"])
    enakl_annual = enakl_monthly * 12
    savings_monthly, savings_annual, savings_pct = compute_savings(total_monthly, enakl_monthly)
    heures_month, heures_year = compute_time_savings(fd["heures_sem"], fd["nb_gestionnaires"])
    insights = generate_insights(savings_pct, heures_year, fd["mode"], fd["nb_salaries"], savings_annual)
    projection = project_3_years(savings_monthly)

    # ── Dashboard header ──────────────────────────────────────────────────────
    col_back, col_title, col_dl = st.columns([1, 4, 1])
    with col_back:
        if st.button("← Modifier"):
            st.session_state.page = "form"
            st.rerun()
    with col_title:
        st.markdown(f"""
        <div class="dash-title">
            <h2>Votre analyse ROI Enakl</h2>
            <p>{fd['secteur']} • {fd['ville']} • {fd['nb_salaries']} collaborateurs • Plan {fd['plan_choice']}</p>
        </div>""", unsafe_allow_html=True)
    with col_dl:
        st.download_button(
            "⬇ Télécharger",
            data=f"Rapport ROI Enakl\n{fd['secteur']} – {fd['ville']}\nÉconomies annuelles: {savings_annual:,.0f} MAD",
            file_name="rapport_roi_enakl.txt",
            mime="text/plain",
        )

    st.markdown("<hr class='dash-divider'>", unsafe_allow_html=True)

    # ── KPI Cards ─────────────────────────────────────────────────────────────
    render_kpi_cards(total_annual, enakl_annual, savings_annual, savings_pct, heures_month, heures_year)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Charts ────────────────────────────────────────────────────────────────
    render_charts(total_annual, enakl_annual, breakdown, projection)

    # ── Insights ─────────────────────────────────────────────────────────────
    render_insights(insights)

    # ── ROI Section ───────────────────────────────────────────────────────────
    render_roi_section(savings_monthly, savings_annual, savings_pct, total_annual, enakl_annual)

    # ── CTA Demo ─────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        st.link_button(
            "📅 Demander une démonstration",
            url="https://enakl.com",
            use_container_width=True,
            type="primary",
        )
