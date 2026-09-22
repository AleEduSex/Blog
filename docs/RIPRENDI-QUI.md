# Riprendi da qui — 21/09/2026

Stato (22/09/2026): prompt "Correzioni blog" ESEGUITO — commit 90254e9, 1261415, a384725, 6e30f70, 1139765.
Punti 1-4 della sezione "Non funziona" risolti. Il prompt qui sotto resta solo come storico: NON rieseguirlo.
Prossimo passo: sezione "Dopo le correzioni" in fondo.

## Nuovo PC — preparazione

```bash
git clone https://github.com/AleEduSex/Blog.git aleedusex-blog
cd aleedusex-blog
git config user.name "Mirko Galetto"
git config user.email "mirkogaletto@gmail.com"
git config core.autocrlf false
bash verifica.sh
```

`verifica.sh` deve stampare OK. Il primo push aprirà il login GitHub.

## Resoconto verifica

### Funziona (testato)
- Pubblicazione simulata seguendo PUBBLICARE.md: verifica.sh OK, cambiano solo i file attesi
- verifica.sh intercetta errori (articolo sbagliato apposta: 5/5 errori trovati)
- Navigazione: menu mobile/desktop landing → Blog → articolo → "Tutti gli articoli" → wordmark → landing; "Scrivimi" → /#contatti
- 375 px senza scroll orizzontale; zero errori JS; zero 404 del blog
- Tag HTML bilanciati; JSON-LD valido (titoli normali); sitemap XML valida
- noindex su modello ed esempi, assente su articolo reale
- Landing: solo 3 righe aggiunte
- verifica.sh funziona anche su clone Windows con autocrlf=true
- Primo Tab = link "Vai all'articolo"

### Non funziona (confermato)
1. Virgolette doppie " in titolo/descrizione rompono il JSON-LD; verifica.sh non lo rileva
2. Contrasto sotto WCAG AA: data/minuti 3.7:1, disclaimer e didascalie 4.3:1, etichette footer 2.9:1, © footer 3.3:1 (il footer della landing ha lo stesso difetto)
3. verifica.sh non controlla: un solo post-item--lead; esistenza foto di og:image
4. Ponytail: ~12 righe superflue per articolo (twitter:* duplicati, meta author, publisher, bottone grande mai usato, file temporaneo in verifica.sh)

### Non verificabile da qui
- Comportamento Netlify (non collegato): redirect, /blog/ con o senza barra finale, cache
- Indicizzazione reale Google e rich results (solo sintassi verificata)
- Safari/iOS (testato solo Chromium)
- Anteprima social: og.jpg è 192×192 con card grande (difetto preesistente)
- Se il Claude/Cowork di Ale avrà git, credenziali e permesso di push
- Flusso con foto di copertina reale; prestazioni (Lighthouse)

### Rischio di processo
Collegare Netlify prima del primo articolo vero mette online /blog/ con 3 titoli segnaposto.

## Prompt da eseguire

