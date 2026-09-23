# Piano di miglioramento — aleedusex.net

Data: 23/09/2026 · Base: commit `009b5fb` · Stato: **Fase 1 e 2 fatte** (23/09/2026), più la pagina legale

Legenda affidabilità: **[V]** = verificato leggendo il codice o misurando · **[I]** = ipotesi da confermare.

---

## 1. Sintesi

Il blog appena costruito è solido: statico, senza dipendenze, protetto da `verifica.sh` e con una procedura di pubblicazione testata dall'inizio alla fine. I punti deboli stanno quasi tutti nella **landing importata così com'era** e nei **contenuti ancora da scrivere**.

I 3 interventi più importanti:
1. **Foto della landing 4-5 volte più grandi del necessario, senza dimensioni dichiarate.** Pesano sulla velocità di caricamento e quindi su Google.
2. **Tailwind caricato dalla CDN in produzione.** È circa 300 KB di JavaScript che genera il CSS nel browser.
3. **Andare online con contenuti veri.** Servono il primo articolo, il testo introduttivo approvato da Ale e un'`og.jpg` da 1200×630.

---

## 2. Stato attuale

### Architettura [V]
```
repo (privato)                       Netlify (pubblica solo site/)
├── netlify.toml  publish="site"  →  aleedusex.net/
├── verifica.sh   controlli pre-push   ├── index.html   landing, Tailwind CDN + JS inline (1645 righe)
├── PUBBLICARE.md procedura per Claude ├── img/         3 foto Alessio
├── CLAUDE.md, docs/                   ├── robots.txt, sitemap.xml
└── site/  ─────────────────────────→  └── blog/        HTML statico + blog.css, nessun JS
```
- **Pubblicazione di un articolo:** Ale scrive in chat, Claude copia `_modello.html`, riempie i segnaposto, aggiorna l'elenco e la sitemap, esegue `verifica.sh`, fa il push. Netlify non è ancora collegato.
- **Dipendenze esterne a runtime:** Google Fonts (landing e blog), Tailwind CDN (solo landing).

### Punti di forza [V]
- **Blog senza nulla da mantenere:** zero build, zero npm, zero JavaScript. Google legge tutto l'HTML subito.
- **`verifica.sh` intercetta davvero gli errori:** testato con errori messi apposta (segnaposto rimasti, link rotti, virgolette, voce in evidenza, foto `og` mancante).
- **Procedura di pubblicazione provata end-to-end** in un clone usa e getta.
- **Separazione pulito/privato chiara:** solo `site/` va online. Radice e `docs/` restano private.
- **Accessibilità del blog corretta:** contrasto a norma, link "salta al contenuto", tag HTML bilanciati, `lang="it"`, focus visibile.
- **Storico git leggibile:** un commit per ogni cambiamento logico.

### Punti deboli
- **Landing mai revisionata:** è stata copiata byte per byte dal sito online. È voluto, ma porta con sé i suoi difetti.
- **Stessi valori in due posti:** i colori del brand sono sia in `site/index.html:40-45` sia in `site/blog/blog.css:3-14`. Se ne cambi uno, l'altro non segue.
- **Testata e footer copiati in ogni pagina del blog** (5 file). Nessun controllo impedisce che diventino diversi tra loro.
- **Blog non ancora pronto per andare online:** 3 articoli segnaposto, testo introduttivo da approvare, flusso di Ale via Claude/Cowork non ancora costruito.

---

## 3. Problemi rilevati

