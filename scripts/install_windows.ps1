param(
  [string]$ClaudeTarget = "$HOME/.claude/skills",
  [string]$CodexTarget = "$HOME/.codex/skills"
)
New-Item -ItemType Directory -Force -Path $ClaudeTarget | Out-Null
New-Item -ItemType Directory -Force -Path $CodexTarget | Out-Null
Copy-Item -Recurse -Force skills/* $ClaudeTarget
Copy-Item -Recurse -Force skills/* $CodexTarget
New-Item -ItemType Directory -Force -Path "$HOME/.codex" | Out-Null
Copy-Item -Force AGENTS.md "$HOME/.codex/AGENTS.md"
Write-Host "Installed skills for Claude and Codex."
