⚠️ DEGRADED: single-context (sono un sottoagente senza strumento per avviare altri sottoagenti: valutazione A fatta e annotata prima di leggere il detector, poi valutazione B)

# Revisione di design: versione di prova di aleedusex.net

Metodo: skill impeccable, `critique` (reference/critique.md). Pagine viste con Playwright a 1280 e 390 px tramite `apri.js`.
Pagine: home, /blog/, /blog/prevenzione-e-salute/, 2 articoli (ansia-da-prestazione-sessuale, preservativo-rotto-cosa-fare), legale, 404, domanda-inviata. Ho confrontato la prova (:8769) con il sito attuale (:8768).
Detector eseguito sugli 8 file HTML della prova: `impeccable detect --json` ha dato 41 segnalazioni ed exit 2.
Nessun file modificato in /home/user/Blog. Per lo stesso motivo non ho salvato lo snapshot in `.impeccable/critique/` e non ho avviato il `live-server` con l'overlay: avrebbe scritto nel progetto.

Screenshot in `/tmp/claude-0/-home-user-Blog/84cca8ba-3da9-5367-a343-0e50ff3ca4bf/scratchpad/revisione/shots-design/`:
- pagine intere `*-d-full.png` e `*-m-full.png`; prima schermata `*-fold.png`;
- pezzi leggibili in `tiles/` (per esempio `tiles/home-d-full-3.png`);
- dettagli: `header-d-zoom.png`, `logo-blog-3x.png` e `logo-blog-attuale-3x.png`, `diag-d.png`, `contatti-m.png`, `percorsi-m.png`, `dalblog-d.png`, `video-aperto-1280.png`, `home-m-strip-a/b/c.png`, `art-m-strip.png`, `blog-m-strip.png`, `small-m.png`;
- misure: `misura.js` (contrasti e microtesti) e `detect.json` (risultato del detector).

---

## Punteggio (euristiche di Nielsen)

| # | Euristica | Voto | Problema principale |
|---|---|---|---|
| 1 | Stato del sistema | 3 | Il modulo porta a una pagina di conferma chiara e le FAQ mostrano se sono aperte. Il menu della home non indica in che sezione sei. |
| 2 | Linguaggio del mondo reale | 3 | La voce è chiara e diretta. Però ci sono «DEOPIARCA» senza spiegazione e etichette come «Posizionamento» e «Manifesto». |
| 3 | Controllo e libertà | 3 | Uscite chiare: «Tutti gli articoli», «Torna al blog», 404 con due link. |
| 4 | Coerenza | 2 | Il nome è scritto in tre modi (logo AleEduSex, dateline Aleedusex, footer aleedusex). La pagina legale dice «non ha moduli», ma ora un modulo c'è. Il chip a pillola è l'unico elemento arrotondato del sito. |
| 5 | Prevenzione degli errori | 3 | Il modulo avvisa di non scrivere dati che ti rendono riconoscibile e chiede la spunta della privacy. |
| 6 | Riconoscere invece di ricordare | 3 | Le sezioni del blog sono visibili e portano il conteggio degli articoli. |
| 7 | Flessibilità | n/a | Sito di persuasione e lettura: non si applica. |
| 8 | Estetica e minimalismo | 2 | La home è lunga e ripete gli stessi concetti. Ci sono molti decori: timbri, texture, etichette maiuscole spaziate, animazioni. |
| 9 | Recupero dagli errori | 3 | La 404 è chiara e calda. Il modulo funziona con l'HTML del browser, senza JS. |
| 10 | Aiuto e documentazione | 3 | Le FAQ in home e le FAQ negli articoli rispondono ai dubbi veri. |
| **Totale** | | **25/36 (69%)** | **Sufficiente, al limite di «Buono»** |

**Voto complessivo di design: 6,5/10.** La base è solida: palette, coppia di font e pagina articolo. Il voto scende per tre motivi: la home è troppo densa e ripetitiva, restano tracce dello stile «timbro e pizzino» appena bocciato, e alcune modifiche nuove non sono finite (logo, coda degli articoli, contraddizioni nei testi).

---

