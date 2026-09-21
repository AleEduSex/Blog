# CLAUDE.md — aleedusex.net

Sito statico di Alessio Cottonaro (aleedusex), consulente in sessuologia a Torino.
Repo: https://github.com/AleEduSex/Blog · Online: https://aleedusex.net

## Struttura

```
/            ← privato: config e documenti di lavoro (Netlify non lo pubblica)
├── netlify.toml   publish = "site", nessun build
└── site/          ← unica cartella pubblicata
    ├── index.html     HTML + Tailwind da CDN, JS inline
    ├── favicon-192.png, og.jpg
    └── img/
```

## Regole

- `site/` contiene solo file che vanno online. Mai `.md`, zip, bozze, file grafici.
- Documenti di lavoro, note, prezzi interni: solo nella radice o fuori dal repo.
- Nessun build step, nessun npm, nessuna dipendenza.
- Push su `main` = sito online (quando Netlify sarà collegato). Ogni modifica a `site/` è una modifica al sito.
- Niente modifiche a `site/` senza richiesta esplicita.

## Stato noto

- Import iniziale (commit 6eb8d9a): copia byte per byte del deploy online al 21/09/2026.
- `index.html` cita `/favicon.ico` e `/cdn-cgi/.../email-decode.min.js` (aggiunta Cloudflare
  presente nella versione pubblicata): entrambi 404 online. Lasciati così di proposito.
- Netlify non ancora collegato al repo: il sito online è ancora il caricamento manuale.
