# Revisione totale del sito (4 novembre 2026)

Oggetto: la versione di prova v2, cioè il sito di oggi più le modifiche proposte (blog per sezioni, percorsi,
logo, blog in home, «Fai una domanda»). Per ogni punto è indicato se riguarda il **sito di oggi** o la **prova**.

Cinque revisori in parallelo, rapporti completi in `revisione-2026-11-04/`:

| # | Revisione | Skill | Modello | Voto |
|---|---|---|---|---|
| 1 | Design, gerarchia, leggibilità | impeccable (critique + detector) | Opus | 6,5/10 · Nielsen 25/36 |
| 2 | Quanto «sembra AI» | design-taste-frontend | Opus | home 7/10 AI · blog 4-5 · articolo 3 |
| 3 | Prestazioni, accessibilità, SEO | web-quality-audit, accessibility, performance, seo | Sonnet | AA quasi ok, 8 priorità |
| 4 | Funzionamento reale (Playwright) | — | Sonnet | 0 link rotti, 8 problemi medi |
| 5 | Testi e voce di Alessio | — (CLAUDE.md come metro) | Opus | 10 modifiche prioritarie |

I punti principali li ho ricontrollati io a mano: sono confermati.

**In una frase.** Le pagine degli articoli sono buone, ordinate e leggibili. La home è il problema: lunga,
ripetitiva, piena di formule da template (etichette in maiuscoletto, una parola in corsivo bordeaux in ogni
titolo, timbri, texture, numeri giganti, 69 comparse animate). Tutto questo c'era già prima e la prova lo ha
ereditato. È anche la ragione per cui ad Alessio il sito sembra «pesante».

---

## A. Da correggere prima di andare online (nessuna decisione da prendere)

| # | Problema | Dove | Soluzione |
|---|---|---|---|
| A1 | La privacy dice «Il sito non ha moduli» nell'In breve; la home dice «nessun modulo», ma ora il modulo c'è | prova: legale.html, home #contatti | Correggere le due frasi |
| A2 | Segnaposto visibili «[periodo da decidere]» e «[Testo in arrivo…]»; il link «Disdette e rimborsi» porta lì | prova: legale.html, home | Non pubblicare finché Alessio non manda i testi, oppure togliere il link e la sezione fino ad allora |
| A3 | Titoli dei libri con gli asterischi visibili (`*La volontà di sapere*`) e una frase senza soggetto | **sito di oggi**: articolo Foucault | Mettere `<em>` ai titoli e sistemare la frase |
| A4 | Su fondo bordeaux non si vede dove si trova chi usa la tastiera (contorno bordeaux su bordeaux, contrasto 1:1) | sito di oggi: riquadro articoli, footer, contatti | Contorno crema nei blocchi scuri (2 righe di CSS) |
| A5 | Chiudendo «Guarda il video» il video sparisce ma l'audio continua; due video possono suonare insieme | prova: home | 5 righe di JS nella home: pausa alla chiusura e un solo video alla volta |
| A6 | A 320 px blog e sezioni scorrono di lato di 9 px | prova: `.sez-list .c` | Permettere l'a capo al conteggio sotto i 360 px |
| A7 | Il link «salta al contenuto» delle pagine sezione punta a un'ancora che non esiste | prova | Sistemare l'ancora |
| A8 | La casella «Ho letto l'informativa» non vale come consenso per dati sulla salute (art. 9); la privacy dice che il modulo raccoglie «solo il testo», ma Netlify registra anche IP e browser; la nota «così non posso risponderti in privato» si capisce al contrario | prova: modulo, legale | Casella «Acconsento al trattamento…», testo privacy completo; da far vedere a chi cura la privacy di Alessio |
| A9 | Virgolette dritte `"` in home (7) e altrove: CLAUDE.md vuole « » | sito di oggi | Sostituire |
| A10 | `verifica.sh` e `PUBBLICARE.md` non conoscono le sezioni: un articolo nuovo passerebbe i controlli ma resterebbe fuori da ogni sezione, senza modulo, con i conteggi sbagliati | prova | Vedi decisione B8 |

## B. Decisioni da prendere (con le proposte)

**B1. Accorciare la home** (design, AI, testi: tutti e tre la indicano come problema n. 1)
Oggi ci sono 12 sezioni e circa 1.750 parole. I tre principi, i 15 minuti e i 60 € compaiono ognuno 5 volte.
- *Decisa (consigliata)*: 8-9 sezioni e circa 1.000 parole.
  - Unire Manifesto e Chi sono.
  - Fondere «Perché me», «Cosa non sono» e «A cosa serve un sessuologo» in «Cosa faccio, e cosa no».
  - Togliere «Parole nella stanza».
  - Accorciare «Come funziona».
  - Portare le FAQ da 7 a 5.
  
  Il testo tagliato è già pronto nel rapporto 5, § 1.2.
- *Leggera*: si tagliano solo le ripetizioni (slogan, prezzi, 15 minuti) e «Parole nella stanza».