## Quanto il design è specifico per Alessio

**Valutazione mia, fatta prima del detector.** L'identità è sua: crema e bordeaux, DM Serif Display con Source Serif 4, la voce in prima persona, la sezione «Cosa non sono». L'impalcatura però è un modello editoriale ripetuto in serie. Quasi ogni sezione ha la stessa formula: etichetta maiuscola spaziata, titolo enorme con una parola in corsivo bordeaux, nota grigia in corsivo a lato. Succede 10 volte:
- «Le frasi che *non dici*»
- «Tre motivi *onesti*»
- «Cosa *non* sono»
- «Cose che mi hanno detto, *prima di iniziare*»
- «A cosa serve *davvero*»
- «Tre passi, *niente acrobazie*»
- «I percorsi, *se servono*»
- «Quello che *si pensa*»
- «Pronto a *parlarne*?»
- «Se preferisci *leggere prima*»

È il segnale più forte di pagina «generata». Lo stesso vale per la serie di elenchi numerati 1. 2. 3. (Manifesto, fascia dei principi, Perché me, Come funziona, FAQ 01-07).

**Cosa dice il detector** (41 segnalazioni su 8 file):
- `cream-palette` (8): è la palette del brand, già decisa. Falso positivo da ignorare.
- `dark-glow` (8): ombre colorate bordeaux sotto i timbri e il riquadro CTA. Confermo: sono un peso decorativo.
- `codex-grid-background` (8): griglia e puntinato sul fondo bordeaux dei contatti e del CTA degli articoli. Confermo: è texture superflua.
- `italic-serif-display` (6), `hero-eyebrow-chip` (2), `kicker-above-heading` (1): coincide con la formula ripetuta che ho descritto sopra.
- `cramped-padding` (6, sulle card «frasi» e su un div mobile): falso positivo. Le card hanno padding, il detector legge male il figlio.
- `flat-type-hierarchy` e `tight-leading` (1 ciascuno, home): falso positivo o marginale. Il detector legge anche elementi nascosti.

Il detector non coglie i problemi più gravi: densità, ridondanza, logo, contraddizioni nei testi, coda degli articoli.

**Overlay visivo:** non attivato (vincolo di sola lettura).

---

## Impressione d'insieme

L'articolo è la parte migliore del sito: calmo, leggibile, ordinato. La home invece fa troppe cose e le dice troppe volte. Le modifiche nuove aggiungono contenuto utile (percorsi, blog, 15 minuti) ma senza toglierne: la home passa da 12.641 a 15.163 px su desktop (+20%), da 16.147 a 19.997 px su mobile (+24%), da 1.195 a 1.536 parole (+28%). Il cliente chiede «calma e ordine». **L'occasione più grande è sottrarre**: una home di circa 8-9 sezioni con un solo percorso verso la consulenza.

## Cosa funziona

1. **La pagina articolo** (`tiles/art-ansia-d-full-1.png`). Testo a 20/34 px, 65-78 caratteri per riga su desktop e 30-40 su mobile. H2 chiari, elenchi sobri, fonti citate, FAQ semplici. È esattamente «ordine e leggibilità».
2. **I percorsi a righe** (`percorsi-m.png`, `tiles/home-d-full-7.png`). Titolo, descrizione, dati e prezzo su una griglia regolare, senza card né decori. È il modello da estendere al resto della home.
3. **404 e domanda-inviata** (`small-m.png`). Brevi, calde, con un passo successivo chiaro. Lo stesso vale per «Cosa non sono»: onesto e utile per la fiducia.

---

## Problemi in ordine di priorità

### 1. [P1 · ALTA] Home troppo lunga e ripetitiva («troppe scritte»)
**Riguarda:** sito attuale, peggiorato dalle modifiche nuove.
**Dove:**
- `home-d-full.png`, `home-m-strip-a/b/c.png`: 12 sezioni più i percorsi e la firma nel footer.
- I tre principi compaiono **5 volte**: sottotitolo dell'hero, Manifesto «tre regole», fascia «1 · Performance / 2 · Vergogna / 3 · Linguaggio», «Tre motivi onesti», «Cosa non sono».
- L'offerta dei 15 minuti è ripetuta **5 volte**: link nell'hero, testo del passo 1, riquadro del passo 1, timbro «15′», link nei contatti.
- I «60 €» sono ripetuti **5 volte**.

