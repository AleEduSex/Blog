# Revisione «quanto sembra AI»: versione di prova di aleedusex.net

Revisore: art direction, skill `design-taste-frontend` in modalità revisione (passi 1 e 2 di «Redesign, restyle or review»).
Lavoro solo in lettura: in `/home/user/Blog` non ho modificato nulla.

## Metodo

- **Inspector** della skill (`inspect.mjs`, browser vero a 1440, 768 e 390 px) su una copia della prova in
  `revisione/taste-copia/`, con Tailwind messo in linea perché il CDN qui è bloccato. Pagine controllate: home, /blog/,
  /blog/prevenzione-e-salute/, sesso-vanilla, pep-e-prep. Rapporti e foto in `revisione/shots-taste/v2/<pagina>/`.
- **Lint** della skill (`lint.mjs`) sul codice di home, blog, articoli e blog.css.
- **Screenshot a pagina intera** via `apri.js` (desktop e telefono, tutte le 8 pagine) in `revisione/shots-taste/*-full.jpg`,
  divisi in fasce `*-d-NN.jpg`. Testo visibile estratto in `revisione/shots-taste/testo-*.txt`.
- Confronto del codice con il sito attuale (`site/`). Quasi tutti i segnali «da template» della home **c'erano già**
  (timbro PIENA, card delle frasi, eyebrow numerati, texture). La prova li eredita e aggiunge blocco blog, percorsi,
  box dei 15 minuti e video.

Vincoli che non contesto: palette crema/bordeaux, DM Serif Display e Source Serif 4. L'inspector segnala come
«WARN» il fondo crema e la scorciatoia del serif elegante. Sono scelte del brand, quindi le ignoro.

## Misure dell'inspector (prova)

| Pagina | FAIL | WARN | Dati principali |
| --- | --- | --- | --- |
| Home | 12 | 8 | 15 eyebrow · 45 maiuscoletti spaziati · 25 titoli con parola in corsivo colorato · numerazioni 01–06 · 4 sfondi a gradiente (puntini e griglia) · 7 ombre su elementi fermi · 35 filetti · 12 box con bordo da 1px · 1 fila di 6 card uguali con icona · 32 corpi di testo diversi · 22 testi sotto i 13px · 69 elementi con effetto reveal · H1 su 3 righe a ogni larghezza |
| Blog | 10 | 6 | eyebrow «Blog» · timbro «parole.» con ombra · 32 filetti · 17 titoli su 3 righe · 16 corpi · margini asimmetrici (120/141 px) |
| Sezione | 10 | 5 | stessi segnali del blog, più box CTA con ombra |
| Articolo | 12–13 | 4–6 | pill della sezione + meta in maiuscoletto sopra l'H1 · H1 di 10–11 parole su 3–4 righe · nessun elemento dominante nel primo schermo · contenuto spostato a sinistra (120 px contro 278 px a destra) · 19 corpi |

Lint: 107 FAIL. I più frequenti sono filetti (60), eyebrow (18), ombre (14), gradienti (8) e numerazioni (7), con 38 trattini lunghi in tutto.

Secondo le «caps» di `critique.md` la home non può superare 6.0. Un solo eyebrow o un timbro con ombra bastano a fermarla a 6.5.

---

## Voti: quanto sembra fatto con l'AI (1 = fatto a mano, 10 = generato)

| Pagina | Voto | In una riga |
| --- | --- | --- |
| **Home** | **7/10** | Contenuti veri e specifici, rivestiti di tutti i tic del «landing editoriale 2025». Chi ne ha viste cento la riconosce in tre secondi. |
| **Blog (indice e sezioni)** | **4/10** (sezioni 5/10) | Pulito e ordinato, a parte timbro ed eyebrow. Le introduzioni delle sezioni invece sono scritte come testo SEO generato. |
| **Articolo** | **3/10** | Il pezzo più autentico: fonti precise, esempi concreti, voce vicina ad Alessio. Il layout è standard e onesto. Pesano poco le illustrazioni un po' «clip art» e qualche «non X, ma Y». |

### Critica in formato `critique.md` §4 (home, prova)

