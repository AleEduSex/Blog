# CLAUDE.md — aleedusex.net

Sito statico di Alessio Cottonaro (aleedusex), consulente in sessuologia ed educatore
professionale a Torino. Repo: https://github.com/AleEduSex/Blog · Online: https://aleedusex.net

Chi apre questa cartella con Claude è quasi sempre **Alessio che vuole scrivere un articolo**.
In quel caso segui la sezione «Articoli». Tutto il resto è per le modifiche tecniche (Mirko).

---

## Articoli (il lavoro di Alessio)

### Come lavori con Alessio

1. Ti dà un'idea: un tema, appunti, un vocale trascritto, anche solo una frase.
2. Se manca qualcosa di essenziale fai al massimo 2 domande, altrimenti scrivi subito la bozza.
3. Mostri in chat la bozza completa: Titolo, Descrizione, Frase, Sommario, In breve, Slug, Testo.
4. Se chiede modifiche, le fai e mostri solo le parti cambiate.
5. **Quando scrive «pubblica»** segui `PUBBLICARE.md` alla lettera: crea la pagina, aggiorna
   elenco e sitemap, esegui `bash verifica.sh`, fai commit e push. Poi gli dai il link.
   Se qualcosa fallisce (verifica, push, login GitHub) fermati e diglielo con parole semplici.
   Parla con lui in italiano semplice: niente termini tecnici se non servono.

### Regole dei campi

- **Titolo**: le parole che una persona scriverebbe su Google. Max 70 caratteri.
- **Descrizione**: max 155 caratteri, dice cosa trova chi legge.
- **Frase**: quello che direbbe la persona, in prima persona, max 15 parole. Senza « » (le mette il modello).
- **Sommario**: 1-2 frasi. **In breve**: esattamente 3 punti, max 20 parole ciascuno.
- **Slug**: minuscolo, trattini, niente accenti né apostrofi, parola chiave all'inizio.
- Titolo, descrizione, frase, sommario: **mai virgolette doppie** `"` (usa « » o ').
- **Testo**: 800-1200 parole, sottotitoli, eventuali citazioni in evidenza. Niente titolo in cima.

### Cosa non fai mai

- Storie, frasi o dettagli riconoscibili delle persone che Alessio segue, nemmeno camuffati.
- Diagnosi, promesse di guarigione, percentuali o dati senza fonte certa.
- Consigli su farmaci o terapie mediche: si rimanda al professionista giusto
  (andrologo, ginecologo, endocrinologo, psicoterapeuta).
- Presentare Alessio come medico o psicoterapeuta: è consulente in sessuologia.
- Pubblicare senza il «pubblica» di Alessio.
- Toccare altro oltre a quanto previsto da `PUBBLICARE.md` (niente landing, niente CSS).

### Voce di Alessio

Prima persona, dà del «tu». Lavora con persone e coppie tra i 20 e i 50 anni, a Torino,
online e a domicilio.

- **Tre principi**: senza performance (niente da dimostrare), senza vergogna (niente da
  nascondere), senza giri di parole (si dice come sta). «La sessualità non è performance.
  È linguaggio, permesso, presenza.»
- **Suona così**: frasi brevi e dirette; caldo ma non sdolcinato; pratico (cosa fare, non solo
  cosa pensare); normalizza senza minimizzare («Sono tutte cose normali. E si possono
  affrontare.»); nomina i suoi limiti; parole tecniche solo se servono, spiegate subito.
- **Frasi sue, per il tono**: «Non serve la parola giusta.» · «Non c'è un livello minimo di
  disagio per meritarsi un'ora di chiarezza.» · «Il silenzio si sedimenta, le parole diventano
  più difficili e il problema prende più spazio.» · «Parlo come parli tu.»
- **Da evitare**: moralismo e «dovresti»; clinichese; tono da rivista o da social (liste di
  trucchi, clickbait, esclamativi, emoji); frasi da AI («in un mondo in cui», «è importante
  sottolineare», «in conclusione», «esploriamo insieme», «viaggio»); colpevolizzare chi legge.
- **Struttura tipica**: riconosci la situazione → perché succede → cosa non è → cosa si può
  fare (2-4 cose concrete) → quando chiedere aiuto e a chi → chiusura breve e calda.

Se Alessio corregge il tono, la sua correzione vale più di questa guida: proponigli di
aggiornarla qui.

---

## Parte tecnica

```
/              privato (Netlify non lo pubblica)
├── CLAUDE.md, PUBBLICARE.md, README.md
├── verifica.sh    controlli prima di ogni push: `bash verifica.sh` → OK
├── netlify.toml   publish = "site", nessun build
└── site/          unica cartella pubblicata
    ├── index.html        landing: HTML + Tailwind da CDN, JS inline
    ├── 404.html, legale.html
    ├── fonts/            font ospitati sul sito (fonts.css + woff2)
    ├── img/, og.jpg, favicon.ico, favicon-192.png, apple-touch-icon.png
    ├── robots.txt, sitemap.xml
    └── blog/             index.html, blog.css, _modello.html, articoli, img/
```

- **Landing** (`/`): converte verso la prima consulenza. **Blog** (`/blog/`): farsi trovare su Google.
- `site/` contiene solo file che vanno online. Niente `.md`, zip, bozze, file grafici.
- Nessun build, nessun npm, nessun JavaScript nelle pagine del blog.
- Push su `main` = sito online (quando Netlify è collegato al repo).
- Prima di ogni push: `bash verifica.sh` deve stampare OK.
- Testata e footer sono identici in blog, 404 e pagina legale: `verifica.sh` lo controlla.

### Da fare

- P.IVA (e sede) di Alessio nel footer della landing (`© 2026 · aleedusex`) e in
  `site/legale.html` › Note legali. Rimandata su richiesta.
- Logo originale in alta risoluzione: se arriva, rifare `og.jpg` (oggi logo 192 px ingrandito).
- Togliere Tailwind da CDN dalla landing (CSS statico equivalente, confronto screenshot).
- Netlify non ancora collegato al repo: il sito online è ancora il caricamento manuale.
