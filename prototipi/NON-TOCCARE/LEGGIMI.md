# Prototipo: blog diviso per temi — NON TOCCARE

Prove del redesign di `/blog/` (novembre 2026). **Niente di questa cartella va online**:
Netlify pubblica solo `site/`. Non modificare questi file e non usarli come modello per gli
articoli. Servono a Mirko e Alessio per decidere; quando la proposta sarà approvata si scriveranno
specifica e piano, e il lavoro vero si farà in `site/`.

## Cosa c'è

| Cartella | Contenuto |
|---|---|
| `pagine/` | Le pagine di prova (versione 6): `blog.html`, le 5 `sezione-*.html`, `articolo-esempio.html`, `icone.html` |
| `tavole/` | Le 3 tavole per Alessio (`tavole.html` più le immagini che usa) |
| `immagini/per-ale/` | Le 3 tavole già pronte in PNG, da mandare su WhatsApp |
| `immagini/schermate/` | Schermate desktop e telefono delle pagine |
| `generatore/` | `genmock6.py` (pagine) e `icons5.py` (le 5 icone animate, solo CSS) |

## Come riaprire le prove

```bash
bash prototipi/NON-TOCCARE/apri.sh
```

Poi apri http://localhost:8766/prove/blog.html. Per rigenerare le pagine dopo una modifica al
generatore: `python3 prototipi/NON-TOCCARE/generatore/genmock6.py prototipi/NON-TOCCARE/pagine`.

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
