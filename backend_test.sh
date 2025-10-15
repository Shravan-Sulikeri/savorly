#!/bin/bash
# Quick backend test for Savorly

echo "Starting backend test..."

# 1. Health check
echo "Checking health endpoint:"
curl -s http://127.0.0.1:8000/api/health
echo -e "\n"

# 2. Generate recipes (stub)
echo "Testing generate_recipes endpoint:"
curl -s -X POST http://127.0.0.1:8000/api/generate_recipes \
  -H "Content-Type: application/json" \
  -d '{"pantry_items":["eggs","spinach","rice","yogurt"]}'
echo -e "\nDone!"

