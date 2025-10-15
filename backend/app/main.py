from fastapi import FastAPI

app = FastAPI(title="Savorly API", version="0.0.1")

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "savorly-backend"}
