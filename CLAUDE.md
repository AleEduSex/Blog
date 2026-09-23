# CLAUDE.md — aleedusex.net

Sito statico di Alessio Cottonaro (aleedusex), consulente in sessuologia a Torino.
Repo: https://github.com/AleEduSex/Blog · Online: https://aleedusex.net

## Struttura

```
/            ← privato: config e documenti di lavoro (Netlify non lo pubblica)
├── netlify.toml   publish = "site", nessun build
├── verifica.sh    controlli prima di ogni push: `bash verifica.sh` → OK
├── PUBBLICARE.md  procedura per pubblicare un articolo
├── docs/          spec e piani
└── site/          ← unica cartella pubblicata
    ├── index.html     landing: HTML + Tailwind da CDN, JS inline
    ├── favicon-192.png, og.jpg, img/
    ├── robots.txt, sitemap.xml
    └── blog/
        ├── index.html     elenco articoli
        ├── blog.css       stile del blog (stessi token della landing, niente Tailwind)
        ├── _modello.html  modello articolo (noindex)
        ├── esempio-*.html segnaposto, da cancellare al primo articolo vero
        └── img/           foto degli articoli
```

## Due pagine, due intenti

- **Landing** (`/`): converte verso la prima consulenza. Non si tocca per pubblicare articoli.
- **Blog** (`/blog/`): farsi trovare su Google. Un file HTML statico per articolo, niente JS.
  Per pubblicare segui `PUBBLICARE.md` alla lettera.

## Regole

- `site/` contiene solo file che vanno online. Mai `.md`, zip, bozze, file grafici.
- Documenti di lavoro, note, prezzi interni: solo nella radice o fuori dal repo.
- Nessun build step, nessun npm, nessuna dipendenza.
- Push su `main` = sito online (quando Netlify sarà collegato). Ogni modifica a `site/` è una modifica al sito.
- Niente modifiche a `site/` senza richiesta esplicita.
- Prima di ogni push: `bash verifica.sh` deve stampare OK.

## Stato noto

- Import iniziale (commit 6eb8d9a): copia byte per byte del deploy online al 21/09/2026.
- Fase 1 di PIANO_MIGLIORAMENTO.md fatta (23/09/2026): niente più 404 in landing, `site/404.html` aggiunta.
- Da fare: P.IVA (e sede) di Ale nel footer della landing (`© 2026 · aleedusex`) e in `site/legale.html` › Note legali. Rimandata su richiesta.
- Netlify non ancora collegato al repo: il sito online è ancora il caricamento manuale.