| # | Dove | Problema | Gravità | Aff. |
|---|---|---|---|---|
| P1 | `site/img/alessio-cottonaro-in-consulenza.jpg` (1919×2560, 605 KB), `…-ritratto.jpg` (2560×1706, 526 KB); `site/index.html:808,822,835` | Foto molto più grandi dei riquadri in cui compaiono (≤ 640 px di larghezza). Gli `<img>` non hanno `width`/`height`, quindi la pagina "salta" mentre le carica (CLS) | **alta** | [V] dimensioni misurate · [I] impatto su Lighthouse non misurato |
| P2 | `site/index.html:34-59` | Tailwind da CDN in produzione: script bloccante di circa 300 KB che genera il CSS a runtime. In console compare l'avviso "should not be used in production" | **alta** | [V] avviso visto in console · [I] peso esatto |
| P3 | `site/index.html:9` | `<link rel="icon" href="/favicon.ico">`, ma il file non esiste: un 404 a ogni visita | media | [V] |
| P4 | `site/index.html:1528` | Script Cloudflare `/cdn-cgi/…email-decode.min.js`, residuo di un vecchio salvataggio: 404 a ogni visita, e non serve a nulla | media | [V] |
| P5 | `site/og.jpg` (192×192) + `site/index.html:4-5` | Immagine di anteprima troppo piccola per la card grande (`summary_large_image`): le condivisioni su WhatsApp e social escono sgranate o tagliate. In più `og:image:width` vale `"192x192"`, che non è un valore valido: dovrebbe essere un numero | media | [V] file e meta · [I] resa sulle singole piattaforme |
| P6 | `site/index.html:1510-1512` | I link Privacy, Cookie e Note legali puntano a `#`. Il sito raccoglie contatti (email, WhatsApp): probabilmente serve almeno un'informativa privacy | media | [V] link · [I] obbligo legale: da confermare con chi segue gli aspetti legali |
| P7 | `site/index.html:1501` | Link YouTube che punta a `#` | bassa | [V] |
| P8 | `site/index.html:1485,1497,1507` | Contrasto del footer della landing sotto la soglia AA (etichette `/40` = 2.9:1, © `/45` = 3.3:1). Stesso difetto che nel blog è già stato corretto | bassa | [V] |
| P9 | assente `site/404.html` | Senza una pagina 404 propria, Netlify mostra la sua pagina generica: niente marchio e nessun link per tornare al sito | bassa | [V] file assente · [I] comportamento Netlify |
| P10 | `site/blog/_modello.html` + `site/robots.txt:2` | Il modello di articolo è un file di lavoro ma viene pubblicato. Per ora è protetto da `noindex` e `Disallow`, ma è raggiungibile da chiunque | bassa | [V] |
| P11 | 5 file in `site/blog/*.html` | Testata e footer copiati a mano in ogni pagina: se in futuro cambia uno, gli altri restano diversi senza che nessuno se ne accorga | bassa | [V] |
| P12 | `site/index.html:40-45` vs `site/blog/blog.css:3-14` | Colori del brand definiti in due posti diversi | bassa | [V] |
| P13 | `site/index.html` (0 occorrenze di `ld+json`) | La landing non ha dati strutturati (`ProfessionalService` o `Person` con città e servizi): è una occasione persa per le ricerche locali tipo "sessuologo Torino" | bassa → media per la SEO | [V] assenza · [I] beneficio |
| P14 | email in chiaro in `site/index.html` e in 4 file del blog | Indirizzo facile da raccogliere per chi manda spam | bassa | [V] |
| P15 | `verifica.sh` | Non controlla: descrizione ≤ 155 caratteri, data nel formato giusto, JSON-LD valido nel suo insieme (controlla solo le virgolette) | bassa | [V] |
| P16 | `netlify.toml` | Mancano intestazioni di cache per foto e CSS, e intestazioni di sicurezza di base | bassa | [V] · [I] beneficio reale |
| P17 | `site/index.html:1523` | `<img src="">` nel lightbox: HTML non valido, anche se innocuo | bassa | [V] |

**Già solido, non va toccato:** struttura e CSS del blog, procedura `PUBBLICARE.md`, `sitemap.xml`, `robots.txt`, JavaScript del menu mobile della landing (testato: si apre, si chiude e segue i link correttamente).

---

## 4. Opportunità abilitate dal nuovo modello

Lavori che prima erano rimandati perché troppo ampi, o perché troppo rischiosi da fare in un colpo solo:

