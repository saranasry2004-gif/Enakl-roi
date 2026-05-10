"""Composant header Enakl"""
import streamlit as st


def render_header():
    st.markdown("""
    <div class="enakl-header">
        <div class="enakl-logo">
            <svg width="32" height="32" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="20" cy="20" r="20" fill="white"/>
                <path d="M20 8C14 8 9 13.5 9 19.5C9 27 20 34 20 34C20 34 31 27 31 19.5C31 13.5 26 8 20 8Z" fill="#FF5A00"/>
                <circle cx="20" cy="19" r="5" fill="white"/>
            </svg>
            Enakl
        </div>
        <span class="logo-badge">Simulateur ROI Entreprise</span>
    </div>
    """, unsafe_allow_html=True)