```
ROUND 1 (prova, home)
Visto in un secondo: il blocco bordeaux inclinato «PIENA».
Idea (una frase): «le frasi che non dici a nessuno» diventano il contenuto. C'è, ma è sepolta a metà pagina
  e ripetuta in tre sezioni di citazioni.
Cosa si può fare: le FAQ apribili, i video e il diagramma «Tu → consulente → specialista».
Layout per sezione: hero=centrato con timbro / manifesto=split + lista numerata / chi sono=split con foto /
  principi=striscia di 3 colonne / frasi=griglia di 6 card / blog=split + lista / perché me=3 colonne numerate /
  cosa non sono=split + lista / parole nella stanza=split + lista di citazioni / posizionamento=diagramma /
  come funziona=numeri giganti + testo / percorsi=listino / FAQ=split + lista numerata / CTA=campo bordeaux + 2 box.
  «Split + lista» compare 5 volte: si vede lo stampo.
Punteggi: design 6.5 · usabilità 7.5 · creatività 6.5 · contenuti 8 → 6.9 (con cap → 6.0)
Cap applicati: FAIL dell'inspector (≤6.0), eyebrow, ombre, hairline (≤6.5)
I tre problemi più visibili:
1. Timbri inclinati con ombra, card con «foro da puntina», texture a puntini: sono gli avanzi dello stile «pizzini»
   appena rifiutato (home-d-00, home-d-03, home-d-10, blog-d-00).
2. Eyebrow e maiuscoletti spaziati sopra ogni titolo, più la parola in corsivo bordeaux in 25 titoli
   (home-d-01…d-10).
3. Cinque serie numerate e regola del tre ovunque (3 regole, 3 principi, 3 motivi, 3 passi, FAQ 01–07):
   la pagina sembra una scaletta generata (home-d-01, d-02, d-04, d-07, d-09).
```

---

## 1. Segnali visivi da «sito generato»

Ne ho contati **16 distinti**. In ordine di peso:

| # | Segnale | Dove | Gravità | Soluzione concreta |
| --- | --- | --- | --- | --- |
| V1 | **Timbri bordeaux inclinati con ombra** (`block-stamp`, `.stamp`, rotate −1,5°, ombra di 10–18 px) | «PIENA» nell'hero, «parole.» nell'hero del blog, card «CONSULENTE IN sessuologia — ALESSIO» nel diagramma | **Alta**: è la stessa famiglia dei pizzini rifiutati | Togliere rotazione, ombra e box. La parola resta nel titolo, stesso corpo e stesso colore inchiostro, al massimo bordeaux pieno senza corsivo. Es.: `Vivere una vita sessuale piena.` su due righe, oppure lo stesso titolo con la foto di Alessio accanto (vedi mossa 4). Nel diagramma basta un rettangolo bordeaux dritto, senza ombra, con la scritta «Consulente in sessuologia» in tondo. |
| V2 | **Card con «foro da puntina»** (cerchietto ○ in alto a sinistra), ombra, ultima card bordeaux a puntini | «Le frasi che non dici a nessuno» (6 card uguali) | **Alta**: sono letteralmente bigliettini appesi | Niente card. Le 5 frasi diventano una lista in grande, senza box, una per riga, con «Sono tutte cose normali. E si possono affrontare.» come frase finale in tondo. |
| V3 | **Texture a puntini e griglia** (`radial-gradient` e `linear-gradient` da 1px) | CTA bordeaux finale, card bordeaux, box CTA del blog | Media | Bordeaux piatto. Il colore pieno basta da solo. |
| V4 | **Eyebrow sopra ogni titolo**: 15 in home (PERCHÉ ESISTO, CHI SONO, DI COSA POSSIAMO PARLARE, PERCHÉ ME, ONESTÀ, PAROLE NELLA STANZA, POSIZIONAMENTO, COME FUNZIONA, PENSIERI AD ALTA VOCE, COMINCIAMO DA QUI…), più «BLOG» e «COMINCIAMO DA QUI» nel blog | Tutte le pagine | **Alta**: è il segnale più riconoscibile | Cancellarli. Se l'informazione serve, va nel titolo: «Chi sono» basta come titolo, non serve «CHI SONO / Ciao, sono Alessio.». «POSIZIONAMENTO» e «ONESTÀ» sono gergo da agenzia rivolto al cliente, non al lettore. |
| V5 | **Maiuscoletti spaziati** (45 in home): «ALEEDUSEX —— TORINO · 2026», «PRIMA CONSULENZA · 60 € · 60 MIN», «TORINO · ONLINE · A DOMICILIO», «CODICE DEONTOLOGICO · SUPERVISIONE · AGGIORNAMENTO CONTINUO», «— DESIDERIO», «→ PROSSIMO PASSO», «60 MINUTI · VIDEO O A DOMICILIO · 60 €», «PRIMA DI TUTTO / 15′ / IN REGALO», «© 2026 · ALEEDUSEX» | Hero, card, passi, CTA, footer | **Alta** | Tre righe di micro-meta nell'hero diventano **una frase** a 17 px: «Prima consulenza: un'ora, 60 €. A Torino, online o a casa tua.» Le etichette delle card spariscono. «Torino · 2026» va cancellato: è l'estetica da agenzia, timbro con anno e città. |
| V6 | **Parola in corsivo bordeaux nel titolo** (25 titoli): «tre *regole*», «*Alessio*», «*non dici*», «*leggere prima*», «*onesti*», «Cosa *non* sono», «*Non* sono…» ×4, «*davvero*», «*niente acrobazie*», «*se servono*», «*si pensa*», «a *parlarne?*», «Ne vuoi *parlare?*», «Senza giri di *parole.*» | Tutti i titoli | **Alta** per la ripetizione: una volta è una scelta, 25 volte è uno stampo | Titoli in un solo colore e un solo stile. Se proprio si vuole tenere, solo nell'H1 della home. |
| V7 | **Cinque serie numerate**: 1./2./3. del manifesto, «1 · PERFORMANCE / 2 · VERGOGNA / 3 · LINGUAGGIO», 1./2./3. dei «Tre motivi», numeri giganti 1./2./3. da 150 px nei «Tre passi», 01–07 nelle FAQ | Home | **Alta** | Numeri solo dove l'ordine conta davvero, cioè «Come funziona», con un `<ol>` normale e i numeri al corpo del titolo (non 150 px). Altrove vanno tolti: le FAQ non hanno un ordine. |
| V8 | **Regola del tre come struttura**: 3 regole + 3 principi + 3 motivi + 3 passi + terzine in hero, chi sono, CTA | Home | Media-alta | Fondere i doppioni (vedi T e mosse). Restano i 3 principi del brand, **una volta sola**. |
| V9 | **Tre sezioni di citazioni di fila** con virgolette decorative grandi: «Le frasi che non dici», «Cose che mi hanno detto, prima di iniziare», FAQ tra « » | Home | Media (alta per il rischio, vedi T9) | Una sola sezione di frasi. Le FAQ senza « » decorative, come semplici domande. |
| V10 | **Effetto reveal su 69 elementi** e diagramma che parte vuoto (alla prima apertura si vedono solo «Tu» e un puntino in un box vuoto, home-d-06) | Home | Media | Contenuto visibile senza animazione. Animazione al massimo sull'hero, e il diagramma deve essere disegnato fin da subito. |
| V11 | **Capolettera** «L» nel manifesto e «V» negli articoli | Home, articoli | Bassa-media | Togliere: è un vezzo da rivista che si ripete. |
| V12 | **Box con bordo da 1px e numeri «biglietto»**: «15′ IN REGALO» e «60 € 60 MINUTI» nella CTA, box «15 min», riquadro «In breve» | Home, articoli | Media | Una frase con il prezzo. «In breve» su un fondo appena più chiaro, senza bordo. |
| V13 | **Filetti ovunque** (35 in home, 32 nel blog) | Liste, header, footer | Bassa | Nel blog i filetti tra gli articoli **vanno bene** (ordine, leggibilità). In home vanno ridotti: spazio al posto delle linee tra le sezioni. |
| V14 | **32 corpi di testo diversi** in home (10…200 px), 22 testi sotto i 13 px | Home | Media | Cinque misure: titolo grande, titolo di sezione, sottotitolo, testo, nota. Niente sotto i 14 px. |
| V15 | **Pill della sezione** con icona sopra la frase dell'articolo, più meta in maiuscoletto («29 OTTOBRE 2026 · 5 MIN DI LETTURA») | Articoli | Bassa-media | Breadcrumb in testo semplice («Blog / Corpo, piacere e fantasie») e data in tondo minuscolo sotto il titolo. |
| V16 | **Illustrazioni «clip art»**: cono in cerchio con anello tratteggiato e pallini, cursore con gradiente | Articolo vanilla | Bassa-media | Vanno bene come idea. Togliere anello tratteggiato, pallini flottanti e gradiente, e tenere un'illustrazione piatta e dritta. |