1. **Togliere Tailwind da CDN dalla landing (P2).** Significa leggere tutte le 1645 righe della landing, estrarre le classi realmente usate e generare un CSS statico equivalente. Serve poi un confronto visivo, sezione per sezione, a più larghezze. Prima era troppo rischioso da fare in un colpo solo; ora il lavoro si può reggere tutto in un'unica sessione, con un controllo automatico degli screenshot "prima e dopo".
2. **Un solo punto per i colori del brand (P12).** Gli stessi colori, raccolti in un unico file CSS, usati sia dalla landing (dopo il punto 1) sia dal blog. È un refactor su più file che prima conveniva evitare.
3. **Controllo automatico della grafica:** screenshot di tutte le pagine a 375, 768 e 1280 px, confrontati con una versione di riferimento prima di ogni push importante. Oggi il controllo visivo lo faccio a mano.
4. **Progetto Claude di Ale (parte 2), finalmente fattibile:**
   - `EDITORIALE.md` ricavato dal tono della landing, che è l'unica fonte autentica della voce di Alessio;
   - istruzioni di progetto che incorporano `PUBBLICARE.md`;
   - una prova completa: da una bozza in chat a un articolo pubblicato.
5. **Contenuti:** proposte di primi articoli pensati per Google, in italiano, nel tono di Ale, con i confini deontologici della landing ("non sono uno psicoterapeuta"). Restano sempre bozze da approvare, mai pubblicate in automatico.
6. **Controlli più precisi in `verifica.sh` (P15),** scritti senza aggiungere dipendenze: resta solo bash, come oggi.

Cosa **non** conviene fare nonostante le capacità in più (ponytail): un generatore di siti o una build per risolvere P11. Un controllo nello script che testata e footer siano uguali in tutte le pagine costa 5 righe e basta.

---

## 5. Piano a fasi

Ogni fase si chiude con `bash verifica.sh` → OK e con il push. Il sito resta funzionante dopo ogni fase.

### Fase 1 — Pulizia a rischio zero (landing: solo righe inutili)
| Task | File | Sforzo | Rischio | Come verificare che è fatto |
|---|---|---|---|---|
| 1.1 Togliere lo script `cdn-cgi` (P4) | `site/index.html:1528` | S | nullo | 0 richieste 404 in console sulla landing, a parte favicon |
| 1.2 Favicon: togliere la riga `favicon.ico` oppure aggiungere il file (P3) | `site/index.html:9` | S | nullo | 0 errori 404 in console |
| 1.3 Correggere `og:image:width/height` (P5, solo la parte dei meta) | `site/index.html:4-5` | S | nullo | valori numerici |
| 1.4 Pagina `404.html` nello stile del blog (P9) | `site/404.html` (nuovo) | S | nullo | un indirizzo inesistente mostra la 404 del sito |
| 1.5 Controllo in `verifica.sh` che testata e footer siano uguali in tutte le pagine (P11) | `verifica.sh` | S | nullo | modificando a mano un footer in una copia → ERRORE |

### Fase 2 — Velocità delle foto (P1)
| Task | File | Sforzo | Rischio | Come verificare che è fatto |
|---|---|---|---|---|
| ✅ 2.1 Ridimensionare le foto | `site/img/*.jpg` | S | basso | FATTO: 1266 → 440 KB, PSNR 42-43 dB, profilo colore mantenuto; foto orizzontale 2048 px per la lightbox su schermi 2× |
| ~~2.2 `width`/`height` agli `<img>`~~ | — | — | — | **SALTATO**: i riquadri hanno già `aspect-ratio` (`index.html:124,137`), niente CLS. Errore del piano |
| ~~2.3 Header di cache~~ | — | — | — | **SALTATO**: la rivalidazione di default di Netlify va bene; una cache lunga servirebbe foto vecchie se sostituite con lo stesso nome |

### Fase 3 — Pronto per andare online (dipende da Ale)
| Task | File | Sforzo | Rischio | Come verificare che è fatto |
|---|---|---|---|---|
| 3.1 `og.jpg` da 1200×630 nello stile del brand (P5) | `site/og.jpg` | S | basso | anteprima corretta su un debugger OG |
| 3.2 Testo introduttivo del blog approvato | `site/blog/index.html:49` | S | nullo | ok scritto da Ale |
| 3.3 Primo articolo vero con `PUBBLICARE.md`, esempi rimossi | `site/blog/*`, `sitemap.xml` | M | basso | `verifica.sh` OK, 0 file `esempio-*` |
| 3.4 Pagina privacy minima e link del footer sistemati (P6, P7) | `site/privacy.html` (nuovo), `site/index.html:1501,1510-1512` | M | basso: contenuto legale | testo fornito o approvato da chi è competente |

