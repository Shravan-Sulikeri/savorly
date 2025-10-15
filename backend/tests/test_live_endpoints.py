import os, httpx, pytest
BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8000")

@pytest.mark.integration
def test_health_live():
    r = httpx.get(f"{BASE_URL}/health", timeout=5.0)
    r.raise_for_status()
    assert r.json().get("status") == "ok"