```
SESSIONE — Correzioni blog aleedusex (repo aleedusex-blog)

RUOLO: sviluppatore del progetto. Leggi CLAUDE.md e docs/RIPRENDI-QUI.md prima di iniziare.
SKILL: ponytail ATTIVA (full) — diff più corto possibile, niente refactor, niente file nuovi.
Nessun'altra skill di design. code-review solo alla fine, sul diff.

PERIMETRO — puoi toccare SOLO:
  site/blog/blog.css, site/blog/_modello.html, site/blog/esempio-1.html,
  site/blog/esempio-2.html, site/blog/esempio-3.html, verifica.sh, PUBBLICARE.md
NON toccare mai: site/index.html, site/img/, favicon, og.jpg, robots.txt, sitemap.xml,
  site/blog/index.html. Nessuna nuova dipendenza, nessun build, nessun JS nelle pagine.

PRIMA DI TUTTO
  git status → deve essere pulito. bash verifica.sh → deve stampare OK.
  Se uno dei due fallisce: FERMATI E CHIEDIMI.

CORREZIONI, IN ORDINE (un commit per punto)

1. verifica.sh — virgolette nel JSON-LD
   Nel ciclo del controllo 2 (segnaposto), per ogni file non _modello aggiungi:
     grep -hE '^[[:space:]]*"(headline|description)": ' "$f" | awk -F'"' 'NF!=5{exit 1}' \
       || fail "$f: virgolette doppie in titolo/descrizione rompono il JSON-LD"
   Test: crea per un attimo una copia di esempio-1.html con "headline": "Il "no"",
   verifica.sh deve dare ERRORE; cancella la copia; verifica.sh → OK.

2. verifica.sh — un solo articolo in evidenza + foto og esistente
   - [ "$(grep -c 'post-item--lead' blog/index.html)" = 1 ] || fail "serve esattamente un post-item--lead"
   - per ogni articolo pubblicato: se og:image contiene aleedusex.net/blog/img/, il file
     corrispondente in site/blog/img/ deve esistere, altrimenti fail.
   Controllo 3: sostituisci tee + file in /tmp con
     out=$(…ciclo…); [ -n "$out" ] && { echo "$out"; err=1; }
   Test: verifica.sh → OK.

3. PUBBLICARE.md — una riga al passo 3.2: «Titolo, descrizione e sommario: MAI virgolette
   doppie ", usa « » o ' (rompono i dati per Google).» Nient'altro.

4. blog.css — contrasto AA (valori già calcolati, non cambiare altro):
   .post-meta               rgba(26,26,26,0.55) → 0.7   (3.7 → 5.8:1)
   .disclaimer, figcaption  rgba(26,26,26,0.6)  → 0.7   (4.3 → 5.8:1)
   .site-footer .label      rgba(240,231,213,0.4)  → 0.6  (2.9 → 4.75:1)
   .site-footer .legal      rgba(240,231,213,0.45) → 0.6  (3.3 → 4.75:1)
   Il footer della landing ha lo stesso difetto: NON toccarlo, elencalo solo nell'output.

5. ponytail — tagli (stesse righe in _modello.html E nei 3 esempio-*.html):
   - elimina twitter:title, twitter:description, twitter:image (tieni twitter:card)
   - elimina <meta name="author"> e <meta property="article:author">
   - elimina il blocco "publisher" dal JSON-LD (occhio alla virgola dopo "author": {…})
   - blog.css: .btn-burgundy non usato in grande → sposta i valori di .small nella base,
     elimina le regole .small, togli la classe "small" dall'header delle 5 pagine blog
     (index.html del blog incluso: È L'UNICA eccezione al perimetro, solo quella classe)
   Test: python/json sul JSON-LD dei 3 esempi → valido; verifica.sh → OK.

VERIFICA FINALE
  - bash verifica.sh → OK
  - git diff --stat 0bfec91..HEAD → solo i file del perimetro; site/index.html assente
  - browser a 1280 e 375 px su /blog/ e /blog/esempio-1.html: aspetto invariato
    (salvo testi grigi leggermente più scuri), zero errori console, zero 404 del blog
  - code-review sul diff
  - push su main, confronto hash remoto/locale

FERMATI E CHIEDIMI SE
  - una correzione richiede di toccare site/index.html o un file fuori perimetro
  - verifica.sh fallisce e la causa non è nel diff appena fatto
  - una skill suggerisce modifiche di design oltre ai valori sopra
  - il push chiede credenziali

NON FARE
  - correggere og.jpg, favicon.ico, cdn-cgi, contrasto della landing: solo elencarli
  - collegare Netlify, creare branch, aggiungere file

OUTPUT
  - per ogni punto: commit hash + test eseguito + esito
  - diff --stat finale
  - cose trovate e non toccate
```

## Dopo le correzioni (da fare)
- Parte 2: progetto Claude di Ale + EDITORIALE.md (voce di Alessio) + accesso GitHub
- Far approvare ad Ale il testo introduttivo del blog ("Le domande che si fanno a bassa voce…")
- Collegare Netlify solo con almeno un articolo vero (o togliere prima i 3 link dalla landing)
