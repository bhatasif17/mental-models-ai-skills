#!/usr/bin/env bash
set -euo pipefail
bash scripts/install_claude.sh
bash scripts/install_codex.sh
bash scripts/install_gemini.sh "$PWD"
echo "All install scripts completed."
