# Pacchetti e video: una parte nel sito? (analisi, 3 novembre 2026)

Fonte: cartella Drive di Alessio «OnDelights» (documento «Pacchetti», elenco dei video).
**I video non li ho potuti guardare**: la rete di questa sessione blocca `drive.google.com`
(vedi in fondo come sbloccarla). Quello che segue viene dal documento e dai dati dei file.

## Cosa c'è

| # | Pacchetto | Per chi | Sessioni | Prezzo | Video (peso) |
|---|---|---|---|---|---|
| 1 | Chiarificazione sessuale iniziale | singoli o coppie | 1 × 60' | 100 € | 54 MB |
| 2 | DEOPIARCA: al cuore del tuo problema sessuale | singoli o coppie | 5 × 60', ogni 2 settimane | 450 € | 58 MB |
| 3 | Dialogo positivo sul desiderio | gruppo (max 8) | 3 × 90' | 240 € a coppia, 300 € singolo | 163 MB |
| 4 | Laboratorio del piacere consapevole | coppie, gruppo (max 6) | 4 × 90' | 400 € a coppia | 205 MB |
| 5 | Parliamo di sessualità ai figli | genitori, gruppo (max 8) | 4 × 90' | 280 € | 117 MB |
| 6 | Aziende (workshop) | aziende | 2 h | da 900 € + IVA | 103 MB — «coming soon» |

Il documento contiene anche politica di cancellazione, rimborsi («regola del valore trattenuto»),
credenziali e un accordo di servizio pensato per la piattaforma OnDelights.

## Da chiarire con Alessio prima di tutto

1. **Prezzo della prima consulenza**: sul sito è **60 €** (landing, box in fondo a ogni articolo,
   dati per Google); nel documento la chiarificazione iniziale è **100 €**. Sono due cose diverse
   (sito diretto e piattaforma) o va aggiornato il sito?
2. **Dove si compra**: i pacchetti si prenotano su OnDelights o direttamente con lui (WhatsApp/email
   come oggi)? Cambia il pulsante di ogni pacchetto.
3. **Aziende** è «coming soon»: va mostrato o no?

## Proposta

- **Dove**: nella landing (`/`), non nel blog. La landing converte verso la consulenza, il blog
  serve a farsi trovare. Nel blog basta un link «Percorsi» nel box finale degli articoli.
- **Come**: una sezione «Percorsi» dopo «Come funziona»: una scheda per pacchetto (nome, per chi,
  sessioni, prezzo, cosa ottieni in 2 righe, pulsante). Il video si apre dalla scheda, non parte da
  solo. Stile coerente con i «pizzini» del blog.
- **Video**: troppo pesanti così (54–205 MB). Due strade:
  - **Sul sito** (consigliata per privacy): ricompressi a 720p, 3–10 MB l'uno se durano pochi
    minuti, con immagine di copertina e **sottotitoli** (molti guardano senza audio, e servono per
    l'accessibilità). Netlify li serve senza servizi esterni né cookie.
  - **YouTube/Vimeo non in elenco**: niente peso sul sito, ma cookie di terzi: si caricano solo al
    clic (versione «nocookie») e va aggiornata la pagina privacy.
- **Da evitare**: video in riproduzione automatica, video con pazienti o persone riconoscibili.

## Per guardare i video in una prossima sessione

Nelle impostazioni dell'ambiente cloud (menu dell'ambiente nella barra del titolo della sessione →
Edit → Network access) aggiungere tra gli **Allowed domains**: `drive.google.com` e
`drive.usercontent.google.com`, lasciando attiva l'opzione per i package manager.
Guida: https://code.claude.com/docs/en/cloud-environments#network-access
Con quei domini aperti posso scaricarli, estrarre fotogrammi e durata, misurare l'audio e prepararne
versioni compresse da provare.
