# -*- coding: utf-8 -*-

main_text = '''Benvenuto nel Catalogo di InventoryBot!
Qui puoi trovare una raccolta di tutti gli oggetti (si spera) disponibili su @InventoryBot.

Gli oggetti generalmente vengono aggiunti al catalogo dagli utenti stessi, per fare in modo di essere sempre al passo con i nuovi aggiornamenti.
Contribuire e' molto semplice, per sapere come fare usa il comando /helpcontribuisci .

Per consultare il catalogo esistono diversi comandi. Per sapere quali sono e come funzionano usa /helpcomandi .

Per qualsiasi tipo di segnalazione, suggerimento o dubbio non esitare a contattare direttamente @Carlovan.'''

commands_text = '''<b>Comando inventario</b>
Il comando /inventario ti permette di filtrare il catalogo e di ottenere la lista degli oggetti corrispondenti alla tua ricerca.
E' possibile applicare dei filtri sia sulla rarita' che sul nome. Prima vanno specificate tutte le rarita'.
<i>Ad esempio per vedere gli oggetti S e S+ il comando e':</i>
<pre>/inventario s s+</pre>
<i>Per vedere i bauli R o S uso:</i>
<pre>/inventario r s baul</pre>
E' inoltre possibile utilizzare dei filtri particolari: <code>+</code> per vedere tutti i +; <code>L</code> per vedere gli Lxx; <code>[usabile]</code> per vedere gli usabili.
Se non viene specificato alcun filtro verranno selezionati tutti gli oggetti.

<b>Comando conta</b>
Il comando /conta si comporta nello stesso identico modo del comando /inventario, tranne per il fatto che non fornisce la lista degli oggetti ma solo il numero.

<b>Comando ultimi</b>
Utilizzando il comando /ultimi è possibile vedere gli ultimi 10 oggetti aggiunti <b>al catalogo</b> (non necessariamente al gioco).

<b>Comando confronta</b>
Il comando /confronta invece ti permette di controllare il tuo inventario personale e sapere quali oggetti ti mancano.
Quando esegui il comando puoi specificare un filtro (ad esempio <code>/confronta +</code>) che verra' usato per effettuare il confronto.
Ti verra' chiesto di mandare il tuo inventario: in questa fase puoi inoltrare dal bot il risultato dei comandi <code>/mostra</code>, <code>/inventario</code>, <code>/inv2</code>, <code>/esporta</code>.
Quando hai finito di inviare i tuoi oggetti esegui il comando <code>/fine</code> per terminare e ottenere la lista degli oggetti che ti mancano.
Per annullare in qualsiasi momento esegui <code>/annulla</code>.'''

contribute_text = '''Per contribuire al catalogo devi inoltrare i messaggi da @InventoryBot.
Sono supportati i seguenti comandi: <code>/mostra</code>, <code>/inventario</code>, <code>/inv2</code>, <code>/esporta</code>.
GRAZIE MILLE DELL'AIUTO!'''

admin_commands_text = '''<b>Comandi admin</b>
<i>/adadd itemtext</i>  : per aggiungere un item.
<i>/adinventario ...</i>  : come <code>/inventario</code> ma mostra gli id degli item.
<i>/addelete itemid1 [idemid2 itemid3 ...]</i>  : per eliminare degli item.
<i>/adsetadmin username bool</i>  : imposta il flag item dell'utente al valore specificato (true se valore = 't', 'true', '1')'''
