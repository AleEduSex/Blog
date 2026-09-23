# Pubblicare un articolo sul blog

Procedura per Claude (progetto di Alessio). Seguila in ordine, senza saltare passi.
Tutto ciò che va online sta in `site/`. Questo file resta privato.

## 0. Regole fisse

- Nulla va online senza il "pubblica" esplicito di Alessio in chat.
- Tocchi SOLO: il nuovo `site/blog/<slug>.html`, `site/blog/index.html`, `site/sitemap.xml`,
  l'eventuale foto in `site/blog/img/`. Mai `site/index.html`, mai `blog.css`, mai altri articoli
  (salvo correzioni richieste, vedi in fondo).
- Niente file di lavoro in `site/` (note, bozze, .md, .docx, zip).
- Testo: voce di Alessio (vedi `EDITORIALE.md` quando esiste). Niente moralismo, niente clinichese,
  niente promesse terapeutiche. Temi medici o psicologici: rimanda al professionista giusto.

## 1. Bozza in chat

Mostra ad Alessio, in chat:

- **Titolo** (contiene la domanda o la parola che la gente cerca su Google)
- **Descrizione** (max 155 caratteri)
- **Frase** (quello che direbbe chi legge, in prima persona, max ~15 parole; apre l'articolo tra « »)
- **Sommario** (1-2 frasi, andrà in corsivo sotto il titolo)
- **In breve** (3 punti chiave, max ~20 parole ciascuno)
- **Slug** (nome del file: minuscolo, trattini, niente accenti, parola chiave in testa;
  es. `calo-del-desiderio-in-coppia`)
- **Testo completo**
- Foto sì/no

Aspetta "pubblica". Se chiede modifiche, rifai questo passo.

### Se ricevi una SCHEDA ARTICOLO (Alessio la scrive nel suo Claude e la manda a Mirko)

La scheda (`=== SCHEDA ARTICOLO === … === FINE SCHEDA ===`) vale già come «pubblica»: salta il passo 1.
Campi → segnaposto: TITOLO → `{{TITOLO}}`, DESCRIZIONE → `{{DESCRIZIONE}}`, FRASE → `{{FRASE}}`,
SOMMARIO → `{{SOMMARIO}}`, IN BREVE (3 righe `- …`) → `{{IN_BREVE}}`, SLUG → `{{SLUG}}`, FOTO → passo 4.
TESTO → `{{CONTENUTO}}`: paragrafi → `<p>`, righe `## …` → `<h2>`, righe `> …` → `<blockquote><p>…</p></blockquote>`,
righe `- …` consecutive → `<ul><li>`. Non cambiare le parole di Alessio: correggi solo refusi evidenti e segnalali.

## 2. Primo articolo vero? Togli i segnaposto

Solo la prima volta: cancella `site/blog/esempio-1.html`, `esempio-2.html`, `esempio-3.html`
e le loro tre voci `<li>` in `site/blog/index.html`.

## 3. Crea la pagina

1. Copia `site/blog/_modello.html` in `site/blog/<slug>.html`.
2. Sostituisci ogni segnaposto (l'elenco è nel commento in testa al modello):
   - `{{DATA_ISO}}` e `{{DATA_MODIFICA_ISO}}`: data di oggi, formato `2026-10-05`
   - `{{DATA_LEGGIBILE}}`: `5 ottobre 2026`
   - `{{FRASE}}`: solo il testo, le « » sono già nel modello
   - `{{IN_BREVE}}`: esattamente 3 righe `        <li>…</li>` (indentate di 8 spazi)
   - `{{MINUTI}}`: parole del testo / 200, arrotondato, minimo 2
   - `{{IMMAGINE_OG}}`: `https://aleedusex.net/blog/img/<slug>.jpg` se c'è la foto,
     altrimenti `https://aleedusex.net/og.jpg`
   - `{{CONTENUTO}}`: il testo in HTML, indentato di 6 spazi. Solo questi tag:
     `<p>` `<h2>` `<h3>` `<blockquote><p>…</p></blockquote>` `<ul><li>` `<ol><li>`
     `<strong>` `<em>` `<a href>` `<hr>` e, per foto nel testo,
     `<figure><img src="/blog/img/…" alt="…" loading="lazy"><figcaption>…</figcaption></figure>`.
     Niente `<h1>` (c'è già il titolo), niente stili inline.
   - Titolo, descrizione e sommario: MAI virgolette doppie `"`, usa « » o ' (rompono i dati per Google).
3. Elimina il commento in testa al file (da `<!--` a `-->` iniziali).
4. Elimina l'intera riga `<!-- RIMUOVERE -->…<!-- /RIMUOVERE -->` (altrimenti Google non la vede).
5. Senza foto: elimina il blocco da `<!-- COPERTINA:` a `<!-- /COPERTINA -->` compresi.

## 4. Foto (solo se c'è)

- Salva come `site/blog/img/<slug>.jpg` (foto nel testo: `<slug>-2.jpg`, `<slug>-3.jpg`…)
- Lato lungo max 1600 px, peso max 300 KB. Se è più grande, ridimensionala prima.
- `alt` descrittivo, in italiano. Niente foto riconoscibili di clienti.

## 5. Aggiungi all'elenco

In `site/blog/index.html`, subito sotto `<!-- NUOVO ARTICOLO QUI … -->`, incolla
(e togli `post-item--lead` dalla voce che prima era in cima):

```html
      <li class="post-item post-item--lead">
        <a href="/blog/SLUG.html">
          <p class="post-meta"><time datetime="2026-10-05">5 ottobre 2026</time><span class="sep">·</span>4 min</p>
          <h2 class="post-title">TITOLO</h2>
          <p class="post-excerpt">SOMMARIO</p>
          <span class="read-more">Leggi <span class="ar" aria-hidden="true">→</span></span>
        </a>
      </li>
```

## 6. Aggiungi alla sitemap

In `site/sitemap.xml`, subito sotto `<!-- NUOVO ARTICOLO QUI -->`:

```xml
  <url><loc>https://aleedusex.net/blog/SLUG.html</loc><lastmod>2026-10-05</lastmod></url>
```

## 7. Verifica

Dalla radice del repository:

```bash
bash verifica.sh
```

Deve stampare `OK`. Se stampa `ERRORE`, correggi e ripeti. Poi `git status`: devono
comparire solo i file del passo 0.

## 8. Pubblica

```bash
git add site
git commit -m "Blog: TITOLO"
git push origin main
```

Conferma ad Alessio con il link `https://aleedusex.net/blog/SLUG.html`
(online dopo 1-2 minuti, quando Netlify è collegato al repository).

## Correggere un articolo già pubblicato

Modifica solo quel file e, se cambia il contenuto, aggiorna `{{DATA_MODIFICA_ISO}}`
(`article:modified_time` e `dateModified`) e `<lastmod>` nella sitemap. Titolo o sommario
cambiati: aggiorna anche la voce in `blog/index.html`. Mai cambiare lo slug di un articolo
già online. Poi passi 7 e 8 con messaggio `Blog: corregge TITOLO`.
