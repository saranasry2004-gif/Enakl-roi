"""Composant insights automatiques"""
import streamlit as st
from typing import List, Dict


def render_insights(insights: List[Dict]):
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">💡 Insights business automatiques</div>', unsafe_allow_html=True)

    color_map = {
        "orange": "insight-orange",
        "purple": "insight-purple",
        "green": "insight-green",
        "blue": "insight-blue",
    }

    for insight in insights:
        css_class = color_map.get(insight["color"], "insight-orange")
        text = insight["text"].replace("**", "<strong>").replace("**", "</strong>")
        # Proper markdown bold handling
        import re
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', insight["text"])
        st.markdown(f"""
        <div class="insight-item {css_class}">
            <span class="insight-icon">{insight['icon']}</span>
            <span class="insight-text">{text}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
