# Savorly
Zero-waste, mood-smart recipes from what you already have.

## Apps
- frontend/ — Next.js + Tailwind UI (dev: http://localhost:3000)
- backend/  — FastAPI API (dev: http://127.0.0.1:8000)

## Dev
1) Backend:
   cd backend && source .venv/bin/activate && uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
2) Frontend:
   cd frontend && npm run dev
