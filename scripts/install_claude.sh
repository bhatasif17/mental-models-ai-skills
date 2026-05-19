#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-$HOME/.claude/skills}"
mkdir -p "$TARGET"
cp -R skills/* "$TARGET/"
echo "Installed skills to $TARGET"
