#!/usr/bin/env bash
# Apre le pagine di prova nel browser: http://localhost:8766/prove/blog.html
# Usa blog.css e i font veri di site/. Ctrl+C per chiudere.
cd "$(dirname "$0")" || exit 1
qui=$PWD
radice=$(mktemp -d)
ln -s "$qui/../../site/blog"  "$radice/blog"
ln -s "$qui/../../site/fonts" "$radice/fonts"
ln -s "$qui/pagine"           "$radice/prove"
ln -s "$qui/tavole"           "$radice/tavole"
echo "Pagine:  http://localhost:8766/prove/blog.html"
echo "Tavole:  http://localhost:8766/tavole/tavole.html"
cd "$radice" && python3 -m http.server 8766
