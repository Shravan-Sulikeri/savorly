import importlib

def test_fastapi_app_imports():
    mod = importlib.import_module("src.app")
    assert getattr(mod, "app", None) is not None
