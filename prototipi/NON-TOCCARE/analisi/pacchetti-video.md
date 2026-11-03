# Pacchetti e video: una parte nel sito? (analisi, 3 novembre 2026)

Fonte: cartella Drive di Alessio «OnDelights» (documento «Pacchetti» e i 6 video).
Prezzo della prima consulenza sul sito: **resta 60 €** (deciso da Mirko il 3/11).

## I video, guardati

Tutti verticali 1080×1920 (formato reel), Alessio parla in camera su fondo chiaro, **sottotitoli
impressi una parola alla volta** e titolo del pacchetto in rosso. **Nessun video dice un prezzo**:
vanno bene così con i 60 € del sito. Fotogrammi e testo (ricostruito dai sottotitoli, con
ripetizioni da ripulire) in `video/`.

| # | Video | Durata | Peso originale → compresso 720p | Di cosa parla |
|---|---|---|---|---|
| 1 | Chiarificazione sessuale iniziale | 44 s | 51 → 4 MB | Prima sessione: capire cosa succede, 3 passi concreti, nessun impegno lungo |
| 2 | DEOPIARCA | 58 s | 55 → 4 MB | Il metodo della Scuola di Torino (desiderio, eccitazione, orgasmo, piacere, identità, affetti, relazione, creatività, amore); da soli o in coppia |
| 3 | Dialogo positivo sul desiderio | 116 s | 155 → 11 MB | Coppie con desideri diversi; 3 incontri in gruppi di 4 coppie |
| 4 | Laboratorio del piacere consapevole | 136 s | 195 → 12 MB | Coppie: corpo, desiderio e comunicazione, sex toys, «patto intimo» |
| 5 | Parliamo di sessualità ai figli | 106 s | 111 → 10 MB | Genitori: come rispondere alle domande dei figli, script per età |
| 6 | Aziende | 90 s | 98 → 8 MB | Molestie, linguaggio, microaggressioni, transizioni di genere sul lavoro («coming soon») |

## Idee

1. **Landing: sezione «Percorsi»** dopo «Come funziona». Una scheda-pizzino per pacchetto (nome,
   per chi, sessioni, cosa ottieni, pulsante «Scrivimi»); il video si apre dalla scheda con il
   comando nativo del browser (`<video controls preload="none" playsinline poster>`): niente peso
   finché non si preme play, niente servizi esterni né cookie. Aziende a parte, come «in arrivo».
2. **Il video 1 accanto alla prima consulenza.** Parla proprio della prima sessione e non cita
   prezzi: è il video giusto vicino al riquadro «60 €» della landing, come «Ti spiego in 45 secondi
   come funziona».
3. **Ponte dal blog ai percorsi.** In fondo a ogni pagina di sezione, prima di «Scrivimi», un
   pizzino «Se vuoi lavorarci insieme» con il video del percorso affine. Funziona senza JavaScript.
   - Corpo, piacere e fantasie → Laboratorio del piacere consapevole (4)
   - Comunicazione, relazioni e consenso → Dialogo positivo sul desiderio (3)
   - Difficoltà e blocchi → DEOPIARCA (2)
   - Prevenzione e salute → Chiarificazione iniziale (1)
   - Approfondimenti → nessun video (è la sezione «da lontano»)
4. **Testo sotto ogni video.** I sottotitoli sono dentro l'immagine: Google e i lettori di schermo
   non li leggono. Sotto ogni video una trascrizione breve (bozza già pronta in `video/`, Alessio la
   corregge) aiuta accessibilità e ricerca.
5. **Copertine nei colori del sito.** Invece del primo fotogramma, un fermo immagine di Alessio che
   guarda in camera, senza parole impresse, con il nome del percorso in DM Serif su carta.
6. **Spunto per il blog.** Il video 5 apre un tema che il blog non ha: parlare di sessualità ai
   figli. Potrebbe diventare un articolo (in Comunicazione o in una sezione futura).

## Peso e formato

Compressi a 720p H.264 (compatibile con tutti i browser) pesano 4–12 MB: con `preload="none"` il
sito non li scarica finché non si preme play. Si possono ridurre ancora (540p) se serve. I file
compressi non sono nel repository: si rigenerano dagli originali quando si passa al sito.

## Deciso (Mirko, 3 novembre)

- **Video: per ora non vanno sul sito.** Le idee qui sopra restano solo come appunto; si
  riprendono soltanto se Mirko lo chiede esplicitamente.
- I percorsi si prenotano **direttamente con Alessio** (WhatsApp/email), come la prima consulenza.
- **Prezzi dei percorsi sul sito: sì**, prima si studia come inserirli → prova in
  `../percorsi/sezione-percorsi.html`, immagini in `../immagini/percorsi/`.
- Prima consulenza: resta 60 € (la «Chiarificazione» del documento è la prima consulenza).
- Aziende: non ancora; un'opzione «Sono un'azienda» nel prossimo futuro.

## Rete

Oggi i domini di Drive sono raggiungibili da questa sessione. Se una sessione futura li trova
bloccati: impostazioni dell'ambiente cloud → Edit → Network access → Allowed domains:
`drive.google.com`, `drive.usercontent.google.com`.
