#!/usr/bin/env bash
set -euo pipefail
BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"
curl -fsS -H "Content-Type: application/json" \
  -d '{"ingredients":["eggs","spinach","rice","yogurt"]}' \
  "$BASE_URL/recipes/generate" | jq .