Cosa pesa di più, in breve: **V1+V2+V3** perché sono lo stile «pizzini» rientrato dalla finestra, poi **V4+V5+V6**
perché sono la firma del template su tutta la pagina, infine **V7+V8**, cioè la scaletta a numeri e terzine.

---

## 2. Segnali testuali da AI

La voce di CLAUDE.md chiede frasi brevi e dirette, calde senza essere sdolcinate, niente frasi da rivista o da social, niente
«dovresti». Nel testo della home ci sono **16 trattini lunghi** e **10 «senza» e 10 «niente»**. In diversi casi a parlare
sono le formule, non Alessio.

| # | Frase esatta | Tipo | Gravità | Proposta |
| --- | --- | --- | --- | --- |
| T1 | «Non quelli che vorresti sentirti dire. Quelli che, secondo me, fanno la differenza.» | Correzione a effetto | Alta | Cancellare. Il titolo basta. |
| T2 | «Dirlo prima, evita di scoprirlo dopo.» | Aforisma | Media | Cancellare, oppure «Meglio dirlo subito.» |
| T3 | «Il consulente in sessuologia è la prima domanda, non l'ultima spiaggia.» | «Non X, ma Y» | Media | «Puoi venire da me anche solo per capire da dove partire.» |
| T4 | «Un'ora del tuo tempo. Una mappa chiara di cosa fare.» | Coppia di frammenti da slogan | Media | «In un'ora capiamo cosa sta succedendo e cosa puoi fare.» |
| T5 | «Rispondo io personalmente entro 24 ore. Nessuna segreteria, nessun modulo, nessuna AI.» + «Non c'è una segreteria. Non ci sono moduli infiniti.» | Terzina + doppione | Media (e «nessuna AI» è un boomerang su un sito che sembra AI) | Una volta sola: «Ti rispondo io, di solito entro 24 ore.» |
| T6 | «Tre passi, niente acrobazie.» / «I percorsi, se servono.» / «Quello che si pensa prima di scrivere.» | Titoli-battuta con virgola | Media | Titoli semplici: «Come funziona», «I percorsi», «Domande frequenti». |
| T7 | «senza pop, senza moralismi, senza fare scena» | Terzina | Bassa | «per smontare i tabù, senza fare scena.» |
| T8 | «Non serve sapere già dove ti trovi. Serve solo cominciare a chiederselo.» | Chiusura a effetto | Media | Cancellare: il diagramma lo dice già. |
| T9 | «Cose che mi hanno detto, prima di iniziare.» + «Non sono testimonianze cliniche. Sono i primi minuti, quelli in cui si decide di restare.» | Testimonianze dal tono inventato | **Alta**. Sembrano prove sociali inventate e CLAUDE.md vieta frasi delle persone seguite, «nemmeno camuffate». | Togliere la sezione. Le frasi generiche stanno già in «Le frasi che non dici a nessuno», presentate come frasi comuni e non come cose dette ad Alessio. |
| T10 | Sottotitoli in 2 frasi corte: «Non serve la parola giusta. Bastano queste.», «Sono tutte cose normali. E si possono affrontare.» | — | Bassa | **Sono di Alessio** (CLAUDE.md): tenerle, ma una per sezione e non come ritornello. |
| T11 | «non sono problemi di tecnica — sono problemi di parola, di paura, di silenzio» e altri 15 trattini lunghi | Trattino lungo + terzina | Media | Punto o due punti: «Non sono problemi di tecnica. Sono problemi di parola, di paura, di silenzio.» |
| T12 | «Sito disegnato con cura.» | Microcopy da agenzia | Media | Cancellare. |
| T13 | Introduzione della sezione Corpo: «Il corpo ti dice cosa succede, il desiderio ti dice perché, l'immaginazione ti dice come lo vivi», «quelli che si dicono, quelli che si tengono per sé, quelli che si provano e quelli che restano nella testa», «il piacere non ragiona per categorie, e nemmeno io.» | Anafore, elenchi ritmici, chiusura a effetto | **Alta** (è la parte più «generata» del blog) | Dimezzare. Tenere cosa trovi e a chi rivolgerti. Es.: «Qui trovi articoli su corpo, desiderio e fantasie. Puoi leggerli in qualsiasi ordine. Se qualcosa ti fa stare male, in ogni pagina ti dico a chi rivolgerti.» |
| T14 | Introduzione della sezione Prevenzione: «Si parla di… Si parla di… E si parla anche…», «Come sono fatte queste pagine?», «La prevenzione, in fondo, è una forma di rispetto», «Succede, e si può gestire.» | Anafora, domanda retorica su se stesso, chiusura morale | Alta | Tenere il paragrafo «Io sono un consulente in sessuologia, non sono un medico… ogni articolo ha le sue fonti», che è vero e utile. Togliere il resto. |
| T15 | Estratti degli articoli nell'indice: «Ecco…» 11 volte, «con calma» 6, «non è» 12 (es. «Ecco cosa succede nel corpo, con calma.», «Ecco cosa fare, con calma.», «Non è debolezza: è un meccanismo») | Formula ripetuta | Media: in fila si vede lo stampo | Far partire ogni estratto dalla risposta, senza «Ecco». Es.: «Cosa succede nel corpo prima, durante e dopo.» Regola da aggiungere ai campi di CLAUDE.md: niente «Ecco» e niente «con calma» nella Descrizione. |
| T16 | Articolo vanilla: «Non è un problema da risolvere, ma una differenza da conoscere.», «Quello che lo rende bello non è quanto è fuori dal comune, ma quanto è vero per te» | «Non X, ma Y» | Bassa | «È una differenza. Si può conoscere, senza doverla risolvere.» Una per articolo al massimo. |
| T17 | Virgolette dritte `"` in pagina: «"Non desidero più il mio partner…"», «"Se non puoi dirlo a voce…"», «"saperlo dire bene"» | Contro la regola di CLAUDE.md | Media | « » ovunque. |
| T18 | La terzina del brand «senza performance, senza vergogna, senza giri di parole» ripetuta in hero, striscia dei principi, H1 del blog e introduzioni delle sezioni, più «La sessualità non è performance. È linguaggio, permesso, presenza.» sia nel manifesto sia nella sezione Corpo | Slogan ripetuto | Media | È di Alessio e va tenuta, **una volta nell'hero e una nel manifesto**. Altrove la si dice con parole diverse. |

