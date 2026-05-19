#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-$PWD}"
cp GEMINI.md "$TARGET/GEMINI.md"
mkdir -p "$TARGET/ai-skills"
cp -R skills/* "$TARGET/ai-skills/"
echo "Installed Gemini context to $TARGET/GEMINI.md and skills to $TARGET/ai-skills"
