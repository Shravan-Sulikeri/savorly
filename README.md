# Savorly — AI-Powered Zero-Waste Recipe Assistant

[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Frontend-Next.js-000000?logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![TailwindCSS](https://img.shields.io/badge/UI-TailwindCSS-38b2ac?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> “Use what you have. Eat smarter. Waste less.”  
> Built with modern AI and data-driven nutrition science.

---

## Overview

**Savorly** is an intelligent kitchen assistant that transforms your leftovers into balanced, mood-boosting meals.  
You type what’s in your fridge (or scan a receipt/photo), and the app recommends recipes that:

- **Minimize waste** — prioritize near-expiry ingredients  
- **Support your mood** — based on PANAS psychological scale + evidence-backed foods  
- **Stay nutrient-dense** — powered by USDA FoodData Central API  

---

##System Architecture

A clear, modular design — optimized for full-stack AI applications.

```text
                          ┌──────────────────────────────────────┐
                          │              Frontend                │
                          │   Next.js 14 + TailwindCSS (Vercel)  │
                          │                                      │
                          │ - Pantry input (text / photo)        │
                          │ - Mood check (PANAS mini)            │
                          │ - Recipe display & scoring            │
                          └──────────────┬───────────────────────┘
                                         │  REST API Calls
                                         ▼
                          ┌──────────────────────────────────────┐
                          │               Backend                │
                          │       FastAPI + Pydantic v2          │
                          │                                      │
                          │  /api/health → system check           │
                          │  /api/generate_recipes → recipe stub  │
                          │  (future) /api/nutrients → USDA FDC   │
                          │  (future) /api/score_mood → PANAS KB  │
                          └──────────────┬───────────────────────┘
                                         │  Async data / model access
                                         ▼
        ┌────────────────────────────────────────────────────────────────────┐
        │                          Data Layer                                │
        │   Supabase (Postgres + Auth) + USDA FoodData Central (API/Cache)   │
        │   - pantry_items, recipes, nutrients, mood_checks                  │
        └────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
                        ┌──────────────────────────────────────┐
                        │              AI Layer                │
                        │   Hugging Face (Mistral / Llama3)    │
                        │   Donut OCR / Tesseract (vision)     │
                        │   Knowledge base YAML (mood ↔ food)  │
                        └──────────────────────────────────────┘
```
## Tech Stack

| Layer | Technology | Purpose |
|:------|:------------|:---------|
| **Frontend** | [![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=nextdotjs&logoColor=white)](https://nextjs.org/) [![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)](https://react.dev/) [![TailwindCSS](https://img.shields.io/badge/TailwindCSS-38B2AC?style=flat&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/) [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/) | Modern UI with responsive design, static optimization, and strong type safety |
| **State / API** | [![TanStack Query](https://img.shields.io/badge/TanStack_Query-FF4154?style=flat&logo=reactquery&logoColor=white)](https://tanstack.com/query/latest) [![Axios](https://img.shields.io/badge/Axios-5A29E4?style=flat&logo=axios&logoColor=white)](https://axios-http.com/) | Data fetching, client-side caching, and backend integration |
| **Backend** | [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) [![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-FFB300?style=flat&logo=python&logoColor=white)](https://www.uvicorn.org/) | High-performance REST API with async capabilities and data validation |
| **Database / Auth** | [![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat&logo=supabase&logoColor=white)](https://supabase.com/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/) | Managed Postgres database with built-in authentication and storage |
| **AI / ML Layer** | [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black)](https://huggingface.co/) [![Mistral](https://img.shields.io/badge/Mistral_AI-000000?style=flat&logoColor=white)](https://mistral.ai/) [![Llama 3](https://img.shields.io/badge/Meta_Llama_3-0466C8?style=flat&logo=meta&logoColor=white)](https://ai.meta.com/llama/) [![Tesseract OCR](https://img.shields.io/badge/Tesseract_OCR-4285F4?style=flat&logo=google&logoColor=white)](https://github.com/tesseract-ocr/tesseract) | Model inference, text understanding, and vision-based input parsing |
| **Data Sources** | [![USDA FDC](https://img.shields.io/badge/USDA_FoodData_Central-7A0019?style=flat)](https://fdc.nal.usda.gov/) [![PANAS](https://img.shields.io/badge/PANAS_Scale-555555?style=flat)]() | Nutritional datasets and psychology-based mood scaling |
| **DevOps / Deployment** | [![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)](https://vercel.com/) [![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white)](https://render.com/) [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)](https://github.com/features/actions) [![Hugging Face Spaces](https://img.shields.io/badge/HF_Spaces-FFD21E?style=flat&logo=huggingface&logoColor=black)](https://huggingface.co/spaces) | CI/CD automation and deployment for both frontend and backend |
| **Testing / QA** | [![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/) [![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=microsoftedge&logoColor=white)](https://playwright.dev/) | Backend unit testing and frontend integration testing (planned) |

---
## Project Progress

| Phase | Milestone | Description | Status |
|:------|:-----------|:-------------|:--------|
| 0 | Repository Scaffold | Folder structure, FastAPI + Next.js boilerplate, GitHub setup | ✅ Complete |
| 1 | API Health + Stub Generator | Functional `/api/health` and `/api/generate_recipes` endpoints | ✅ Complete |
| 2 | Nutrient Grounding | Connect pantry items to USDA FoodData Central and cache nutrient vectors | 🟡 In Progress |
| 3 | Mood Scoring Engine | Integrate PANAS model and evidence-based mood→food scoring | ⏳ Planned |
| 4 | Vision & OCR | Receipt and fridge image recognition using Donut / Tesseract | ⏳ Planned |
| 5 | Expiry Intelligence | Ingredient shelf-life estimation and zero-waste optimization | ⏳ Planned |
| 6 | Shareable Insights | Generate visual "Mood Plate" cards and export to social / meal planners | ⏳ Planned |

---

## Key Features

- **AI Recipe Generation** using lightweight LLMs hosted via Hugging Face  
- **Zero-Waste Optimization** based on expiry prediction and pantry utilization  
- **Mood-Smart Scoring** grounded in validated psychological research (PANAS, SMILES trial, etc.)  
- **Explainable Recommendations** — users can view which ingredients contributed to each mood score  
- **Extensible API Layer** — modular endpoints for easy integration with nutrition or grocery APIs  
- **Secure Data Layer** — built on Supabase for authentication, storage, and SQL persistence  

---

## Research Basis

- *USDA FoodData Central* — Nutrient composition dataset (API + bulk dump)  
- *PANAS (Positive and Negative Affect Schedule)* — Psychological mood scale used in affective computing  
- *HELFIMED & SMILES Trials* — RCTs demonstrating diet–mood correlations  
- *Cochrane Review (2023)* — Evidence on omega-3 and depression outcomes  
- *Open Food Facts* — Supplementary ingredient/product metadata  

---

## License

MIT License © 2025 [Shravan Sulikeri](https://github.com/Shravan-Sulikeri)

---

## Repository Stats

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Shravan-Sulikeri/savorly)
![GitHub last commit](https://img.shields.io/github/last-commit/Shravan-Sulikeri/savorly)
![GitHub repo size](https://img.shields.io/github/repo-size/Shravan-Sulikeri/savorly)
![GitHub contributors](https://img.shields.io/github/contributors/Shravan-Sulikeri/savorly)

---



## API quickstart (local)

```bash
# health
BASE_URL=http://127.0.0.1:8000 ./scripts/curl/health.sh

# generate recipes (will 404 until endpoint is implemented)
BASE_URL=http://127.0.0.1:8000 ./scripts/curl/recipes_generate.sh
## 4) Commit
```bash
git add shared/types.ts scripts/curl README.md
git commit -m "chore: add shared API types and curl samples"
git push