**B2. «Cose che mi hanno detto, prima di iniziare»** (sito di oggi)
Sono frasi presentate come dette da persone seguite. CLAUDE.md vieta «frasi riconoscibili delle persone che
Alessio segue, nemmeno camuffate», e la FAQ 05 della home stessa dice di non usarle.
- *Togliere (consigliato)*.
- *Trasformarle*: «Frasi che sento spesso», senza dire che vengono da qualcuno.

**B3. Togliere gli avanzi dello stile a timbri** (sito di oggi; era proprio ciò che Ale ha trovato pesante)
Gli elementi in questione:
- timbri inclinati con ombra («parole.», «PIENA»);
- puntina e texture a puntini e griglia sui blocchi bordeaux;
- 15 etichette maiuscole sopra i titoli e 45 scritte in maiuscoletto spaziato;
- una parola in corsivo bordeaux in 25 titoli;
- numeri da 150-200 px;
- 69 elementi che compaiono scorrendo.

Le opzioni:
- *Via quasi tutto (consigliato)*: niente timbri ed etichette; il corsivo bordeaux resta in 2-3 titoli chiave; le comparse restano solo nell'hero.
- *Un solo timbro*: resta il timbro «parole.» del blog e il resto va via.

Proposta del revisore Taste, da valutare: come unico gesto tipografico usare la «frase» di chi legge, che apre già ogni articolo.

**B4. Logo**
Il PNG ricavato dal file di Alessio ha un alone chiaro attorno alle lettere (fa effetto adesivo) e un rosso
`#80011F` diverso da quello del sito `#7A1E2B`. Il nome poi è scritto in tre modi: AleEduSex, Aleedusex, aleedusex.
- *Chiedere ad Alessio il file originale senza alone* (SVG o PNG trasparente pulito), come aveva offerto lui.
- *Nel frattempo*: togliere l'alone dal nostro ricalco (si può fare) e decidere una sola grafia del nome.

**B5. La coda degli articoli**
Dopo le fonti vengono In breve, autore, avvertenza, modulo, riquadro con 3 pulsanti e altri articoli: circa 3 schermate
su telefono, con modulo e consulenza che si fanno concorrenza.
- *Proposta*: In breve in alto, sotto il sommario. In fondo un blocco solo, con il pulsante della consulenza e
  «Hai una domanda anonima?» che si apre a richiesta. Poi gli altri articoli.

**B6. I 15 minuti in regalo: una sola formula e un solo canale**
Oggi le formule sono cinque. «I primi 15 minuti» sembra uno sconto sulla consulenza. Si promette una
telefonata, ma il link apre una chat WhatsApp vuota.
- *Proposta*: la formula «Una telefonata di 15 minuti, gratis», usata al massimo 2 volte in home. Il link apre WhatsApp con un
  messaggio già scritto («Ciao Alessio, vorrei fissare la telefonata gratuita di 15 minuti»). Da confermare con Ale.

**B7. Incontri e prezzi coerenti**
- «Come funziona» e la FAQ 04 parlano di un percorso di «4-5 incontri» con sconto e di «seduta». I percorsi invece vanno
  da 3 a 5 incontri, hanno prezzi fissi e si chiamano «incontri».
- Da chiarire: 280 € è a persona? Che significa «300 € se vieni da solo»? DEOPIARCA va spiegato o tolto?
- Anche la zona di lavoro è scritta in 6 modi diversi, e «Sede Torino» fa pensare a uno studio. Serve una formula sola.

**B8. Come si pubblica un articolo con le sezioni** (decisivo per Alessio)
Oggi la stessa informazione va aggiornata a mano in 6-8 file: elenco, sezione, conteggi in più pagine,
«ultimo articolo» in home, sitemap.
- *Consigliato*: ogni articolo dichiara la sua sezione e un piccolo script, lanciato da Claude quando Ale scrive
  «pubblica» (non da Netlify, quindi niente build), rigenera elenco, sezioni, conteggi, home e sitemap.
  `verifica.sh` controlla sezione, conteggi, modulo e segnaposto. PUBBLICARE.md torna a 4 passi.
- *Alternativa*: niente conteggi né «ultimo articolo» in home, così resta meno da tenere allineato a mano.

**B9. Approfondimenti ha 1 solo articolo** e due parti «in arrivo».
- *Proposta*: tenere la pagina ma non farla indicizzare a Google finché non ha almeno 3 articoli, e togliere «In arrivo».

**B10. Video**
I sottotitoli sono dentro l'immagine, quindi per chi non vede e per Google non c'è testo. I video sono a 60 fps (34 MB in tutto).
- *Proposta*:
  - trascrizione breve sotto ogni video (bozze già pronte in `analisi/video/`, da far correggere ad Ale);
  - ricodifica a 30 fps, circa la metà del peso;
  - copertine più leggere.
  
  La prima copertina di «Al cuore del problema» va rifatta.

## C. Tecnico (lavoro di Mirko, non cambia l'aspetto)

