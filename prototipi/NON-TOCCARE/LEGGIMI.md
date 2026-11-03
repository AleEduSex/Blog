# Prototipo: blog diviso per temi — NON TOCCARE

Prove del redesign di `/blog/` (novembre 2026). **Niente di questa cartella va online**:
Netlify pubblica solo `site/`. Non modificare questi file e non usarli come modello per gli
articoli. Servono a Mirko e Alessio per decidere; quando la proposta sarà approvata si scriveranno
specifica e piano, e il lavoro vero si farà in `site/`.

## Versione 7 (attuale, 3 novembre 2026): le decisioni di Alessio

Fonte: la sua nota del 2/11 (`ale/nota-sezioni-2026-11-02.txt`, testo esatto del PDF) e i messaggi
del 3/11. Dati in `generatore/sezioni.py`, pagine in `pagine7/`, generatore `generatore/genmock7.py`.

- **5 sezioni**, in quest'ordine: Corpo, piacere e fantasie (si apre con questa) · Prevenzione e
  salute · Comunicazione, relazioni e consenso · Difficoltà e blocchi · Approfondimenti e attualità
  (parti: Storia e idee, Letture e ascolti, Notizie). 23 articoli, uno solo per sezione.
- **Testi**: titolo pagina, descrizione, H1 e introduzione (339–367 parole) di ogni sezione sono
  quelli di Alessio, parola per parola. Le frasi dei riquadri sono frasi sue prese dalle introduzioni.
- **Stile «pizzino attaccato»** (scelto da lui): foglietti di carta con nastro, inclinati solo su
  schermi grandi. **Solo i colori del sito** (crema, carta, bordeaux, inchiostro): niente pastelli.
- **Icone**: fiamma, scudo, fumetti restano; il lucchetto (non gli piaceva) diventa un germoglio
  dal sasso; nuova icona libro per Approfondimenti. Maschera non più usata.
- **Analisi** in `analisi/`: `commenti.md` (sconsigliati; meglio una domanda anonima),
  `pacchetti-video.md` (proposta «Percorsi» nella landing; video non visti: rete bloccata).
- **Logo HD** ufficiale in `materiali/logo/` (fuori da questa cartella).

## Cosa c'è

| Cartella | Contenuto |
|---|---|
| `pagine7/` | **Versione 7**: `blog.html`, 5 `sezione-*.html`, `articolo-esempio.html`, `articolo-approfondimenti.html`, `icone.html` |
| `pagine/` | Versione 6 (pastelli, temi provvisori), tenuta per confronto |
| `tavole/` | Le 3 tavole per Alessio (`tavole.html` più le immagini che usa) |
| `immagini/per-ale/` | Le 3 tavole già pronte in PNG, da mandare su WhatsApp |
| `immagini/schermate/` | Schermate desktop e telefono delle pagine |
| `generatore/` | v7: `genmock7.py`, `sezioni.py`, `icone7.py` · v6: `genmock6.py`, `icons5.py` |
| `ale/` | Testo esatto della nota di Alessio sulle sezioni |
| `analisi/` | Commenti, pacchetti e video |

## Come riaprire le prove

```bash
bash prototipi/NON-TOCCARE/apri.sh
```

Poi apri http://localhost:8766/prove/blog.html. Per rigenerare le pagine dopo una modifica al
generatore: `python3 prototipi/NON-TOCCARE/generatore/genmock7.py prototipi/NON-TOCCARE/pagine7`.

## Scelte fatte

- **5 temi**: Protezione e salute (8), Piacere e corpo (5), Desiderio e fantasie (3),
  Coppia e consenso (3), Difficoltà e blocchi (3). Un solo tema per articolo.
- **Pagina `/blog/`**: riquadri per tema (pastello scaldato verso crema e bordeaux, icona, frase,
  3 articoli fissi scelti una volta, «Tutti gli articoli del tema»), fascia «Scrivimi», elenco
  completo dal più recente. Niente conteggi, «nuovo» o fasce che scorrono (da aggiornare a mano).
- **Pagina di tema**: stile indice di libro, introduzione nella voce di Alessio (bozza), chiusura
  con «Scrivimi» e «Prossimo tema». Online diventerà `/blog/<tema>/`.
- **Articolo**: in alto «Blog / tema», in fondo «Altri articoli su…».
- **Icone** (scudo, fiamma, maschera, fumetti con «sì», lucchetto con chiave): si disegnano una
  volta all'apertura e si muovono solo con il mouse sopra o col Tab. A riposo nessuna animazione;
  con «riduci movimento» tutto fermo, lucchetto aperto.

## Revisioni (skill in `.claude/skills/`)

| Revisore | Primo giro | Versione 5 |
|---|---|---|
| Impeccable, design (Nielsen) | 20/32 | 25/32 |
| Taste, «sembra fatto a mano», blog / tema | 4 / 6 su 10 | 6 / 7 su 10 |
| Animazioni infinite a riposo | 36 | 0 |
| Processore del telefono (rallentato 4×) | ~570 ms/s | ~0 ms/s |

La versione 6 aggiunge le correzioni del secondo giro (senza «Ultimi articoli», link «Tutti gli
articoli del tema», telefono compatto, icone senza decorazioni, malva per Desiderio, breadcrumb
completo) e non è ancora stata rivalutata.

## Da decidere con Alessio

Nomi dei temi; frasi e introduzioni (sono bozze nella sua voce); i 3 articoli in vetrina per
tema; colori e icone (la maschera è stata tenuta per scelta, due revisori la trovano un cliché);
quale tema ha il riquadro grande.

## Da fare quando si passa al sito

- File `site/blog/temi.css` caricato solo da blog e pagine di tema; icone grandi scritte nella
  pagina (le animazioni CSS non funzionano dentro `<img>` o `<use>`).
- Pagine `/blog/<tema>/` con title, description, canonical, sitemap, JSON-LD
  (`CollectionPage` + `BreadcrumbList`), 5 redirect in `netlify.toml`.
- `PUBBLICARE.md`: un campo «Sezione» nella bozza e la riga dell'articolo da incollare anche nella
  pagina del tema. `verifica.sh`: ogni articolo in esattamente un tema e nella sua pagina.
- Difetto già presente online: negli articoli gli indirizzi lunghi delle fonti escono dallo
  schermo del telefono. Basta `.prose a{overflow-wrap:anywhere}` in `blog.css`.
