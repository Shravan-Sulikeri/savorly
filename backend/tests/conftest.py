import os, sys
# Add the project root (backend/) to sys.path so `import src.*` works in tests
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
