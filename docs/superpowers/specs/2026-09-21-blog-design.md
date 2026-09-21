# Blog aleedusex.net — Design

Data: 2026-09-21 · Stato: approvato da Mirko

## Obiettivo

Aggiungere un blog al sito statico aleedusex.net. Due pagine, due intenti, stesso posto:

- **Landing** (`/`): converte → prima consulenza 60 €. Non cambia, salvo il link "Blog".
- **Blog** (`/blog/`): farsi trovare su Google con articoli che rispondono alle domande
  che le persone cercano. Accompagna con discrezione verso la consulenza.

Pubblicazione futura: Ale, tramite il suo progetto Claude/Cowork. Ale legge il testo in
chat, dice "pubblica", Claude pubblica (commit + push su `main`). Il blog deve quindi
essere regolare e prevedibile per un'AI: un modello, segnaposto espliciti, procedura scritta.

## Decisioni

| Tema | Scelta |
|---|---|
| Architettura | Un file HTML statico per articolo, da modello. Niente build, niente npm, niente JS |
| Stile | CSS scritto a mano in `site/blog/blog.css`, stessi token della landing. Niente Tailwind CDN sul blog |
| Nome | "Blog" (menu, testata) · URL `/blog/` |
| Categorie | Nessuna. Elenco cronologico, più recente in alto |
| Immagini | Facoltative: copertina e/o immagini nel testo, se Ale le fornisce |
| Invito alla consulenza | Solo a fine articolo, box bordeaux |
| Presenza nella landing | Voce "Blog" in menu desktop, menu mobile, footer "Indice". Nient'altro |
| Contenuti iniziali | 3 articoli segnaposto, `noindex`, fuori dalla sitemap, da cancellare al primo articolo vero |

## File

```
site/
├── index.html          + 3 link "Blog" (unica modifica)
├── robots.txt          nuovo
├── sitemap.xml         nuovo: /, /blog/, articoli reali
└── blog/
    ├── index.html      elenco
    ├── blog.css        stile condiviso
    ├── _modello.html   modello articolo (noindex, Disallow in robots)
    ├── esempio-1.html  segnaposto (noindex)
    ├── esempio-2.html
    ├── esempio-3.html
    └── img/            foto articoli (vuota all'inizio, con .gitkeep)
PUBBLICARE.md           radice, privato: procedura per Claude
CLAUDE.md               aggiornato con le regole del blog
```

URL degli articoli: `/blog/<slug>.html` (link espliciti con `.html`: funzionano ovunque,
anche in locale).

## Token di stile (dalla landing)

- Colori: cream `#F0E7D5`, paper `#F8F1E0`, burgundy `#7A1E2B`, burgundy-deep `#5C1520`,
  ink `#1A1A1A`, line `rgba(122,30,43,0.30)`
- Font: DM Serif Display (titoli, corsivi bordeaux), Source Serif 4 (testo). Google Fonts,
  stesso URL della landing
- Componenti ripresi: `btn-burgundy` (con cerchio freccia), `btn-cream-on-burgundy`,
  `num-eyebrow`, `drop-cap`, header sticky crema con blur e bordo `line`, footer
  burgundy-deep. Raggi piccoli (2–3 px), ombre morbide calde
- `prefers-reduced-motion` rispettato; nessuna animazione d'ingresso sul blog

## Pagina elenco `/blog/`

1. **Header**: wordmark `aleedusex` → `/` · link "Blog" (attivo, `aria-current="page"`) ·
   "Chi sono" → `/#chi-sono` · bottone "Scrivimi" → `/#contatti`. Su mobile tutto in una
   riga, niente hamburger ("Chi sono" nascosto sotto 480 px)
2. **Apertura**: eyebrow "Blog" (num-eyebrow), H1 DM Serif, una riga di presentazione.
   Testi proposti, modificabili da Ale
3. **Elenco** editoriale, non griglia: per voce → data · minuti di lettura, titolo
   (link), estratto, "Leggi →". Separatori filetto `line`. Prima voce più grande.
   Marcatore `<!-- NUOVO ARTICOLO QUI -->` in cima alla lista
4. **Footer**: come la landing (identità, Indice con link a `/#…` + Blog, Dove trovarmi,
   strip legale)

## Pagina articolo

1. Header come sopra
2. Briciola "Blog /" → `/blog/`
3. Data (`<time datetime>`) · minuti di lettura
4. H1 titolo, sommario in corsivo
5. Copertina facoltativa (`<figure>` + didascalia), rimovibile come blocco marcato
6. Corpo: colonna ~68ch, 19 px mobile / 20 px desktop, interlinea 1.7. Primo paragrafo con
   capolettera. Stili per `h2`, `h3`, `p`, `blockquote` (filetto bordeaux), `ul`, `ol`,
   `strong`, `em`, `a`, `figure`/`figcaption`, `hr`