---

## 3. Cosa è autentico e va protetto

- **Le foto vere di Alessio** (tre ritratti in «Chi sono»). Sono il segnale anti-AI più forte del sito e oggi stanno a metà
  pagina. Non vanno filtrate né incorniciate.
- **I video suoi** (prima consulenza 44 s, percorsi 58 s, 1:56, 2:16, 1:46). Non vanno trasformati in decorazione.
- **I fatti specifici**: 60 € e 60 minuti; 15 minuti gratis al telefono; percorsi con prezzo, numero di incontri e dimensione
  del gruppo; metodo DEOPIARCA della Scuola di sessuologia di Torino; «rispondo io, dal mio indirizzo personale»;
  WhatsApp; Torino, online, a domicilio; «Non sono uno psicoterapeuta». Nessun generatore inventa questi dettagli.
- **Il diagramma «Tu → consulente → psicoterapeuta / andrologo-ginecologo / altri»**. È l'idea più «sua» del sito:
  dice cosa fa e cosa non fa. Va tenuto, raddrizzato e reso statico.
- **Le frasi sue** già in CLAUDE.md: «Non serve la parola giusta.», «Non c'è un livello minimo di disagio per meritarsi
  un'ora di chiarezza.», «Parlo come parli tu.», «Sono tutte cose normali. E si possono affrontare.».
- **La «frase» in testa a ogni articolo** («Cosa vuol dire sesso vanilla? Il nostro è noioso?»), cioè la domanda come
  la direbbe chi legge. È la vera idea del sito (vedi sotto) e va tenuta, togliendo la pill e il filetto che le stanno intorno.
- **Gli articoli**: fonti precise e datate (Manuale MSD, ANLAIDS 4 ore / 48 ore, Oxford 1997), «In breve», box
  dell'autore, avviso «non sostituisce una consulenza», form «Hai una domanda su questo tema?» anonimo. Sono la parte più
  credibile e professionale.
- **Blog e sezioni come lista ordinata** (data, sezione, titolo, estratto, «Leggi»). È ordine vero, va tenuto.

**L'idea che c'è già** (passo 4 della skill): *su questo sito, la frase che non dici a nessuno diventa il titolo di ogni
pagina.* Supera il test del concorrente: un altro sessuologo di Torino non scrive così. Oggi questa idea è sommersa da timbri e
card. Basta usarla in modo sobrio: una frase in corsivo bordeaux, senza box, in testa all'articolo, alla sezione e alla CTA.
Diventa così l'unico gesto tipografico ricorrente, al posto delle 25 parole in corsivo.

