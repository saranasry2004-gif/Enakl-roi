# Enakl ROI Simulator 🚌

Application Streamlit B2B premium pour simuler les économies réalisées en adoptant la solution Enakl.

## Structure du projet

```

├── app.py                    # Point d'entrée principal
├── requirements.txt
└── components/
    ├── __init__.py
    ├── header.py             # Header avec logo
    ├── kpi_cards.py          # 4 KPI cards dashboard
    ├── charts.py             # Graphiques Plotly (bar, pie, line)
    ├── insights.py           # Insights automatiques
    └── roi_section.py        # Bannière ROI orange
   ├── utils/
│   ├── __init__.py
│   ├── calculations.py       # Logique métier & calculs ROI
│   └── styles.py             # CSS custom branding Enakl
```
## Installation locale

```bash
# 1. Cloner / télécharger le projet
cd enakl_roi

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
streamlit run app.py
```

L'app s'ouvre automatiquement sur http://localhost:8501

## Déploiement sur Streamlit Cloud

1. Pusher le projet sur un dépôt GitHub (public ou privé)
2. Aller sur https://share.streamlit.io
3. Cliquer **"New app"**
4. Sélectionner votre dépôt, branche `main`, fichier `app.py`
5. Cliquer **"Deploy"**

Votre app sera accessible en quelques minutes sur une URL publique.

## Personnalisation

### Modifier les tarifs Enakl
Dans `utils/calculations.py`, ajuster `PRICE_PER_EMPLOYEE` :
```python
PRICE_PER_EMPLOYEE = {
    "Standard": 120,    # MAD/salarié/mois
    "Premium": 180,
    "Enterprise": 250,
}
```

### Modifier les couleurs
Dans `utils/styles.py`, modifier les variables CSS :
```css
--orange: #FF5A00;
--purple: #4B3FB5;
```

### Ajouter un secteur d'activité
Dans `app.py`, ajouter à la liste du `st.selectbox` secteur.
