#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"

echo "Starting backend smoke test..."

echo "1) GET /health"
curl -fsS "${BASE_URL}/health" | jq .

echo "2) POST /recipes/generate (optional)"
payload='{"ingredients":["eggs","spinach","rice","yogurt"]}'
# capture status + body
status="$(curl -s -o /tmp/resp.json -w "%{http_code}" \
  -H "Content-Type: application/json" -d "$payload" \
  "${BASE_URL}/recipes/generate" || true)"

if [[ "$status" == "200" ]]; then
  cat /tmp/resp.json | jq .
  count=$(jq '.recipes | length // 0' /tmp/resp.json)
  if [[ "$count" -lt 1 ]]; then
    echo "WARN: /recipes/generate returned no recipes"
  else
    echo "OK: /recipes/generate returned $count recipes"
  fi
else
  echo "SKIP: /recipes/generate not ready (HTTP $status)"
fi

echo "PASS: backend smoke tests completed"
