# Revisione v3 (piccola) - home, /blog/, sezione, 2 articoli, legale

Metodo: Playwright a 1440, 1024, 768, 390 px, scorrimento completo con testata sticky visibile; menu, frasi apribili, video, domanda anonima, tastiera.
Controlli automatici su 6 pagine x 4 larghezze: nessun overflow orizzontale, nessun testo tagliato, nessun contenuto rimasto a opacity 0, nessun errore JS.
Screenshot e contact sheet: /tmp/claude-0/-home-user-Blog/84cca8ba-3da9-5367-a343-0e50ff3ca4bf/scratchpad/revisione/shots-v3rev/
Script: r1.js, r2.js, r4.js, r5.js, r6.js nella stessa cartella revisione/.

## Problemi (in ordine di gravita)

### 1. ALTA - Link «Manifesto» morto in tutto il sito
- Dove: footer, colonna «Indice», di tutte le pagine del blog (24 articoli, 5 sezioni, indice blog), 404 e legale. Punta a `/#manifesto`, che nella home v3 non esiste (le sezioni sono chi-sono, parliamone, dal-blog, cosa-faccio, funziona, percorsi, faq, contatti).
- Riproduzione: apri /blog/ > footer > «Manifesto»; la home si apre in cima e non succede nulla. Verificato con un crawler su 34 pagine: e' l'unico link interno rotto.
- Screenshot: shots-v3rev/sheet-m-sez-0.jpg (footer), sheet-d-blog-2.jpg.
- Soluzione: sostituire con «Di cosa parliamo» (`/#parliamone`) o togliere la voce, in _modello.html, generatore e tutte le pagine.

### 2. MEDIA - Indice del footer incoerente tra home e blog
- Home: Di cosa parliamo, Chi sono, Come funziona, Percorsi, FAQ, Blog. Blog/articoli: Manifesto, Chi sono, Come funziona, FAQ, Blog (manca «Percorsi»). In piu' l'ordine e' diverso dalla testata (Chi sono viene prima di Di cosa parliamo).
- Nel footer del blog «Privacy, cookie e note legali» e' un unico link (con sottolineatura a tutta larghezza su mobile); nella home sono tre link separati (Privacy, Cookie, Note legali).
- Soluzione: un solo footer condiviso (stessa lista, stesso ordine della testata, Percorsi incluso), e verifica.sh che lo controlli.

### 3. MEDIA - Testata del blog diversa dalla home, su telefono senza menu
- Home: 6 voci + Scrivimi (su telefono hamburger). Blog, sezioni, articoli, legale: solo «Blog», «Chi sono» (nascosto sotto ~640 px) e «Scrivimi». Su telefono, da un articolo, per arrivare a Percorsi o FAQ bisogna scendere al footer.
- Riproduzione: apri /blog/pep-e-prep-hiv.html a 390 px: vedi solo Blog + Scrivimi.
- Screenshot: sheet-m-pep-0.jpg.
- Soluzione: stesso hamburger della home anche nel blog, oppure aggiungere almeno «Come funziona» e «Percorsi».

### 4. MEDIA - Il nome della testata cambia: nella home «Blog» e' l'ultima voce, nel blog e' la prima
- Piccola ma visibile passando da una pagina all'altra (le voci saltano). Soluzione: stesso ordine ovunque.

### 5. BASSA/MEDIA - Evidenziazione della voce attiva (scroll-spy) sbagliata in home
- Dove: home, desktop. «Chi sono» resta evidenziato per tutto lo scorrimento, anche su Di cosa parliamo, Blog, Cosa faccio, Come funziona, Percorsi. Si evidenzia solo FAQ (e resta anche su Contatti). «Come funziona» e «Percorsi» non si accendono mai.
- Causa: IntersectionObserver con threshold 0.3 e rootMargin -10%/-60% (banda alta il 30% della finestra): le sezioni lunghe non raggiungono mai il 30% della propria altezza dentro la banda.
- Verifica: r4.js (porta ciascuna sezione sotto la testata e legge `.nav-active`).
- Soluzione: threshold 0 e scegliere la sezione la cui parte alta ha superato la testata.
- Nota: nelle pagine del blog «Blog» ha aria-current ed e' sottolineato: li' funziona.

