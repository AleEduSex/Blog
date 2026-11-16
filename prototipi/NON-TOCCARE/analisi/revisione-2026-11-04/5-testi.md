# Revisione 5 · Testi (versione di prova)

Pagine lette: home, blog/index, le 5 pagine sezione, legale, domanda-inviata, 404 e 5 articoli
(pillola del giorno dopo = salute; perdita di erezione = difficoltà; come parlare di sesso con il
partner = coppia; kink = piacere; Foucault = approfondimento). Metro di giudizio: `CLAUDE.md`.
Solo lettura: nessun file del repo è stato toccato.

Gravità: **A** = da sistemare prima di andare online · **M** = conviene sistemare · **B** = rifinitura.

---

## 0. Il quadro in breve

- **Home troppo lunga**: circa 1.750 parole visibili in 12 sezioni. I pezzi più pesanti sono «Come
  funziona» con i percorsi (~430 parole) e le FAQ (~410). Tre sezioni dicono la stessa cosa
  («Perché me», «Cosa non sono», «A cosa serve davvero un sessuologo») e tre sono fatte di frasi
  tra virgolette (Di cosa parliamo, Parole nella stanza, FAQ). Si può scendere a circa 950-1.000
  parole senza perdere niente di sostanza (proposta al § 1.2).
- **Ripetizioni**: gli slogan di Alessio, che in CLAUDE.md servono a dare il tono, sono copiati
  parola per parola in molte pagine. «Il silenzio si sedimenta…» compare in 5 pagine, «Non serve la
  parola giusta» in 24, «con calma» 48 volte in 24 pagine del blog, «i primi 15 minuti te li regalo
  io» in 25 pagine, «Io non faccio diagnosi e non prescrivo farmaci» in 11, e «Ecco…» apre il
  sommario di 18 articoli.
- **Segnali da testo AI** soprattutto in home: 12 trattini lunghi nel corpo del testo, molte terzine,
  sopratitoli («Perché esisto», «Posizionamento», «Onestà»), frasi del tipo «non è X, è Y» e chiusure a effetto.
- **Bloccanti**: segnaposto visibili in legale.html, la pagina legale che dice «non ha moduli»
  quando nel blog un modulo c'è, asterischi markdown visibili nell'articolo su Foucault (anche nel sito vero).

---

## 1. Home (`index.html`)

### 1.1 Frase per frase

