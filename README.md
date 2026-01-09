## 📊 Analyse des Sinistres – Data Analytics Assurance  
**De la donnée brute à l’aide à la décision métier**


## 🚀 Contexte & Objectif
Ce projet vise à analyser les **données de sinistres d’une compagnie d’assurance** afin de mieux comprendre :
- le comportement des sinistres,
- la qualité des données,
- les leviers d’optimisation opérationnelle et stratégique
- Période d'analyse : 2020-2021 (pandémie covid 19).

L’objectif est double :
- **Mettre en œuvre une démarche data complète** (EDA, nettoyage, modélisation, visualisation),
- **Fournir des indicateurs exploitables** pour les équipes métier (gestion des sinistres, partenaires, performance).

---

## 🛠️ Stack & Outils
- **Dataiku DSS** : préparation des données, recipes visuels, modélisation, dashboards
- **Python** (Notebook Dataiku) : EDA, nettoyage automatisé, analyses statistiques
- **Visualisation** : Charts & Dashboards Dataiku

---

## 📂 Données
Les données portent sur des **sinistres d’assurance** et incluent :
- Informations sur les sinistres
- Données agents et vendors (partenaires)
- Variables catégorielles, numériques et temporelles

> ⚠️ Certaines valeurs atypiques sont conservées volontairement, car la période d’analyse coïncide avec la **pandémie Covid-19**, justifiant des comportements exceptionnels.

---

## 🔍 Méthodologie

### 1️⃣ Analyse Exploratoire (EDA) – Python
Réalisation d’une EDA complète dans un notebook Dataiku :
- Analyse de la structure et des types de données
- Statistiques descriptives (moyenne, médiane, min/max, écart-type)
- Détection et analyse des valeurs manquantes
- Traitement des valeurs manquantes catégorielles par le **mode**
- Analyse des doublons complets
- Détection des valeurs aberrantes via **boxplots**

📌 *Aucune normalisation n’a été appliquée afin de préserver la réalité métier.*

---

### 2️⃣ Nettoyage & Intégration dans le Flow Dataiku
- Création d’un **dataset managé vide** dans le Flow
- Chargement automatisé du dataset nettoyé depuis Python
- Gain de temps et **industrialisation du nettoyage**

---

### 3️⃣ Préparation & Modélisation – Recipes Dataiku
**Prepare Recipe**
- Correction des types sémantiques
- Nettoyage des champs texte (whitespace)
- Parsing des dates
- Création de nouvelles variables (calculs de durée, différences de dates…)

**Join Recipe**
- Jointure des datasets sinistres, vendors et agents
- Left join pour préserver l’exhaustivité
- Analyse des non-correspondances (insight métier : vendors sans clients)

**Group Recipe**
- Agrégations pour produire des **chiffres clés**
- Premières métriques de pilotage

---

### 4️⃣ Visualisation & KPIs
Création d’un **dashboard interactif** dans Dataiku :
- KPIs clés sur les sinistres
- Visualisations dynamiques
- Filtres interactifs
- Publication et export des tableaux de bord

🎯 Objectif : fournir une **vue synthétique et exploitable** pour la prise de décision.

---

## 📈 Résultats & Insights
- Mise en évidence de déséquilibres dans l’attribution des vendors
- Identification de patterns dans les sinistres selon les périodes
- Base fiable et nettoyée pour analyses futures ou outils BI

---

## 💡 Apports du Projet
✔️ Démarche **end-to-end data analytics**  
✔️ Combinaison **Python + Dataiku** (automatisation & visual)  
✔️ Forte **orientation métier assurance**  
✔️ Projet facilement **industrialisable et scalable**

---

## 🔮 Pistes d’Amélioration
- Enrichissement avec des données externes
- Analyse prédictive (probabilité de sinistre, délais de traitement)
- Connexion à Power BI / base SQL pour reporting avancé
- Mise en place de contrôles qualité automatisés

---

## 👤 À propos
Ce projet illustre ma capacité à :
- comprendre un **besoin métier assurance**,
- structurer et nettoyer des données complexes,
- produire des analyses claires et exploitables,
- utiliser **Dataiku et Python** dans un contexte professionnel.

📫 *Ouvert aux opportunités Data Analyst / Data Scientist / Assurance Analytics*
