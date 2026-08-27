#!/bin/zsh
# Recherche d'appartements — lancé par launchd à 8h et 17h
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

cd "$HOME/home-search" || exit 1
mkdir -p logs

LOG="logs/run-$(date +%Y%m%d-%H%M).log"
{
  echo "=== Recherche démarrée : $(date) ==="
  # Se synchroniser avec le dépôt distant avant de générer quoi que ce soit,
  # sinon un commit poussé ailleurs (ex. GitHub web) fait diverger la branche
  # et tous les push suivants sont rejetés.
  if ! git pull --rebase --autostash -q; then
    git rebase --abort 2>/dev/null
    echo "!!! ÉCHEC git pull --rebase : conflit avec le dépôt distant, intervention manuelle requise"
  fi
  # Scraper Marketplace (session Facebook dédiée) — non bloquant en cas d'échec
  python3 scripts/fetch_marketplace.py || echo "Marketplace ignoré (voir message ci-dessus)"
  claude -p "$(cat criteres.md)" \
    --model sonnet \
    --allowedTools "WebSearch,WebFetch,Read,Write,Edit,Glob,Grep,Bash(python3:*)"
  echo "=== Recherche terminée : $(date) (code $?) ==="
  # Retirer les annonces expirées (garde-fou intégré : n'efface rien si >50% semblent mortes)
  python3 scripts/check_links.py
  # Filet de sécurité : régénérer photos, Excel et site même si l'agent a oublié
  python3 scripts/fetch_photos.py
  python3 scripts/make_xlsx.py
  python3 scripts/make_site.py
  echo "=== Sorties régénérées : $(date) ==="
  # Publier sur GitHub Pages
  git add -A
  if ! git diff --cached --quiet; then
    git commit -m "Mise à jour des annonces — $(date '+%Y-%m-%d %H:%M')" -q
    if git push -q; then
      echo "=== Publié sur GitHub Pages : $(date) ==="
    else
      echo "!!! ÉCHEC du push : $(date) — commit local conservé, site NON mis à jour"
    fi
  else
    echo "=== Aucun changement à publier ==="
  fi
} >> "$LOG" 2>&1

# Garder seulement les 30 derniers logs
ls -t logs/run-*.log 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null
exit 0
