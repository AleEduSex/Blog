#!/usr/bin/env bash
# Rigenera il sito pubblicato (site/) da sorgente/ e sezioni.py. Non si modifica mai site/ a mano.
set -euo pipefail
cd "$(dirname "$0")"
python3 prototipi/NON-TOCCARE/generatore/anteprima.py site
echo "site/ rigenerato"
