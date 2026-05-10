"""
Logique métier — calculs ROI Enakl
"""

from typing import Tuple, List, Dict


# ── Tarification Enakl ───────────────────────────────────────────────────────
PRICE_PER_EMPLOYEE = {
    "Standard": 120,    # MAD/salarié/mois
    "Premium": 180,
    "Enterprise": 250,
}

def get_enakl_price(nb_employees: int, plan: str) -> float:
    """Calcule le coût mensuel Enakl selon le nombre de salariés et le plan."""
    rate = PRICE_PER_EMPLOYEE.get(plan, 180)
    return nb_employees * rate


# ── Calcul des économies ─────────────────────────────────────────────────────
def compute_savings(
    current_monthly: float, enakl_monthly: float
) -> Tuple[float, float, float]:
    """
    Retourne (économies_mensuelles, économies_annuelles, pourcentage_économies).
    """
    savings_monthly = current_monthly - enakl_monthly
    savings_annual = savings_monthly * 12
    savings_pct = (savings_monthly / current_monthly * 100) if current_monthly > 0 else 0
    return savings_monthly, savings_annual, round(savings_pct, 1)


# ── Économies de temps ───────────────────────────────────────────────────────
def compute_time_savings(
    hours_per_week: float, nb_managers: int, reduction_rate: float = 0.70
) -> Tuple[float, float]:
    """
    Estime les heures de gestion économisées grâce à l'automatisation Enakl.
    Enakl réduit la charge opérationnelle d'environ 70%.
    Retourne (heures_par_mois, heures_par_an).
    """
    weekly_total = hours_per_week * nb_managers
    monthly_saved = weekly_total * 4.33 * reduction_rate
    annual_saved = monthly_saved * 12
    return round(monthly_saved, 1), round(annual_saved, 1)


# ── Insights automatiques ────────────────────────────────────────────────────
def generate_insights(
    savings_pct: float,
    hours_year: float,
    transport_mode: str,
    nb_employees: int,
    savings_annual: float,
) -> List[Dict]:
    """Génère des insights business contextualisés."""
    insights = []

    if savings_pct > 0:
        insights.append({
            "icon": "💰",
            "color": "orange",
            "text": (
                f"Votre entreprise pourrait réduire ses coûts de transport de **{savings_pct:.1f}%**, "
                f"soit **{savings_annual:,.0f} MAD** d'économies annuelles."
            ),
        })
    elif savings_pct < 0:
        insights.append({
            "icon": "📊",
            "color": "blue",
            "text": (
                "Le plan sélectionné est supérieur à votre coût actuel. "
                "Cela peut s'expliquer par des services additionnels (technologie, accompagnement, reporting). "
                "Essayez le plan Standard pour maximiser vos économies directes."
            ),
        })

    if hours_year > 0:
        insights.append({
            "icon": "⏱",
            "color": "purple",
            "text": (
                f"L'automatisation via Enakl permettrait d'économiser environ **{hours_year:.0f} heures** "
                f"de gestion administrative par an — du temps libéré pour vos équipes RH et opérations."
            ),
        })

    mode_insights = {
        "Flotte interne": (
            "🚗",
            "green",
            "Le modèle flotte interne présente une forte dépendance aux coûts variables "
            "(carburant, maintenance, chauffeurs). Enakl transforme ces charges imprévisibles "
            "en forfait mensuel fixe et prévisible.",
        ),
        "Externalisation transporteur": (
            "🔄",
            "green",
            "En passant à Enakl, vous conservez la flexibilité d'un prestataire tout en gagnant "
            "en visibilité temps réel, en optimisation data-driven des lignes et en reporting mensuel.",
        ),
        "Indemnités de transport": (
            "🌱",
            "green",
            "Les indemnités individuelles sont peu optimisées vs le transport mutualisé. "
            "Enakl peut réduire votre empreinte carbone de **40–60%** par trajet grâce à la mutualisation.",
        ),
    }
    if transport_mode in mode_insights:
        icon, color, text = mode_insights[transport_mode]
        insights.append({"icon": icon, "color": color, "text": text})

    if nb_employees >= 200:
        insights.append({
            "icon": "🏆",
            "color": "orange",
            "text": (
                f"Avec **{nb_employees} collaborateurs**, vous êtes éligible au plan Enterprise "
                "avec des conditions tarifaires négociées, un CSM dédié et un onboarding prioritaire."
            ),
        })
    elif nb_employees >= 50:
        insights.append({
            "icon": "📈",
            "color": "purple",
            "text": (
                f"Votre volume de **{nb_employees} salariés** vous permet de bénéficier "
                "d'une optimisation de lignes sur mesure et d'un accompagnement dédié dès le déploiement."
            ),
        })

    return insights


# ── Projection 3 ans ─────────────────────────────────────────────────────────
def project_3_years(savings_monthly: float) -> Dict:
    """
    Retourne les données de projection des économies cumulées sur 3 ans.
    """
    months = list(range(1, 37))
    labels = []
    cumulative = []
    for m in months:
        if m <= 12:
            labels.append(f"M{m}")
        elif m <= 24:
            labels.append(f"M{m}" if m % 3 == 0 else "")
        else:
            labels.append(f"M{m}" if m % 6 == 0 else "")
        cumulative.append(round(savings_monthly * m, 0))

    # Points clés pour annotations
    milestones = {
        12: round(savings_monthly * 12, 0),
        24: round(savings_monthly * 24, 0),
        36: round(savings_monthly * 36, 0),
    }
    return {"months": months, "labels": labels, "cumulative": cumulative, "milestones": milestones}