1. **Tailwind da CDN → CSS statico** (sito di oggi, già nei «Da fare»). La home è lo script più pesante e
   bloccante, e senza JS resta senza stile. È l'intervento tecnico con più impatto.
2. **`netlify.toml` con gli header.** Cache lunga per font, immagini e video (oggi si riscaricano a ogni visita). Header
   di sicurezza: nosniff, Referrer-Policy, Permissions-Policy, frame-ancestors.
3. **Menu da telefono.** Da chiuso la tastiera entra nei 7 link nascosti. Va aggiunto `inert`, con il focus su
   «Chiudi» all'apertura e di nuovo sul pulsante alla chiusura.
4. **Contrasti in home.** 26 testi sono sotto AA (per esempio «Codice deontologico…» a 2,43:1 e 11 px) e 34 testi stanno sotto i 12 px:
   vanno alzate le opacità e portato il minimo a 13-14 px.
5. **Immagini.** La foto della home è a 2048 px ma si vede a 165 px. Le copertine sono a 1600 px senza `srcset`.
6. **SEO.**
   - I title degli articoli sono lunghi 86-110 caratteri e vengono tagliati: meglio stare intorno ai 60.
   - La description del blog ha 177 caratteri.
   - Le pagine sezione non hanno dati strutturati.
7. **Varie.**
   - La home non ha `<main>`.
   - Manca `scroll-margin-top` sulle ancore.
   - Non c'è un CSS di stampa (un articolo esce in 9 pagine).
   - A zoom 200% su telefono la testata sborda.
   - Le sezioni senza barra finale non hanno un redirect.

## D. Testi (dettaglio nel rapporto 5)

- **Slogan copiati ovunque**:
  - «Non serve la parola giusta» compare in 24 pagine;
  - «Il silenzio si sedimenta…» in 5;
  - «con calma» 48 volte nel blog;
  - 18 sommari iniziano con «Ecco…».
  
  Le frasi di Alessio funzionano se compaiono una volta sola.
- **Segnali da AI in home**: 12-16 trattini lunghi nel testo, molte terzine, «non è X, è Y», chiusure a effetto, sopratitoli
  («Perché esisto», «Posizionamento», «Onestà»). Le riscritture proposte sono nel rapporto 5, § 3.
- **Linguaggio inclusivo incoerente**: «perso/a», «Pronto a parlarne?», «non sei l'unico» convivono con «da sola o da solo».
  Proposta: aggiungere una regola unica a CLAUDE.md, dopo averne parlato con Ale.
- **Articoli da riguardare con Alessio** (contenuto, non stile):
  - Kink: il paragrafo sulla sicurezza minimizza i rischi.
  - Pillola del giorno dopo: la regola sulla ricetta ha una fonte del 2017; va ricontrollata.
  - Parlare col partner: la «terapia sessuale» è accostata ad Alessio.
  - Home: la videochiamata è descritta come «criptata» senza verifica.
- **Le introduzioni delle sezioni** sono testo di Alessio. Il revisore Taste le trova le più «generate» del sito,
  quello dei testi non vi trova problemi seri. Non le tocchiamo: al massimo lo diciamo ad Ale con tatto.

## E. Da proteggere

- Le pagine articolo: misura delle righe, tipografia, fonti con la data.
- Le foto vere di Alessio e i suoi video.
- I fatti chiari: 60 €, 15 minuti gratis, «Non sono uno psicoterapeuta», il diagramma dei rimandi.
- La 404 e la pagina di conferma.
- I percorsi a righe.
- I colori e i caratteri del brand.

## Ordine di lavoro proposto

1. **Subito**: tutto il blocco A. Sono correzioni, senza scelte da fare.
2. **Decidere con Ale**: B1-B4 (home, testimonianze, timbri, logo) e B6-B7 (15 minuti, prezzi).
3. **Prima di passare al sito vero**: B8 (pubblicazione semplice), C1-C3.
4. **Dopo**: C4-C7, D (testi), B10 (trascrizioni video).

---

## Stato (4 novembre, sera)

Fatte nella versione di prova (`generatore/anteprima.py`, passo 10), verificate nel browser:
A1 (frasi sul modulo), A2 (disdette nascoste finché non c'è il testo; conservazione domande 12 mesi,
da confermare con Alessio), A3 (Foucault: 7 corsivi, frase con soggetto), A4 (focus crema sui fondi
bordeaux, home e blog), A5 (video in pausa alla chiusura, uno alla volta), A6 (nessuno scorrimento
laterale a 320 px, anche il titolo di Approfondimenti), A7 (salta al contenuto), A8 (casella di consenso,
nota chiara, dati tecnici di Netlify nella privacy, honeypot nascosto ai lettori di schermo),
A9 (virgolette « » nel testo visibile di tutte le pagine).
Restano: A10 dipende dalla scelta B8. Le correzioni A3 e A9 valgono anche per il sito di oggi:
entrano in `site/` insieme al resto quando la prova viene approvata.