| # | Originale | Proposta | Motivo | Grav. |
|---|---|---|---|---|
| 1 | Sopratitolo «Torino · 2026» | Togliere | Sopratitolo decorativo senza informazione. «2026» invecchia. | B |
| 2 | «Codice deontologico · supervisione · aggiornamento continuo» (sotto l'hero) | Togliere qui e lasciarlo solo in «Chi sono» | È ripetuto quasi uguale in «Chi sono». | B |
| 3 | Sopratitolo «Perché esisto» | Togliere, oppure «Come lavoro» | È enfatico e suona da agenzia. | M |
| 4 | «La maggior parte dei blocchi sessuali non sono problemi di tecnica — sono problemi di parola, di paura, di silenzio. Lavoro su quelli.» | «Spesso un blocco non è una questione di tecnica. Mancano le parole, c'è paura, c'è silenzio. Io lavoro lì.» | È un dato senza fonte («la maggior parte»), con un trattino lungo, la forma «non X — Y» e una terzina. C'è anche l'accordo «la maggior parte… sono». | M |
| 5 | `"Se non puoi dirlo a voce, intanto puoi dirlo qui. È un buon primo passo."` | Togliere | Virgolette dritte. Il «qui» non si capisce (in home non c'è un modulo, e la home stessa dice «nessun modulo»). | M |
| 6 | Le tre regole del manifesto («Niente moralismo. Niente clinichese.» / «Si parla di te, non della tua diagnosi.» / «Ogni parola detta qui resta qui.») **e** le tre del Chi sono (Performance/Vergogna/Linguaggio) | Tenerne una sola: «Niente da dimostrare. Niente da nascondere. Niente giri di parole.» (sono i tre principi di CLAUDE.md) | Sono due terzine di fila sullo stesso tema. «Niente clinichese» torna anche in «Perché me» e in «Cosa non sono» (4 volte in tutta la home). | M |
| 7 | «Ogni parola detta qui resta qui.» | «Quello che mi racconti resta tra noi.» | La promessa è assoluta e il «qui» è vago: il sito? la stanza? | M |
| 8 | «Mi sono formato seriamente — codice deontologico, supervisione, aggiornamento — perché su questi temi l'improvvisazione fa più danni del silenzio.» | «Seguo un codice deontologico, vado in supervisione e continuo a formarmi: su questi temi improvvisare fa danni.» | Trattini lunghi e terzina. Inoltre «fa più danni del silenzio» contraddice il resto del sito, dove il silenzio è il problema. | M |
| 9 | «Online o, in alcune zone, anche a domicilio.» + scheda «Sede: Torino · Online» | Un'unica formula per tutto il sito (vedi § 2) | «Sede Torino» fa pensare a uno studio dove andare. | M |
| 10 | «senza pop, senza moralismi, senza fare scena» | «senza moralismi e senza fare spettacolo» | «Senza pop» non si capisce. È un'altra terzina. | B |
| 11 | `"Mi sento perso/a nelle relazioni o nella mia sessualità."` | «Non mi ritrovo più, nelle relazioni o nella mia sessualità.» | La barra «/a» è l'unica del sito. La frase così è neutra. Vanno messe le « ». | M |
| 12 | Tutte le frasi di «Di cosa possiamo parlare» tra `" "` | « » | Le virgolette dritte sono vietate da CLAUDE.md. | B |
| 13 | «— Desiderio», «— Ansia da prestazione»… | «Desiderio», «Ansia da prestazione»… senza trattino (basta lo stile) | Altri 5 trattini lunghi. | B |
| 14 | «Tre motivi onesti per scegliermi. Non quelli che vorresti sentirti dire. Quelli che, secondo me, fanno la differenza.» | Unire la sezione con «Cosa non sono» (vedi § 1.2) | Terzina, formula da pubblicità, frasi a effetto. | M |
| 15 | «andrologo, ginecologo, psicologo, endocrinologo» (Perché me) | «andrologo, ginecologo, psicoterapeuta, endocrinologo» | Nelle FAQ e in legale si dice «psicoterapeuta». | B |
| 16 | «Dirlo prima, evita di scoprirlo dopo.» | «Meglio dirlo prima che scoprirlo dopo.» | Virgola tra soggetto e verbo: è un errore. | M |
| 17 | Sopratitolo «Parole nella stanza» + «Cose che mi hanno detto, prima di iniziare. Non sono testimonianze cliniche. Sono i primi minuti, quelli in cui si decide di restare.» | Togliere la sezione, oppure: «Frasi che sento spesso» senza «mi hanno detto» | Frasi attribuite a persone seguite: è proprio ciò che CLAUDE.md e la FAQ 05 escludono («Non uso storie, frasi…»). La chiusura è a effetto. È anche il terzo blocco di citazioni della pagina. | **A** |
| 18 | Sopratitolo «Posizionamento» | Togliere | È gergo di marketing visibile a chi legge. | M |
| 19 | «A cosa serve davvero un sessuologo.» | «A cosa serve un consulente in sessuologia.» | Alessio si presenta come consulente in sessuologia (CLAUDE.md). Il titolo «sessuologo» crea ambiguità. | M |
| 20 | «è la prima domanda, non l'ultima spiaggia» / «Non serve sapere già dove ti trovi. Serve solo cominciare a chiederselo.» | Tenere la prima frase e togliere la seconda | Due chiusure a effetto di fila. | B |
| 21 | Testo nel diagramma: «io ti aiuto a capire dove sei e dove andare» | «Io ti aiuto a capire dove sei e dove andare» | Manca la maiuscola iniziale. | B |
| 22 | Passo 1: `Non serve "saperlo dire bene"` + «ti offro anche una telefonata gratuita di 15 minuti» + riquadro «15 min In regalo…» | Una sola menzione (vedi § 1.2) | Virgolette dritte. I 15 minuti sono detti due volte nello stesso passo e 4 volte in tutta la home. | M |
| 23 | «Rispondo io, dal mio indirizzo personale, entro 24 ore.» / «Rispondo io personalmente entro 24 ore. Nessuna segreteria, nessun modulo, nessuna AI.» | «Ti rispondo io, di solito entro 24 ore.» | È una promessa rigida (weekend, ferie). «Nessun modulo» è falso, perché il blog ha un modulo. «Nessuna AI» va tenuto solo se è vero in ogni caso. Altra terzina. | M |
| 24 | «— Non c'è una segreteria. Non ci sono moduli infiniti.» / «— Niente percorsi infiniti…» | Togliere | Ripete il passo stesso e il Chi sono («Non propongo percorsi infiniti»). | B |
| 25 | Passo 3: «un percorso breve — di solito tra 4 e 5 incontri —» | «un percorso con un obiettivo chiaro e un numero di incontri definito» | I percorsi elencati sotto hanno 3, 4, 4 e 5 incontri (vedi § 2). | M |
| 26 | «con il metodo DEOPIARCA della Scuola di sessuologia di Torino» | «con il metodo della Scuola di sessuologia di Torino» oppure una spiegazione di mezza riga | È una sigla mai spiegata. | M |
| 27 | «Cinque incontri per capire dove ti sei bloccato» | «Cinque incontri per capire dove si è bloccato qualcosa e cosa fare» | Al maschile, per un percorso «da solo o in coppia». | B |
| 28 | «Dialogo positivo…: Per coppie… 240 € a coppia · 300 € se vieni da solo» | «… 300 € se partecipi senza partner» con mezza riga che spieghi come funziona | Non si capisce come si partecipi da soli a un gruppo di coppie. | M |
| 29 | «Parliamo di sessualità ai figli» … «280 €» | «Parlare di sessualità ai figli» … «280 € a persona» (o «a coppia di genitori») | Nel titolo il soggetto è ambiguo. Il prezzo non dice per chi è. | M |
| 30 | «Disdette e rimborsi: come funzionano» → porta a un segnaposto | Togliere il link finché la sezione non è scritta | Rimanda a «[Testo in arrivo da Alessio…]». | **A** |
| 31 | FAQ 02 «posso venire da solo?» | «posso venire senza partner?» | Neutro e più chiaro. | B |
| 32 | FAQ 03 «Online è la stessa cosa di una sessione vera? Sì. La videocall è criptata…» | «Online funziona come in presenza? Per molte persone sì. Ci vediamo in videochiamata, l'ora è tutta tua…» | «Sessione vera» svaluta l'online, che è il servizio principale. «Criptata» dipende dallo strumento: va scritto solo se verificato, nominando lo strumento. | M |
| 33 | FAQ 04 «di solito propongo un percorso breve da 4 o 5 incontri… Puoi pagare una seduta alla volta oppure… uno sconto sul totale» | Vedi § 1.2 | Incoerente con i prezzi fissi dei percorsi e con i 3-5 incontri. Il prezzo del singolo incontro non è indicato. «Seduta» è un termine clinico (altrove si dice «incontro»). | M |
| 34 | FAQ 07 «Tanto magari passa da solo, no?» | Unirla alla 01 | Dicono la stessa cosa: non serve aspettare che sia «grave». | B |
| 35 | «Pronto a parlarne?» | «Ne vuoi parlare?» (come nelle pagine del blog) | È solo al maschile, mentre il blog usa già la forma neutra. | M |
| 36 | «Un'ora del tuo tempo. Una mappa chiara di cosa fare.» | «Un'ora per mettere in fila le cose e capire da dove partire.» | «Mappa chiara» promette un po' troppo e suona come uno slogan. | B |
| 37 | «15′ in regalo» | «15 minuti gratis» | Il simbolo ′ per i minuti non lo legge chiunque. | B |
| 38 | Firma: «…E uno dei più zittiti. Lavoro su quel silenzio.» | Facoltativa. Se resta: «Faccio questo lavoro perché di sesso si parla tanto, ma quasi mai di come stai tu. — Alessio» | Chiusura a effetto che ripete il manifesto («Lavoro su quelli»). | B |

### 1.2 Home tagliata: proposta (da ~1.750 a ~950-1.000 parole)

Per sezione:

| Sezione | Oggi | Proposta |
|---|---|---|
| Hero | 68 | ~45: togliere «Torino · 2026» e la riga sul codice deontologico |
| Manifesto + Chi sono | 75 + 133 | **~110 in tutto**: unire in un blocco solo |
| Di cosa parliamo | 94 | ~80: tenere (è la sezione più forte) e correggere «perso/a» |
| Dal blog | 76 | ~60 |
| Perché me + Cosa non sono + Posizione | 108 + 106 + 55 | **~110 in tutto**: una sezione «Cosa faccio, e cosa no» con il diagramma |
| Parole nella stanza | 71 | **0**: togliere (doppione e rischio privacy) |
| Come funziona + percorsi | 429 | ~260 |
| FAQ | 413 | ~220 (5 domande, risposte da 2-3 frasi) |
| Contatti | 134 | ~60 |

**Manifesto + Chi sono (unico blocco)**

> **Ciao, sono Alessio.**
> Sono consulente in sessuologia ed educatore professionale. Lavoro con persone e coppie tra i 20
> e i 50 anni, online o a domicilio. Seguo un codice deontologico, vado in supervisione e continuo
> a formarmi: su questi temi improvvisare fa danni.
> La sessualità non è performance. È linguaggio, permesso, presenza. Spesso un blocco non è una
> questione di tecnica: mancano le parole. Io lavoro lì, in modo pratico. Mi interessa cosa fare,
> non solo cosa pensare.
> **Niente da dimostrare. Niente da nascondere. Niente giri di parole.**

**Cosa faccio, e cosa no** (sostituisce Perché me, Cosa non sono e Posizione; si tiene il diagramma)

> **Parlo come parli tu.** Le parole tecniche solo se servono, e te le spiego subito.
> **Lavoro su cosa fare.** Esci con qualcosa di concreto da provare, non solo con un'analisi.
> **Non sono medico né psicoterapeuta.** Se quello che porti chiede un altro professionista
> (andrologo, ginecologo, psicoterapeuta, endocrinologo), te lo dico chiaramente e ti aiuto a capire a chi rivolgerti.
> **Non insegno a funzionare a comando.** Lavoriamo su consapevolezza, comunicazione e scelte concrete.
> *(sotto il diagramma)* Sono la prima porta, non l'ultima spiaggia.

**Come funziona**

> **1. Scrivi.** Un messaggio o una mail, anche due righe. Non serve saperlo dire bene. Ti rispondo
> io, di solito entro 24 ore.
> *Riquadro:* **Hai solo una domanda?** Una telefonata di 15 minuti, gratis. Serve anche a capire se ha senso iniziare.
> **2. Prima consulenza · 60 € · 60 minuti, online o a domicilio.** Ti faccio qualche domanda e
> ascolto. Alla fine ti dico chiaramente cosa stiamo guardando e se ha senso andare avanti.
> **3. Decidiamo insieme.** Se serve, ti propongo un percorso con un obiettivo chiaro e un numero di
> incontri definito. Se serve un altro professionista, te lo dico e ti indirizzo.
> **I percorsi** · Te li propongo solo dopo la prima consulenza, se hanno senso per te. *(seguono le 4 schede, invariate a parte le correzioni 26-29)*

**FAQ (5 domande)**

> **«Non so se è abbastanza grave da scriverti.»** Non c'è un livello minimo di disagio per
> meritarsi un'ora di chiarezza. Se ci pensi da mesi, è già un buon motivo. *(assorbe la 07)*
> **«Il problema è del mio partner, posso venire senza?»** Sì, succede spesso. Partiamo da quello
> che dipende da te. Se serve coinvolgere l'altra persona, lo decidiamo insieme.
> **«Online funziona come in presenza?»** Per molte persone sì. Ci vediamo in videochiamata e l'ora
> è tutta tua. A volte parlarne da casa propria aiuta.
> **«Quanto costa, in tutto?»** La prima consulenza costa 60 €. Se poi serve un percorso, costo e
> numero di incontri li trovi qui sopra e li decidiamo prima di iniziare. Nessuna sorpresa.
> **«Quello che dico resta tra noi?»** Sì. Non uso storie, frasi o situazioni riconoscibili, né sul
> sito né sui social. *(la FAQ 06 «E se non sei tu la persona giusta» si può togliere perché è già detta in «Cosa faccio, e cosa no»)*

**Contatti**

> **Ne vuoi parlare?**
> Prima consulenza 60 € · 60 minuti · Telefonata di 15 minuti gratis.
> [Scrivimi su WhatsApp] [Mandami un'email]
> Ti rispondo io, di solito entro 24 ore.

---

## 2. Coerenza tra le pagine

| Tema | Come è detto oggi | Proposta unica |
|---|---|---|
| **15 minuti** | «15 minuti al telefono, te li regalo io» (hero e contatti) · «telefonata gratuita di 15 minuti» (passo 1) · «15 min In regalo, al telefono» · «15′ in regalo» · nel blog «**i primi** 15 minuti te li regalo io» (25 pagine) | «Una telefonata di 15 minuti, gratis». Togliere «i primi», che fa pensare ai primi 15 minuti della consulenza a pagamento. Il link porta a WhatsApp, quindi: «Scrivimi e ti chiamo». |
| **Numero di incontri** | «di solito tra 4 e 5 incontri» (passo 3) · «da 4 o 5 incontri» (FAQ 04) · percorsi da 3, 4, 4 e 5 | «un numero di incontri definito», oppure «da 3 a 5 incontri» |
| **Pagamento** | FAQ 04: «una seduta alla volta… sconto sul totale» · percorsi a prezzo fisso, prezzo del singolo incontro non indicato | Decidere con Alessio. Se il pagamento a incontro esiste, va indicato il prezzo. Usare sempre «incontro», mai «seduta». |
| **Dove** | «Torino · Online · A domicilio» (hero e footer) · «Sede: Torino · Online» · «Online o, in alcune zone, anche a domicilio» · «in video o a domicilio» · «online o a domicilio» (blog) · «Torino e online» (firma degli articoli) · «videocall» | Una formula sola, per esempio «Online in tutta Italia · a domicilio a Torino e dintorni». Togliere «Sede» se non c'è uno studio. Nella firma degli articoli aggiungere «a domicilio». |
| **Specialisti** | psicologo / psicoterapeuta / «un professionista della salute mentale» / urologo | Usare sempre «psicoterapeuta». |
| **Moduli** | «nessun modulo» (contatti) · legale «non ha moduli» · modulo «Fai una domanda» in 24 articoli | Togliere «nessun modulo» e correggere legale.html (§ 5). |
| **Slogan ripetuti** | «La sessualità non è performance. È linguaggio, permesso, presenza.» (home, sezione Corpo, kink) · «Il silenzio si sedimenta…» (home FAQ, Comunicazione, Difficoltà, erezione, parlare-col-partner) · «Non c'è un livello minimo di disagio…» (home, Difficoltà, Prevenzione) · «Sono tutte cose normali. E si possono affrontare.» (home, Difficoltà) · «Non serve la parola giusta» (24 pagine) · «Non esiste il trucco che risolve tutto. Esistono cose concrete.» (identica in ansia ed erezione) | Ogni slogan al massimo una volta in home e una volta nel blog. Negli articoli dirlo con altre parole. CLAUDE.md riporta queste frasi «per il tono», non da incollare. |
| **Chiusura degli articoli** | «Un consulente in sessuologia serve a capire cosa sta succedendo e quale professionista è il più indicato. Io non faccio diagnosi e non prescrivo farmaci» (11 pagine, quasi uguale) | Bene la sostanza, ma va variata la forma. Il disclaimer in fondo all'articolo c'è già. |
| **Footer** | Home: indice con «Di cosa parliamo» e link Privacy / Cookie / Note legali separati · altre pagine: senza «Di cosa parliamo», un link solo | Questione tecnica, da segnalare a Mirko. |

---

## 3. Segnali di testo da AI

| Tipo | Dove (frasi esatte) | Riscrittura nella voce di Alessio | Grav. |
|---|---|---|---|
| Trattini lunghi a raffica | 12 nel corpo della home (vedi righe 4, 8, 13, 22, 25), più FAQ 02 «Partiamo da quello che dipende da te — di solito…» e FAQ 06 «— andrologo, ginecologo… —» | Due punti o punto. «Partiamo da quello che dipende da te: di solito è già un bel pezzo di strada.» | M |
| Terzine | Manifesto con 3 regole + 3 principi + «Tre motivi» + «Tre passi» · «senza pop, senza moralismi, senza fare scena» · «Nessuna segreteria, nessun modulo, nessuna AI» · «di parola, di paura, di silenzio» | Tenere solo la terzina dei tre principi (che è di Alessio). Le altre in due elementi o in prosa. | M |
| Sopratitoli | «Torino · 2026», «Perché esisto», «Onestà», «Posizionamento», «Parole nella stanza», «Pensieri ad alta voce», «Prima di tutto», «Cominciamo da qui» (su ogni pagina) | Toglierli. Il titolo da solo basta. | M |
| «Non è X, è Y» | «Il consulente… è la prima domanda, non l'ultima spiaggia» · «Non è un difetto di carattere: è un meccanismo» (erezione) · «Non è debolezza: è un meccanismo» (ansia, sommario) · «Il confessionale non è sparito, ha cambiato stanza» (Foucault) · «è un invito, non una richiesta» / «è una risposta, non un rifiuto di te» (parlare) · «Un "stop" è un'informazione, non un fallimento» (kink) · «non è una gara» (lubrificante e sex toys, sommari) | Lasciarne una per articolo. Le altre in forma diretta: «Succede per un meccanismo preciso, e si può smontare.» | M |
| Chiusure a effetto | «Sono i primi minuti, quelli in cui si decide di restare.» · «Serve solo cominciare a chiederselo.» · «Lavoro su quel silenzio.» · «Le domande aperte aprono, le conclusioni chiudono.» (parlare) · «I gusti degli altri non sono un tuo problema.» (kink) | Togliere, o chiudere con una cosa pratica: «Se vuoi provarci, comincia da una domanda: "Cosa ne pensi?"» | B |
| Sommari tutti uguali | «Ecco…» in 18 articoli · «con calma» 48 volte in 24 pagine (sommari: pillola, preservativo rotto, orgasmo, stealthing) | Variare. Per esempio, pillola: «Si prende dopo un rapporto non protetto e funziona meglio se la prendi presto. Come funziona, quando e dove trovarla.» | M |
| Ripetizione interna | Kink: «Il kink è fantasia che prende forma» 3 volte (sommario, apertura, In breve) | Tenerla solo nell'apertura. | B |
| Riferimenti alla «serie» | Parlare: «Questo articolo fa parte di una serie sul kink e sulle fantasie» · Kink: «Nei prossimi articoli entro nei dettagli su come dirlo» (l'articolo esiste già) | Parlare: togliere la frase (l'articolo è generale e così sembra destinato solo a chi pratica kink). Kink: «Come dirlo lo spiego in Come parlare di sesso con il partner.» | M |

---

## 4. Errori

| Pagina | Originale | Correzione | Grav. |
|---|---|---|---|
| Foucault | `*La volontà di sapere*`, `*L'uso dei piaceri*`, `*La cura di sé*`, `*scientia sexualis*`, `*ars erotica*` con gli asterischi visibili | Corsivo vero (`<em>`) oppure « ». **Il problema c'è anche nel sito vero** (`site/blog/foucault-storia-della-sessualita.html`). | **A** |
| Foucault | «E io cosa faccio, allora? Io non sono un confessore e non ti giudico. Serve a capire cosa sta succedendo…» | «Non sono un confessore e non ti giudico. Il mio lavoro serve a capire cosa sta succedendo e quale professionista è il più indicato.» (manca il soggetto) | M |
| Home | «Dirlo prima, evita di scoprirlo dopo.» | «Meglio dirlo prima che scoprirlo dopo.» | M |
| Home | 7 virgolette dritte `" "` | « » | B |
| Erezione (FAQ) | «Succedere ogni tanto è comune» | «Se succede ogni tanto, è comune» | M |
| Erezione (FAQ) | «Un episodio isolato non è una diagnosi, e nemmeno quella fatta in casa lo è.» | «Un episodio isolato non dice niente di definitivo. E nemmeno una ricerca su Google.» | B |
| Pillola (FAQ) | «…fai il test e, se serve, parlane con un consultorio. Non fare diagnosi in casa.» | Togliere «Non fare diagnosi in casa»: contraddice il test di gravidanza, che si fa proprio in casa. | M |
| Comunicazione (sezione) | «non è una colpa tua» | «non è colpa tua» | B |
| Modulo (24 articoli) | «Ho letto l’informativa privacy.» con apostrofo tipografico (altrove è dritto) | Uniformare (vedi anche § 5) | B |
| Home / percorsi | «Parliamo di sessualità ai figli» | «Parlare di sessualità ai figli» | B |

**Linguaggio inclusivo, oggi incoerente.** In home: «perso/a» (barra), «Pronto a parlarne?», «posso
venire da solo?», «Credevo di essere l'unico», «dove ti sei bloccato». Nel blog: «da sola o da solo»,
«sicura o sicuro» (pillola), «non sei l'unico» (In breve di parlare), «stare più tranquillo»
(Prevenzione). Regola proposta da scrivere in CLAUDE.md: forme neutre quando si può («Ne vuoi
parlare?», «senza partner», «non sei la sola persona»). Maschile e femminile per esteso solo dove il
tema lo chiede (pillola). Mai barre né asterischi. Il maschile solo quando l'articolo riguarda
uomini (erezione: va bene così).

---

## 5. Rischi (promesse, salute, privacy)

| Pagina | Originale | Proposta | Motivo | Grav. |
|---|---|---|---|---|
| legale | «In breve: questo sito non usa cookie, non ha moduli e non traccia nessuno.» | «In breve: questo sito non usa cookie e non traccia nessuno. L'unico modulo è quello anonimo per fare una domanda dal blog. Quello che mi scrivi resta tra noi.» | Contraddice la stessa pagina e il modulo presente in 24 articoli. | **A** |
| legale | «[Testo in arrivo da Alessio: …]» (Disdette) e «le cancello entro [periodo da decidere]» | Scrivere i testi o nascondere le sezioni | Segnaposto visibili. | **A** |
| Modulo articoli | Casella «Ho letto l'informativa privacy.» con base giuridica dichiarata «il consenso che dai spuntando la casella» | «Acconsento a inviare la domanda alle condizioni dell'[informativa privacy].» | «Ho letto» non è un consenso. Le domande possono contenere dati sulla salute e sulla vita sessuale (art. 9). Da far confermare a chi segue la privacy. | M |
| Modulo articoli | «Non scrivere nome, email o dettagli che ti rendono riconoscibile: così non posso risponderti in privato.» | «Non scrivere nome, email o dettagli che ti rendono riconoscibile. Da qui non posso risponderti in privato: se vuoi una risposta solo per te, scrivimi su WhatsApp.» | Così com'è sembra che non si debba scrivere il nome *per* impedire la risposta. | M |
| Modulo articoli | «Arriva solo a me e non viene pubblicata: se può servire anche ad altre persone, diventa un articolo» | «La leggo solo io e non la pubblico così com'è. Se può servire ad altre persone, ne faccio un articolo, senza niente che ti renda riconoscibile.» | «Non viene pubblicata» e poi «diventa un articolo» si contraddicono. | B |
| legale | «Il servizio esterno Tailwind CSS… riceve il tuo indirizzo IP…» | «La pagina principale usa un servizio esterno (Tailwind) per la grafica: questo servizio vede il tuo indirizzo IP, ma non salva cookie.» | Per una persona comune «Tailwind CSS» non vuol dire niente. | B |
| Home | «Parole nella stanza: Cose che mi hanno detto…» | Vedi riga 17 | Frasi attribuite a persone seguite. | **A** |
| Home | «La videocall è criptata» | Solo se è verificato, nominando lo strumento. Altrimenti togliere. | Garanzia tecnica non verificabile. | M |
| Home | «Rispondo… entro 24 ore» (2 volte) | «di solito entro 24 ore» | È una promessa rigida. | B |
| Home | «La maggior parte dei blocchi sessuali…» | Vedi riga 4 | Dato senza fonte. | M |
| Home | «A cosa serve davvero un sessuologo» | Vedi riga 19 | Titolo professionale. | M |
| Kink | «Il Manuale MSD segnala una cosa sola, ma importante: i giochi che limitano il respiro… Non sono una pratica da provare da soli o senza esperienza. Per tutto il resto, il consiglio è semplice: curiosità, calma e comunicazione.» | «Una cosa in particolare: i giochi che limitano il respiro sono tra i più pericolosi, perché si può perdere conoscenza in pochi secondi. Il mio consiglio è di non farli. Per tutto il resto: andate piano, accordatevi prima su una parola per fermarvi e non lasciate mai sola una persona legata.» | «Una cosa sola» e «per tutto il resto il consiglio è semplice» minimizzano i rischi. «Senza esperienza» lascia intendere che con l'esperienza vada bene. | M |
| Pillola | Regola sulla ricetta del levonorgestrel ricavata da una fonte AOGOI del 2017, con la nota «le regole possono cambiare» | Sostituire con la fonte AIFA in vigore sulla pillola del giorno dopo (da verificare prima di scrivere la regola) e dirla chiaramente: chi cerca questa pagina ha fretta. | Fonte datata su un tema urgente. Il testo resta vago proprio dove serve chiarezza. | M |
| Parlare | «Il Manuale MSD, nel capitolo per i medici sul disturbo orgasmico femminile, scrive che la terapia sessuale per le donne… può spesso aiutare. Vale anche per le situazioni in cui le difficoltà sono di coppia» | Togliere il paragrafo, oppure: «Quando le parole non arrivano, avere uno spazio con una guida aiuta. Un consulente in sessuologia può essere quella guida, e se serve un percorso di terapia ti dice a chi rivolgerti.» | La fonte è forzata (un altro disturbo, applicato alla coppia in generale). «Terapia sessuale» accostata ad Alessio, che non è psicoterapeuta. | M |
| Erezione | «Detto ad alta voce, il problema perde metà del suo peso.» | «Detto ad alta voce, pesa già meno.» | Quantità inventata. | B |
| Erezione (FAQ) | «Nella forma psicogena i test notturni sono in genere nella norma» | «Quando la causa è psicologica, di solito le erezioni notturne e al risveglio ci sono, come indicano le linee guida EAU.» | Termini tecnici non spiegati. | B |
| Foucault | «è una delle ricerche più frequenti su questi temi» | «Se l'hai cercato su Google, non sei la sola persona a farlo.» | Dato senza fonte. | B |
| Approfondimenti (sezione) | «quando un pezzo ha più di un anno lo segnalo con un avviso» | Va bene se qualcuno lo farà davvero (è una promessa che richiede manutenzione). | — | B |

**Introduzioni delle sezioni (testo di Alessio)**: non ci sono problemi seri. Vanno corretti solo
«non è una colpa tua» e «stare più tranquillo» (al maschile). Le introduzioni ripetono gli slogan
della home (vedi § 2): va bene che la voce sia la stessa, ma meglio non ripetere le frasi parola per parola.

**Pagine piccole**: 404 a posto. domanda-inviata a posto («La leggo io, e solo io» è coerente). Il
blog/index è chiaro; il problema sono solo i sommari tutti uguali («Ecco…», «con calma»).

---

## 6. Le 10 modifiche di testo più utili

1. **legale.html**: correggere «non ha moduli» nell'In breve e riempire (o nascondere) i due
   segnaposto, cioè Disdette e il periodo di cancellazione delle domande. Togliere il link «Disdette e
   rimborsi» dalla home finché il testo non c'è.
2. **Foucault**: trasformare in corsivo vero i 5 titoli tra asterischi, anche nel sito vero. Sistemare la frase senza soggetto «Serve a capire…».
3. **Home, togliere «Parole nella stanza»** (frasi attribuite a persone seguite, terzo blocco di citazioni).
4. **Home, unire «Perché me», «Cosa non sono» e «A cosa serve davvero un sessuologo»** in una
   sezione «Cosa faccio, e cosa no» (~110 parole, testo al § 1.2). Il titolo diventa «consulente in sessuologia».
5. **Home, unire Manifesto e Chi sono** con una sola terzina (i tre principi). Togliere i sopratitoli
   «Perché esisto», «Posizionamento», «Onestà», «Torino · 2026».
6. **15 minuti, una formula sola**: «Una telefonata di 15 minuti, gratis», al massimo 2 volte in home.
   Nel blog togliere «i primi», che fa pensare a uno sconto sulla consulenza.
7. **Incontri e prezzi coerenti**: niente «4-5 incontri» (i percorsi vanno da 3 a 5), FAQ 04 riscritta,
   «incontro» e mai «seduta», «280 € a persona», spiegare il «300 € se vieni da solo», spiegare o togliere DEOPIARCA.
8. **Dove lavora, una formula sola** su tutto il sito: per esempio «Online in tutta Italia · a domicilio a
   Torino e dintorni». Togliere «Sede» se non c'è uno studio.
9. **Ripulire i segnali AI in home**: niente trattini lunghi nel testo, « » al posto di `" "`, «Dirlo
   prima evita…», «Ne vuoi parlare?» al posto di «Pronto a parlarne?», «Non mi ritrovo più…» al posto di «perso/a».
10. **Blog**: variare sommari e chiusure (meno «Ecco…» e «con calma», niente slogan incollati in ogni
    articolo). Riscrivere il paragrafo sulla sicurezza nel kink, la casella e la nota del modulo, e il
    paragrafo «terapia sessuale» in parlare-col-partner.
