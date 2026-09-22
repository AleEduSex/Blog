#!/usr/bin/env bash
# Controlli del sito prima di ogni push. Uso: bash verifica.sh  (dalla radice del repo)
cd "$(dirname "$0")/site" || exit 1
shopt -s nullglob
err=0
fail() { echo "ERRORE: $*"; err=1; }

# 1. File base
for f in blog/index.html blog/blog.css blog/_modello.html robots.txt sitemap.xml; do
  [ -f "$f" ] || fail "manca site/$f"
done

# 2. Segnaposto non sostituiti
for f in blog/*.html; do
  [ "$f" = blog/_modello.html ] && continue
  grep -q '{{' "$f" 2>/dev/null && fail "$f contiene ancora {{…}}"
  grep -hE '^[[:space:]]*"(headline|description)": ' "$f" | awk -F'"' 'NF!=5{exit 1}' \
    || fail "$f: virgolette doppie in titolo/descrizione rompono il JSON-LD"
done

# 3. Riferimenti locali esistenti (ignora i 404 storici della landing)
out=$(for f in $(find . -name '*.html' ! -name '_*'); do
  dir=$(dirname "$f")
  grep -oE '(href|src)="[^"]*"' "$f" | sed -E 's/^(href|src)="//; s/"$//' | while read -r u; do
    case "$u" in ''|'#'*|http:*|https:*|mailto:*|tel:*|/favicon.ico|/cdn-cgi/*|*"'"*) continue ;; esac
    p=${u%%#*}; p=${p%%\?*}
    case "$p" in /*) t=".$p" ;; *) t="$dir/$p" ;; esac
    case "$t" in */) t="${t}index.html" ;; esac
    [ -e "$t" ] || echo "ERRORE: $f → $u non esiste"
  done
done)
[ -n "$out" ] && { echo "$out"; err=1; }

# 4. Articoli pubblicati: indicizzabili, in elenco, in sitemap
for f in blog/*.html; do
  b=$(basename "$f")
  case "$b" in index.html|_*|esempio-*) continue ;; esac
  grep -q 'noindex' "$f" && fail "$f ha ancora noindex"
  grep -q "href=\"/blog/$b\"" blog/index.html || fail "$b non è nell'elenco blog/index.html"
  grep -q "/blog/$b</loc>" sitemap.xml || fail "$b non è in sitemap.xml"
  og=$(grep -o 'og:image" content="https://aleedusex.net/blog/img/[^"]*' "$f" | sed 's|.*aleedusex.net/||')
  [ -z "$og" ] || [ -f "$og" ] || fail "$b: foto og:image site/$og non esiste"
done
[ "$(grep -c 'class="post-item post-item--lead"' blog/index.html)" = 1 ] || fail "blog/index.html: serve esattamente un post-item--lead"

# 5. Sitemap
if [ -f sitemap.xml ]; then
  [ "$(grep -c '<url>' sitemap.xml)" = "$(grep -c '</url>' sitemap.xml)" ] || fail "sitemap.xml: <url> non bilanciati"
  grep -qE 'esempio-|_modello' sitemap.xml && fail "sitemap.xml contiene segnaposto o modello"
fi

# 6. Nessun file di lavoro dentro site/
w=$(find . -type f \( -iname '*.md' -o -iname '*.zip' -o -iname '*.psd' -o -iname '*.fig' -o -iname '*.docx' \))
[ -n "$w" ] && fail "file di lavoro in site/: $w"

[ $err = 0 ] && echo OK
exit $err
