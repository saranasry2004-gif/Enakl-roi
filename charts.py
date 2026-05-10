"""Composant graphiques Plotly — branding Enakl"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict

ORANGE = "#FF5A00"
PURPLE = "#4B3FB5"
ORANGE_LIGHT = "#FF7A30"
PURPLE_LIGHT = "#7F77DD"
GRAY = "#E5E7EB"

CHART_CONFIG = {"displayModeBar": False, "responsive": True}

LAYOUT_BASE = dict(
    font_family="Inter, sans-serif",
    font_color="#1A1A2E",
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=10, r=10, t=20, b=10),
)


def render_charts(
    total_annual: float,
    enakl_annual: float,
    breakdown: Dict[str, float],
    projection: Dict,
):
    col1, col2 = st.columns(2)

    # ── Graphique 1 : Bar comparatif ─────────────────────────────────────────
    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">📊 Comparatif avant / après Enakl</div>', unsafe_allow_html=True)

        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(
            x=["Avant Enakl", "Avec Enakl"],
            y=[total_annual, enakl_annual],
            marker_color=[ORANGE, PURPLE],
            text=[f"{total_annual:,.0f} MAD", f"{enakl_annual:,.0f} MAD"],
            textposition="outside",
            textfont=dict(size=12, color="#1A1A2E"),
            width=0.45,
        ))
        fig_bar.update_layout(
            **LAYOUT_BASE,
            height=260,
            showlegend=False,
            yaxis=dict(
                showgrid=True,
                gridcolor=GRAY,
                tickformat=",.0f",
                ticksuffix=" MAD",
                tickfont=dict(size=10),
            ),
            xaxis=dict(tickfont=dict(size=13, color="#1A1A2E")),
        )
        st.plotly_chart(fig_bar, use_container_width=True, config=CHART_CONFIG)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Graphique 2 : Camembert répartition coûts ─────────────────────────────
    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">🥧 Répartition des coûts actuels</div>', unsafe_allow_html=True)

        colors_pie = [ORANGE, ORANGE_LIGHT, PURPLE, PURPLE_LIGHT, "#AFA9EC", "#FF9955", "#FFB380"]
        labels = list(breakdown.keys())
        values = list(breakdown.values())

        if any(v > 0 for v in values):
            fig_pie = go.Figure(go.Pie(
                labels=labels,
                values=values,
                hole=0.45,
                marker_colors=colors_pie[:len(labels)],
                textinfo="percent",
                textfont=dict(size=12),
                hovertemplate="<b>%{label}</b><br>%{value:,.0f} MAD<br>%{percent}<extra></extra>",
            ))
            fig_pie.update_layout(
                **LAYOUT_BASE,
                height=260,
                showlegend=True,
                legend=dict(
                    orientation="v",
                    x=1.02, y=0.5,
                    font=dict(size=10),
                ),
            )
            st.plotly_chart(fig_pie, use_container_width=True, config=CHART_CONFIG)
        else:
            st.info("Renseignez vos coûts pour voir la répartition.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ── Graphique 3 : Projection 3 ans ────────────────────────────────────────
    st.markdown('<div class="chart-card"><div class="chart-title">📈 Projection des économies cumulées sur 3 ans</div>', unsafe_allow_html=True)

    months = projection["months"]
    cumulative = projection["cumulative"]
    milestones = projection["milestones"]

    fig_line = go.Figure()

    # Zone remplie
    fig_line.add_trace(go.Scatter(
        x=months,
        y=cumulative,
        mode="lines",
        line=dict(color=ORANGE, width=2.5),
        fill="tozeroy",
        fillcolor="rgba(255,90,0,0.08)",
        hovertemplate="Mois %{x} : %{y:,.0f} MAD<extra></extra>",
        name="Économies cumulées",
    ))

    # Points clés
    for m, val in milestones.items():
        label = f"An {m // 12}" if m % 12 == 0 else f"M{m}"
        fig_line.add_annotation(
            x=m, y=val,
            text=f"<b>{val:,.0f} MAD</b>",
            showarrow=True,
            arrowhead=2,
            arrowcolor=ORANGE,
            arrowsize=1,
            font=dict(size=11, color=ORANGE),
            bgcolor="white",
            bordercolor=ORANGE,
            borderwidth=1,
            borderpad=4,
            ax=0, ay=-35,
        )

    fig_line.update_layout(
        **LAYOUT_BASE,
        height=240,
        showlegend=False,
        yaxis=dict(
            showgrid=True,
            gridcolor=GRAY,
            tickformat=",.0f",
            ticksuffix=" MAD",
            tickfont=dict(size=10),
        ),
        xaxis=dict(
            tickvals=[1, 6, 12, 18, 24, 30, 36],
            ticktext=["M1", "M6", "An 1", "18m", "An 2", "30m", "An 3"],
            tickfont=dict(size=10),
        ),
    )
    st.plotly_chart(fig_line, use_container_width=True, config=CHART_CONFIG)
    st.markdown('</div>', unsafe_allow_html=True)
