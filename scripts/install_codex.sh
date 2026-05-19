#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-$HOME/.codex/skills}"
mkdir -p "$TARGET"
cp -R skills/* "$TARGET/"
mkdir -p "$HOME/.codex"
cp AGENTS.md "$HOME/.codex/AGENTS.md" 2>/dev/null || true
echo "Installed skills to $TARGET"
echo "Copied AGENTS.md to $HOME/.codex/AGENTS.md if permitted"
