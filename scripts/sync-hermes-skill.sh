#!/usr/bin/env bash
# Sync a project skill from the canonical Claude copy into the active Hermes profile.
# Usage: bash scripts/sync-hermes-skill.sh grill-me
set -euo pipefail

cd "$(dirname "$0")/.."

name="${1:-}"
if [ -z "$name" ]; then
  echo "Usage: $0 <skill-name>" >&2
  exit 2
fi

src=".claude/skills/$name"
if [ ! -d "$src" ]; then
  echo "ERROR: canonical skill not found: $src" >&2
  exit 1
fi

hermes_home="${HERMES_HOME:-$HOME/AppData/Local/hermes}"
dst="$hermes_home/skills/productivity/$name"
mkdir -p "$(dirname "$dst")"
rm -rf "$dst"
cp -R "$src" "$dst"

echo "Synced $name: $src -> $dst"