### Fase 4 — Togliere Tailwind da CDN (P2, P12)
| Task | File | Sforzo | Rischio | Come verificare che è fatto |
|---|---|---|---|---|
| 4.1 Screenshot di riferimento della landing a 375, 768 e 1280 px, pagina intera | fuori dal repo | S | nullo | 3 immagini salvate |
| 4.2 Generare un CSS statico con solo le classi usate (Tailwind CLI eseguita una volta in locale, fuori dal repo) → `site/css/landing.css` | `site/index.html:34-59`, nuovo `site/css/landing.css` | L | **medio**: differenze grafiche | nessuno script Tailwind; differenza tra screenshot ≈ 0 |
| 4.3 Un solo file con i colori del brand, usato da landing e blog | `site/css/tokens.css`, `blog.css`, `landing.css` | M | medio | colori definiti in un posto solo; screenshot invariati |
| 4.4 Contrasto AA nel footer della landing (P8) | `site/css/landing.css` | S | basso | contrasto misurato ≥ 4.5:1 |

### Fase 5 — Parte 2: autonomia di Ale
| Task | File | Sforzo | Rischio | Come verificare che è fatto |
|---|---|---|---|---|
| 5.1 `EDITORIALE.md` (voce, parole da usare ed evitare, limiti deontologici) ricavato dalla landing | `EDITORIALE.md` | M | basso | approvato da Ale |
| 5.2 Istruzioni del progetto Claude/Cowork di Ale, con prova completa | documento fuori dal repo | M | medio: accessi GitHub [I] | un articolo di prova pubblicato da Ale da solo |
| 5.3 Spostare `_modello.html` nella radice, così non viene pubblicato (P10) | `_modello.html`, `robots.txt`, `PUBBLICARE.md`, `CLAUDE.md`, `verifica.sh` | S | basso | `site/` senza modello; `verifica.sh` OK |
| 5.4 Controlli aggiuntivi in `verifica.sh` (P15) | `verifica.sh` | S | nullo | test con errori messi apposta |

### Fase 6 — Facoltativa, SEO locale
| Task | File | Sforzo | Rischio | Come verificare che è fatto |
|---|---|---|---|---|
| 6.1 Dati strutturati `ProfessionalService` e `Person` nella landing (P13) | `site/index.html` (`<head>`) | S | basso | Rich Results Test valido |
| 6.2 Email nascosta ai raccoglitori di spam (P14) | landing e blog | S | basso | nessun indirizzo in chiaro nell'HTML, il link funziona |
| 6.3 Feed RSS del blog (se servirà) | `site/blog/feed.xml` + `PUBBLICARE.md` | S | basso | feed valido |

---

## 6. Domande aperte e decisioni che spettano a te

1. **Si può modificare la landing?** Finora era intoccabile. Le fasi 1, 2, 4 e 6 la modificano, e ogni modifica cambia il sito online appena Netlify è collegato. Serve l'ok di Ale in generale, oppure per ogni singola fase?
2. **Fase 4 (Tailwind), sì o no?** Il guadagno in velocità e SEO è reale, ma è l'unico intervento con un rischio medio di regressioni grafiche. Alternativa: lasciare Tailwind da CDN e fare solo le fasi 1-3.
3. **Contenuti legali e social:** chi fornisce il testo della privacy e il link YouTube (o si toglie)? E chi fornisce `og.jpg` (foto di Ale o grafica generata)?

Decisioni già prese che il piano rispetta: nessuna build o npm nel repository, nessun JavaScript nelle pagine del blog, Netlify collegato solo con almeno un articolo vero, pubblicazione sempre dopo il "pubblica" di Ale.