---

## 4. Regole dell'inspector che **non** applicherei a questo cliente

- Fondo crema e serif display: sono il brand.
- Filetti tra le voci di blog e sezioni: aiutano la lettura e il cliente chiede ordine.
- Titoli degli articoli su 3 righe in elenco: sono titoli SEO e devono restare lunghi. Basta scendere da 36 a 30 px in
  elenco e da 64 a 52 px nell'H1 dell'articolo.
- «Almeno 4 foto per pagina» nel blog: non serve una foto per articolo. Basta la firma di Alessio con la sua foto
  piccola nel box dell'autore.
- «Motion layer» obbligatorio: per un sito che deve essere sobrio e leggibile, meno movimento è meglio.

---

## 5. Le 5 mosse che lo rendono «fatto a mano» con il minimo intervento

1. **Via i residui dei pizzini.** Timbri senza rotazione né ombra («PIENA», «parole.», card del diagramma), card delle
   frasi senza box, foro e ombra, CTA e box bordeaux piatti senza puntini né griglia. Nel CSS si tratta di
   `transform:none; box-shadow:none; background-image:none` su `.block-stamp`, `.stamp`, `.concern-card`, sulla CTA e su
   `.cta-box`. È il segnale che il cliente ha già rifiutato. *Gravità alta, sforzo basso.*
2. **Via eyebrow e maiuscoletti.** Cancellare le 15 etichette sopra i titoli. Le tre righe di micro-meta dell'hero
   diventano una frase («Prima consulenza: un'ora, 60 €. A Torino, online o a casa tua.»). La meta degli articoli e
   «© 2026 · aleedusex» vanno in tondo normale. *Alta, basso.*
3. **Un solo stile per titolo.** Niente parola in corsivo bordeaux nei 25 titoli e niente numeri decorativi: restano solo i
   passi di «Come funziona», con un `<ol>` a corpo normale. Il corsivo bordeaux si usa soltanto per «la frase» (l'idea qui
   sopra). *Alta, basso.*
4. **Alessio nel primo schermo e meno doppioni.** Ritratto vero accanto al titolo nell'hero. Si fondono manifesto e striscia
   dei 3 principi; «Le frasi che non dici» e «Cose che mi hanno detto» (la seconda va tolta, vedi T9); «Tre motivi» e
   «Cosa non sono». Così spariscono la regola del tre e quattro sezioni a «split + lista». *Alta, sforzo medio.*
5. **Passata sul testo.** Togliere le frasi T1–T8, T12, T13 e T14 così come sono citate. Trattini lunghi sostituiti da
   punto o virgola. Virgolette dritte sostituite da « ». Estratti del blog senza «Ecco… con calma». Togliere «nessuna AI»
   e «Sito disegnato con cura». Reveal soltanto sull'hero, con il diagramma visibile senza script. *Media, basso.*

Stima: con le mosse 1–3 la home scende da 7 a circa 4 su 10, e con 4–5 a circa 3. Blog e articoli scendono a 2–3
senza toccarne la struttura.

---

### File di lavoro

- Rapporti dell'inspector e fasce di screenshot: `/tmp/claude-0/-home-user-Blog/84cca8ba-3da9-5367-a343-0e50ff3ca4bf/scratchpad/revisione/shots-taste/v2/`
- Screenshot a pagina intera e fasce desktop: `/tmp/claude-0/-home-user-Blog/84cca8ba-3da9-5367-a343-0e50ff3ca4bf/scratchpad/revisione/shots-taste/`
  (`home-d-00…11.jpg`, `blog-d-*.jpg`, `sez-d-*.jpg`, `vanilla-d-*.jpg`, `home-m-tris.jpg`, `home-mappa2.jpg`)
- Testo visibile delle pagine: `/tmp/claude-0/-home-user-Blog/84cca8ba-3da9-5367-a343-0e50ff3ca4bf/scratchpad/revisione/shots-taste/testo-*.txt`
- Copia con Tailwind in linea (solo per l'inspector): `/tmp/claude-0/-home-user-Blog/84cca8ba-3da9-5367-a343-0e50ff3ca4bf/scratchpad/revisione/taste-copia/`
