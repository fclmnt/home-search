#!/bin/zsh
# Recherche d'appartements — lancé par launchd à 8h et 17h
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

cd "$HOME/home-search" || exit 1
mkdir -p logs

LOG="logs/run-$(date +%Y%m%d-%H%M).log"
{
  echo "=== Recherche démarrée : $(date) ==="
  claude -p "$(cat criteres.md)" \
    --model sonnet \
    --allowedTools "WebSearch,WebFetch,Read,Write,Edit,Glob,Grep,Bash(python3:*)"
  echo "=== Recherche terminée : $(date) (code $?) ==="
  # Filet de sécurité : régénérer photos, Excel et site même si l'agent a oublié
  python3 scripts/fetch_photos.py
  python3 scripts/make_xlsx.py
  python3 scripts/make_site.py
  echo "=== Sorties régénérées : $(date) ==="
} >> "$LOG" 2>&1

# Garder seulement les 30 derniers logs
ls -t logs/run-*.log 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null
exit 0