### 6. BASSA - Testo legale non aggiornato al sito v3
- /legale.html: «Ultimo aggiornamento: 23 settembre 2026» ma gli articoli arrivano al 2 novembre e il modulo domande/video sono recenti; il modulo e' chiamato «Fai una domanda» mentre sul sito e' «Preferisci fare una domanda anonima?».
- Cita il servizio Tailwind CDN come destinatario dell'IP: va tolto quando Tailwind non sara' piu' da CDN (gia' in Da fare), altrimenti l'informativa e' falsa nel verso opposto.
- Soluzione: allineare nome del modulo e data; ricordarsi di aggiornare la voce Tailwind al momento del cambio. Nessun accenno ai video ospitati sul sito: ok (nessun terzo).

### 7. BASSA - Titolo di sezione a 3 px sotto la testata dopo l'ancora (solo telefono)
- Home, 390 px, menu > «Di cosa parliamo»: `h2` a top 80 px, testata alta 83 px. Il testo si legge (c'e' interlinea) ma e' appoggiato al bordo; le altre sezioni a 390 px hanno 80 px+ di margine di meno rispetto al desktop (128-144 px).
- Soluzione: padding-top della sezione o scroll-margin-top di ~24 px in piu' sotto i 640 px.
- Tutte le altre ancore (desktop 1440/1024/768, legale con scroll-margin 96 px) lasciano il titolo libero.

### 8. BASSA - Spazi vuoti larghi in home su telefono
- Dopo la firma «Alessio Cottonaro / Consulente in sessuologia» (circa 90 px vuoti) prima di «Le frasi che non dici a nessuno»; blocco crema vuoto di ~50 px sopra la sezione scura «Se preferisci leggere prima». A 1440 e 768 non succede.
- Screenshot: sheet-m-home-0.jpg (riquadri 4 e 6).
- Soluzione: ridurre il padding verticale sotto 640 px.

### 9. BASSA - Contrasto della testata semitrasparente sopra le sezioni scure/bordeaux
- Oltre al pulsante «Scrivimi» (gia' noto), il fondo della testata (crema 85%) sopra bordeaux/nero diventa un beige sporco e il logo con alone si vede peggio: sheet-m-home-0.jpg (riquadri 6-7), sheet-d-home-0.jpg (riquadro in basso a sinistra), footer a fine pagina. Il testo resta leggibile.
- Soluzione: fondo testata piu' opaco (95%) o piena tinta quando sopra una sezione scura.

### 10. INFO - Cose che ho provato e funzionano
- Menu mobile: si apre, link corretti, Escape chiude. Focus tastiera: contorno 2 px bordeaux sui link della testata (home, blog, articolo).
- Frasi apribili: aprono/chiudono, se ne possono aprire piu' insieme, nessun salto di layout; i link «Leggi: ...» portano agli articoli giusti.
- Video: si aprono, il poster e il player compaiono (max 260 px), la riproduzione parte e si ferma quando richiudi il riquadro.
- Domanda anonima: si apre, il campo ha etichetta, la casella privacy e' obbligatoria (messaggio di errore del browser), nessun invio senza consenso; /domanda-inviata.html esiste.
- Coerenza testi: prima consulenza 60 EUR, 60 minuti, telefonata di 15 minuti gratis identiche in home, sezione, articoli, contatti e meta; link WhatsApp con testo precompilato uguale ovunque. Conteggi sezioni (5+11+3+3+1 = 23) uguali agli articoli elencati.
- Nessun overflow orizzontale, nessun errore in console, nessun contenuto invisibile dopo lo scorrimento (animazioni `reveal` incluse) a 4 larghezze.
- Anchor e link: oltre a #manifesto nessun link interno o ancora rotta.

## Non verificabile qui
- CDN Tailwind sostituito da CSS locale (helper), quindi eventuali differenze reali col CDN non viste.
- Video: riproduzione con audio non provata (muto); font e immagini da rete reale.