7. Box autore: Alessio Cottonaro · Consulente in sessuologia · Educatore professionale ·
   link `/#chi-sono`
8. Nota: "Questo articolo ha uno scopo informativo e non sostituisce una consulenza
   personale."
9. Box CTA bordeaux: "Ne vuoi parlare?" · Prima consulenza 60 € · 60 min · WhatsApp
   (`https://wa.me/393273003855`) · email (`mailto:alessio.edu.sex@gmail.com`) · "I primi 15
   minuti te li regalo io"
10. "← Tutti gli articoli"
11. Footer come l'elenco

## SEO per pagina

- `<html lang="it">`, charset, viewport, `theme-color #F0E7D5`
- `<title>`: `{{TITOLO}} — Alessio Cottonaro, consulente in sessuologia`
- `meta description`, `link canonical` assoluto `https://aleedusex.net/blog/{{SLUG}}.html`
- Open Graph (`og:type article`, title, description, url, image, locale `it_IT`,
  site_name) + Twitter card. Immagine: copertina se presente, altrimenti
  `https://aleedusex.net/og.jpg`
- JSON-LD `BlogPosting`: headline, description, datePublished, dateModified, author
  (Person, Alessio Cottonaro, url `https://aleedusex.net/`), publisher, mainEntityOfPage,
  image, inLanguage `it-IT`
- Favicon: solo `/favicon-192.png` (niente riferimento a `favicon.ico`, che non esiste)
- Segnaposto e modello: `<meta name="robots" content="noindex, nofollow">`

## Modello `_modello.html`

Segnaposto in maiuscolo tra doppie graffe, elencati in testa al file in un commento:
`{{TITOLO}}`, `{{DESCRIZIONE}}`, `{{SOMMARIO}}`, `{{SLUG}}`, `{{DATA_ISO}}`,
`{{DATA_LEGGIBILE}}`, `{{DATA_MODIFICA_ISO}}`, `{{MINUTI}}`, `{{IMMAGINE_OG}}`,
`{{CONTENUTO}}`. Blocco copertina delimitato da `<!-- COPERTINA INIZIO/FINE -->` da
eliminare se non c'è foto. Riga `noindex` delimitata da `<!-- RIMUOVERE -->`.

Controllo meccanico dopo la compilazione: nessuna occorrenza di `{{` nel file.

## Procedura `PUBBLICARE.md`

1. Ale manda idea/testo (ed eventuale foto)
2. Claude scrive/sistema il testo e lo mostra in chat: titolo, descrizione (≤155 caratteri),
   slug, testo. Aspetta "pubblica"
3. Copia `_modello.html` → `<slug>.html`, sostituisce tutti i segnaposto, rimuove `noindex`
4. Foto (se c'è): in `site/blog/img/<slug>.jpg`, lato lungo ≤1600 px, ≤300 KB
5. Aggiunge la voce in `blog/index.html` sotto `<!-- NUOVO ARTICOLO QUI -->`
6. Aggiunge `<url>` in `sitemap.xml` sotto il marcatore
7. Al primo articolo vero: cancella `esempio-*.html` e le loro voci nell'elenco
8. Verifiche: nessun `{{`; link interni esistenti; nessun file toccato fuori da quelli sopra
9. Commit `Blog: <titolo>` + push su `main`

Regole: slug minuscolo, trattini, niente accenti, parola chiave in testa. Mai toccare
`site/index.html` né altri articoli (salvo correzioni richieste; in quel caso aggiornare
`DATA_MODIFICA_ISO`).

## Modifica alla landing

Solo 3 righe aggiunte, nessuna modificata:
- menu desktop: `<li><a href="/blog/" class="nav-desktop-link hover:text-brand-burgundy">Blog</a></li>` dopo FAQ
- menu mobile: voce "Blog" dopo FAQ, stesse classi delle altre
- footer Indice: voce "Blog" dopo FAQ

Verifica: `git diff --stat site/index.html` = 3 inserimenti, 0 cancellazioni.

## Verifica finale

- Browser integrato: `/blog/`, un articolo, landing — desktop e 375 px
- Console senza errori, nessun 404 sulle risorse delle nuove pagine
- Nessun riferimento relativo rotto; `robots.txt` e `sitemap.xml` validi
- Link "Blog" funzionanti dalla landing

## Fuori scope

Categorie, ricerca, RSS, commenti, newsletter, sezione "Dal blog" nella landing,
correzione dei 404 esistenti della landing, progetto Claude di Ale ed `EDITORIALE.md`
(parte 2), collegamento Netlify.
