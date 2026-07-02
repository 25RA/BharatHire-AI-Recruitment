# BharatHire
### AI-Powered Explainable Recruitment Intelligence Platform

<p align="center">

AI Recruitment • Semantic Candidate Ranking • Explainable AI • Recruiter Analytics • Hybrid Scoring Engine

</p>

---

# Overview

Hiring the right candidate has become increasingly challenging as recruiters must evaluate hundreds or even thousands of resumes for a single job opening. Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, often overlooking strong candidates whose experience or skills are expressed differently.

BharatHire is an intelligent AI recruitment platform designed to automate candidate screening using semantic understanding, hybrid ranking algorithms, explainable artificial intelligence, and recruiter-centric analytics.

Instead of ranking resumes based solely on keywords, BharatHire evaluates multiple dimensions of every candidate including skills, experience, career progression, behavioural attributes, industry relevance, recruiter assessments, and overall confidence to generate transparent and reliable hiring recommendations.

The platform combines multiple AI engines into a unified recruitment intelligence system capable of processing large candidate datasets while providing meaningful explanations for every recommendation.

---

# Problem Statement

Modern recruitment pipelines suffer from several limitations:

- Manual resume screening is slow and expensive.
- Keyword-based ATS systems miss highly qualified candidates.
- Hiring decisions often lack transparency.
- Recruiters receive limited analytical insights.
- Candidate evaluation varies between recruiters.
- Large datasets become difficult to manage efficiently.

These issues increase hiring time, reduce candidate quality, and introduce unconscious bias into recruitment decisions.

---

# Our Solution

BharatHire addresses these challenges through a multi-engine AI recruitment pipeline.

The platform:

- understands resumes semantically rather than matching keywords
- evaluates candidates across multiple independent scoring engines
- generates explainable recommendations
- ranks candidates using hybrid weighted scoring
- provides recruiter dashboards and hiring analytics
- visualizes recruitment trends
- enables faster and more transparent hiring decisions

---

# Key Features

## Intelligent Resume Processing

- Resume Parsing
- Candidate Profile Extraction
- Experience Analysis
- Skill Identification
- Education Recognition
- Behaviour Indicators
- Industry Classification

---

## Hybrid AI Ranking Engine

Each candidate is evaluated using multiple AI engines:

- Skill Matching Engine
- Experience Engine
- Career Progression Engine
- Behaviour Engine
- Industry Matching Engine
- Recruiter Assessment Engine
- Risk Analysis Engine

These independent scores are normalized and combined into a final recommendation score.

---

## Explainable AI

Unlike traditional ATS systems, BharatHire explains every recommendation.

Each ranked candidate includes:

- strengths
- weaknesses
- missing skills
- confidence score
- recommendation category
- reasoning behind ranking

This allows recruiters to trust AI-generated decisions.

---

## Analytics Dashboard

Interactive dashboards provide:

- Total Candidates Processed
- Average Candidate Score
- AI Confidence
- Recommendation Distribution
- Component-wise Score Analysis
- Hiring Insights
- Recruitment Statistics
- Performance Metrics

---

## Candidate Intelligence

Individual candidate profiles include:

- Final Score
- Recommendation
- Confidence
- Experience Analysis
- Behaviour Analysis
- Career Growth
- Skill Breakdown
- AI Explanation

---

## Leaderboard

Automatically ranks candidates according to:

- Final AI Score
- Confidence
- Recommendation Category
- Overall Hiring Priority

---

# System Architecture

```
                   Job Description
                          │
                          ▼
                Requirement Extraction
                          │
                          ▼
                Candidate Processing
                          │
        ┌────────────────────────────────┐
        │                                │
        ▼                                ▼
 Skill Engine                 Experience Engine
        │                                │
        ▼                                ▼
 Behaviour Engine            Career Engine
        │                                │
        ▼                                ▼
 Industry Engine            Assessment Engine
        │                                │
        └──────────────┬─────────────────┘
                       ▼
                Hybrid Ranker
                       ▼
              Explainability Engine
                       ▼
      Dashboard • Leaderboard • Reports
```

---

# Technology Stack

## Backend

- Python
- FastAPI

## Frontend

- HTML5
- CSS3
- JavaScript

## AI & NLP

- Sentence Transformers
- Semantic Embeddings
- Hybrid Ranking
- Explainable AI

## Data Processing

- Pandas
- NumPy

## Visualization

- Chart.js

---

# Project Structure

```
BharatHire
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── app.py
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── dashboard.html
│   ├── candidate.html
│   └── index.html
│
├── engines/
│   ├── candidate_engine/
│   ├── recruiter_engine/
│   ├── explainability_engine/
│   ├── jd_engine/
│   └── scoring_engine/
│
├── preprocessing/
├── ranking/
├── evaluation/
├── explainability/
├── scripts/
├── outputs/
├── configs/
├── tests/
└── utils/
```

---

# AI Pipeline

```
Job Description
        │
        ▼
JD Parser
        │
        ▼
Candidate Loader
        │
        ▼
Feature Extraction
        │
        ▼
Multiple AI Engines
        │
        ▼
Hybrid Ranking
        │
        ▼
Recommendation
        │
        ▼
Explainability
        │
        ▼
Dashboard & Reports
```

---

# Recommendation Categories

Candidates are classified into:

- Elite Match
- Strong Shortlist
- Shortlist
- Needs Manual Review
- Not Recommended

---

# Dashboard Modules

- Recruitment Dashboard
- Candidate Search
- KPI Cards
- Analytics
- Recommendation Distribution
- AI Confidence
- Candidate Leaderboard
- Hiring Insights
- Notifications
- System Status

---

# Explainability

Every recommendation includes:

- Overall AI Score
- Confidence Score
- Matching Skills
- Missing Skills
- Career Analysis
- Behaviour Analysis
- Recruiter Signals
- Final Explanation

This makes hiring decisions transparent and interpretable.

---

# Outputs

The platform generates:

- Ranked Candidate List
- Leaderboard
- Analytics Dashboard
- Candidate Reports
- Recommendation Categories
- Performance Metrics

---

# Installation

Clone the repository

```bash
git clone https://github.com/25RA/BharatHire-AI-Recruitment.git
```

Move into the project

```bash
cd BharatHire-AI-Recruitment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the backend

```bash
python main.py
```

Launch the frontend

Open

```
frontend/index.html
```

in your browser.

---

# Future Enhancements

- Large Language Model based interview assistant
- Resume summarization using Generative AI
- Voice interview evaluation
- AI recruiter chatbot
- Bias detection module
- Live recruiter collaboration
- Multi-language resume understanding
- Cloud deployment with scalable APIs

---

# Vision

BharatHire aims to redefine recruitment by combining explainable artificial intelligence, semantic understanding, and intelligent analytics into a single platform that empowers recruiters to make faster, fairer, and more informed hiring decisions.

---

# License

This repository is intended for educational, research, and demonstration purposes.