**Perché è un problema:** chi arriva con un disagio cerca rassicurazione e un passo chiaro. Leggere lo stesso concetto cinque volte fa sembrare la pagina gonfia e allontana il pulsante.

**Soluzione A (consigliata):**
- Unire Manifesto, fascia, «Perché me» e «Cosa non sono» in una sola sezione «Come lavoro»: 3 principi in una riga ciascuno, più 2-3 righe «cosa non sono».
- Togliere la fascia «1 · Performance…».
- Spostare #dal-blog in fondo, prima dei contatti.
- Lasciare i 15 minuti in due punti: hero e contatti.
- Obiettivo: 8-9 sezioni, circa 10-11.000 px su desktop.

**Soluzione B (più leggera):** togliere solo la fascia dei principi e «Perché me», e mettere i percorsi in un `<details>` «Vedi i percorsi e i prezzi».

### 2. [P1 · ALTA] Logo PNG in testata: alone chiaro e colore diverso
**Riguarda:** modifica nuova.
**Dove:** `logo-blog-3x.png` (prova) e `logo-blog-attuale-3x.png` (attuale), `header-d-zoom.png`. Il problema si vede su tutte le pagine.

**Perché è un problema:**
- Il PNG (487×108) ha attorno alle lettere un contorno color carta (#F9F3E9). Sul crema (#F0E7D5) diventa un effetto «adesivo scontornato», cioè proprio l'estetica pizzino appena bocciata.
- Il rosso del file (#80011E) è più acceso e freddo del bordeaux del brand (#7A1E2B).
- Il footer dice ancora «aleedusex» in minuscolo e la dateline dice «Aleedusex»: tre grafie diverse.

**Soluzione A:** riesportare il logo come SVG (o PNG trasparente pulito a 2x/3x) senza contorno, colore #7A1E2B, e usarlo anche nel footer in crema.
**Soluzione B:** finché non arriva il logo ufficiale in alta definizione (è già tra i «Da fare»), tenere il wordmark tipografico attuale e uniformare la grafia ovunque.

### 3. [P1 · ALTA] Resti dello stile «timbro e pizzino» e troppo movimento
**Riguarda:** in parte il sito attuale, in parte le modifiche nuove (timbro 15′, riquadri, diagramma).
**Dove:**
- Timbri ruotati con ombra: «PIENA» in home, «parole.» nel blog, «non c'è.» nella 404, «arrivata.» in domanda-inviata, carta «sessuologia» nel diagramma.
- Ingresso `stampIn` con rotazione di -9°, rimbalzo `scale(1.03)` e durata 1,2 s, ripetuto su ogni pagina del blog.
- Card «frasi» (`tiles/home-d-full-2.png`) con il forellino `::before` e il sollevamento al passaggio del mouse.
- Puntinato e griglia sui fondi bordeaux (`contatti-m.png`, CTA degli articoli).
- 69 elementi `.reveal` che compaiono in dissolvenza mentre scorri.
- 52 etichette maiuscole spaziate nella sola home.

**Perché è un problema:** ogni pagina «salta» all'apertura. Le texture e le ombre colorate sporcano la calma richiesta. Il timbro ripetuto smette di essere un segno e diventa un tic.

**Soluzione A (consigliata):**
- Tenere **un solo** timbro, «PIENA» in home, statico o con una dissolvenza di 300 ms senza rotazione né rimbalzo.
- In blog, 404 e domanda-inviata mettere la parola in corsivo bordeaux senza riquadro.
- Togliere puntinato, griglia, forellino e sollevamento.
- Applicare `.reveal` solo ai titoli delle sezioni, o a niente.
- Etichette maiuscole al massimo in una sezione su due, a 12-13 px.

**Soluzione B:** tenere i timbri ma senza ombra né rotazione (rettangolo bordeaux piatto, angoli 2 px), un solo stile ovunque.

### 4. [P1 · ALTA] Coda degli articoli affollata, con due richieste in concorrenza
**Riguarda:** modifica nuova.
**Dove:** `tiles/art-ansia-d-full-4.png`, `-5.png`, `art-m-strip.png`. Dopo «Fonti» vengono, in quest'ordine:
1. In breve
2. Autore
3. Avvertenza
4. Modulo «Hai una domanda?»
5. Riquadro bordeaux con **3** pulsanti (WhatsApp, email, 15 minuti)
6. «Altri articoli in…»
7. «Tutti gli articoli»

Su mobile sono circa 3 schermate di sola coda.

**Perché è un problema:**
- Domanda anonima e consulenza a pagamento arrivano una dopo l'altra e si tolgono forza a vicenda.
- «In breve» messo in fondo non fa più da sommario: chi arriva da Google lo cerca in alto.

**Soluzione A:**
- Spostare «In breve» subito dopo il sottotitolo o l'immagine.
- In fondo: «Altri articoli in…», poi un solo blocco «Ne vuoi parlare?» con un pulsante principale (WhatsApp) e due link di testo («Mandami un'email» · «Preferisci fare una domanda anonima?»). Il secondo apre il modulo dentro un `<details>`, senza JS.
- Autore e avvertenza in due righe sotto.

**Soluzione B:** modulo e CTA nello stesso riquadro, con due colonne su desktop: «Domanda anonima» e «Parliamone».

### 5. [P1 · ALTA] Contraddizioni e segnaposto visibili nei testi
**Riguarda:** modifiche nuove.
**Dove:**
- `legale.html`, riga 39: «questo sito non usa cookie, **non ha moduli**…». Però la riga 83 descrive il modulo e il modulo esiste.
- Home: «Nessuna segreteria, **nessun modulo**, nessuna AI» e «Non ci sono moduli infiniti».
- Segnaposto visibili: «[Testo in arrivo da Alessio: …]» (`tiles/legale-d-full-0.png`) e «[periodo da decidere]».
- Il link «Disdette e rimborsi: come funzionano» sotto i percorsi porta proprio a quel segnaposto.

**Perché è un problema:** per una professione basata sulla fiducia, una promessa smentita due pagine dopo pesa più di qualsiasi scelta grafica.

**Soluzione:**
- Riscrivere il sottotitolo della pagina legale, per esempio «non usa cookie né tracciamento; l'unico modulo è quello anonimo delle domande».
- In home, «nessuna segreteria, nessuna AI».
- Togliere il link alle disdette finché il testo non c'è.
- Non pubblicare segnaposto tra parentesi quadre.

### 6. [P2 · MEDIA] Percorsi: il prezzo urla e le copertine dei video sono da social
**Riguarda:** modifica nuova.
**Dove:** `tiles/home-d-full-6.png`, `-7.png`, `video-aperto-1280.png`.

**Perché è un problema:**
- Il prezzo in corsivo display a 44 px bordeaux è l'elemento più forte di ogni riga: l'occhio va ai soldi prima che al contenuto.
- La copertina del primo video è un fotogramma di reel con baffi disegnati e la scritta «Creazione»: tono da Instagram dentro una pagina che vuole essere professionale.
- «DEOPIARCA» è gergo senza spiegazione.
- Ci sono 5 link «video» in una sezione.

**Soluzione:**
- Prezzo in tondo, 26-28 px, color inchiostro, con la nota sotto.
- Copertine scelte apposta: volto neutro, niente scritte sovrapposte, stessa inquadratura per tutti.
- Spiegare DEOPIARCA in mezza riga o toglierlo.
- In alternativa: un solo video «Come funziona» e niente video per riga.

### 7. [P2 · MEDIA] #dal-blog in home: doppione posizionato male
**Riguarda:** modifica nuova.
**Dove:** `dalblog-d.png`.

**Perché è un problema:**
- È identico alla lista «Le sezioni» del blog.
- Arriva a metà del percorso verso la consulenza, subito dopo «Sono tutte cose normali. E si possono affrontare.», e porta fuori dalla pagina nel momento meno adatto.
- Le icone a linea (maschera, scudo, fumetti, piantina, libro) sembrano prese da un set generico.

**Soluzione A:** spostarlo dopo le FAQ, prima dei contatti, ridotto a 3 righe: «Ultimi articoli» con titolo e link, più «Tutte le sezioni →».
**Soluzione B:** tenerlo dov'è ma come una sola riga di testo: «Preferisci leggere prima? Nel blog rispondo alle domande che si fanno a bassa voce →».
In entrambi i casi niente icone in home.

### 8. [P2 · MEDIA] Riquadri prezzo nei contatti: «60 €» va a capo
**Riguarda:** modifica nuova (timbro 15′).
**Dove:** `tiles/home-d-full-8.png`. Su desktop il riquadro stretto spezza «60» e «€» su due righe. Le etichette a 9-10 px, maiuscole e molto spaziate, non si leggono bene.

**Perché è un problema:** è un errore visibile proprio nel punto di conversione, e i riquadri ripetono informazioni già date tre volte.

**Soluzione A:** togliere i due riquadri e scrivere una riga sotto i pulsanti: «Prima consulenza 60 € · 60 minuti. Hai solo una domanda? 15 minuti al telefono, gratis.»
**Soluzione B:** un solo riquadro largo con `white-space: nowrap` ed etichette a 12-13 px.

### 9. [P2 · MEDIA] Microtesti piccoli e poco contrastati
**Riguarda:** soprattutto il sito attuale.
**Dove:** home (misurato con `misura.js`). 26 testi sotto il contrasto minimo AA e 34 testi sotto i 12 px. Esempi:

| Testo | Contrasto | Dimensione |
|---|---|---|
| «Torino · 2026» | 2,77:1 | 11 px |
| «Codice deontologico · supervisione…» (corsivo, maiuscolo, spaziato) | 2,43:1 | 11 px |
| «Prima consulenza · 60 min» sotto il pulsante | 3,18:1 | 11 px |
| «5 articoli» | 4,39:1 | 15 px |
| « » decorative | 2,41:1 | — |

Il blog è a posto: nessun testo sotto AA.

**Soluzione:**
- Microtesti a 13 px minimo.
- Inchiostro con opacità di almeno 0,7 sul crema.
- Mai maiuscolo, corsivo e spaziatura insieme.
- La riga «Prima consulenza 60 €» sotto il pulsante dell'hero va resa leggibile: è un'informazione decisiva.

### 10. [P2 · MEDIA] Pagina sezione e indice del blog: dettagli non finiti
**Riguarda:** modifica nuova.
**Dove:** `tiles/sezione-d-full-0.png`, `tiles/blog-d-full-1.png`.

**Perché è un problema:**
- Il percorso di navigazione «Blog /» finisce nel vuoto.
- L'icona grande dello scudo galleggia isolata a destra.
- I titoli nelle liste hanno `max-width: 22ch` e vanno su 3 righe anche su desktop, con un ritmo verticale irregolare.
- Il primo articolo dell'indice ha un titolo a circa 64 px, più grande del titolo della pagina.

**Soluzione:**
- «Blog / Prevenzione e salute», oppure solo «← Blog».
- Icona piccola accanto al titolo, oppure nessuna icona.
- Titoli della lista a 30-34ch.
- Primo articolo con la stessa misura degli altri, oppure al massimo 44 px.

### 11. [P3 · BASSA] Chip della sezione negli articoli
**Riguarda:** modifica nuova.
**Dove:** `tiles/art-ansia-d-full-0.png`. Una pillola bordata con icona accanto a «Blog /», non allineata alla stessa linea di base. È l'unico elemento arrotondato del sito.
**Soluzione:** testo semplice «Blog / Difficoltà e blocchi», con il secondo pezzo come link in corsivo bordeaux.

### 12. [P3 · BASSA] Altre cose minori
- **Menu mobile (attuale):** l'hamburger sta in mezzo, tra logo e «Scrivimi» (`attuale-home-m-fold.png`). Meglio: logo a sinistra, «Scrivimi» e ☰ a destra.
- **Diagramma «Tu → sessuologia» (attuale):** nello screenshot della pagina intera il riquadro di 470 px appare vuoto, perché tutto è a opacità 0 finché non parte l'animazione (`tiles/home-d-full-5.png` contro `diag-d.png`). Lo stato iniziale dovrebbe essere visibile e l'animazione limitarsi al tratto.
- **Virgolette (attuale):** virgolette dritte "…" nelle card «frasi» e nella citazione del Manifesto, ma « » altrove. Uniformare a « ».
- **Lettera iniziale grande (attuale):** la «L» di «La sessualità…» lascia «a sessualità» staccato. Va bene negli articoli; in home si può togliere.
- **Video aperto:** la colonna dei dati resta in alto e lascia un vuoto di circa 500 px a destra. Accettabile.

---

## Le persone che usano il sito

**Jordan, alla prima volta, arriva dalla home.** Nei primi 5 secondi capisce «Scrivimi» e «60 €», ma la riga del prezzo è a 11 px con contrasto 3,18:1. Scorrendo incontra i principi più volte, poi a metà pagina un invito ad andare sul blog: rischio di uscire senza aver scritto.

**Casey, da telefono:**
- La home richiede circa 20.000 px di scorrimento.
- Il pulsante «Scrivimi» resta sempre in testata (bene), ma il menu è scomodo con il pollice.
- La coda degli articoli occupa circa 3 schermate prima del footer.
- I video a 9:16 si aprono dentro la pagina e la allungano ancora.

**Persona del progetto: 30 anni, arriva da Google su «ansia da prestazione», si vergogna.**
- L'articolo la accoglie bene.
- «In breve» però è in fondo e lei non lo vede.
- Alla fine trova il modulo anonimo (ottimo per lei), ma subito dopo un riquadro bordeaux con tre pulsanti che chiedono di più.
- Se apre la pagina legale legge «non ha moduli» appena dopo averne usato uno: la fiducia cala.

---

## Domande su cui riflettere
- Se la home avesse una sola sezione sui principi invece di quattro, cosa perderebbe davvero?
- Il timbro «PIENA» è più forte se è l'unico timbro del sito?
- Chi arriva da un articolo deve scegliere fra tre modi di scrivere e un modulo, o basta una scelta chiara più un'alternativa discreta?

---

## Le 5 priorità

1. **Sottrarre dalla home.** Unire Manifesto, fascia dei principi, «Perché me» e «Cosa non sono» in una sezione. Spostare o ridurre #dal-blog. Tenere i 15 minuti in 2 punti. Obiettivo 8-9 sezioni. (`/impeccable distill`, poi `/impeccable layout`)
2. **Sistemare il logo.** SVG o PNG pulito senza alone, colore #7A1E2B, stessa grafia in testata, dateline e footer. In alternativa, tenere il wordmark tipografico finché non arriva il logo ufficiale. (`/impeccable polish`)
3. **Calmare la superficie.** Un solo timbro statico, niente rimbalzo né rotazione, niente texture, puntinato, forellino o sollevamento. Meno `.reveal` ed etichette maiuscole. (`/impeccable quieter`)
4. **Riordinare la coda degli articoli.** «In breve» in alto. In fondo un solo blocco «Ne vuoi parlare?» con un pulsante principale e il modulo anonimo come alternativa in `<details>`. (`/impeccable layout` e `/impeccable clarify`)
5. **Coerenza e finitura.** Correggere «non ha moduli» e «nessun modulo», togliere i segnaposto e il link alle disdette. Riparare «60 €» che va a capo. Microtesti a 13 px minimo con contrasto AA. Titoli delle liste a 30ch e percorso di navigazione completo nelle sezioni. Prezzi dei percorsi in tondo e copertine dei video scelte apposta. (`/impeccable clarify` e `/impeccable polish`)

Questions skipped: sono un sottoagente in sola lettura, senza strumento per fare domande all'utente. Le domande da girare ad Alessio e Mirko sono: (a) home ridotta in modo deciso (A) o leggero (B)? (b) un solo timbro o nessun timbro? (c) negli articoli conta di più il modulo anonimo o la consulenza?
